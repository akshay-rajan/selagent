"""Dropdowns, checkboxes, radios, fill-by-label, and high-level submit."""

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from src.locators import resolve
from src.session import get_driver
from src.utils import ok, err, safe


def _find(strategy: str, value: str, timeout: int = 10):

    by, sel = resolve(strategy, value)
    return WebDriverWait(get_driver(), timeout).until(
        EC.presence_of_element_located((by, sel))
    )


@safe
def select_dropdown(
    strategy: str,
    value: str,
    *,
    option_text: str | None = None,
    option_value: str | None = None,
    option_index: int | None = None,
    timeout: int = 10,
) -> dict:
    """
    Select an option from a <select> dropdown.
    Provide exactly one of option_text, option_value, or option_index.
    """
    el = _find(strategy, value, timeout)
    sel = Select(el)
    if option_text is not None:
        sel.select_by_visible_text(option_text)
    elif option_value is not None:
        sel.select_by_value(option_value)
    elif option_index is not None:
        sel.select_by_index(option_index)
    else:
        return err("Provide option_text, option_value, or option_index")
    return ok(message="Option selected")


@safe
def check_checkbox(strategy: str, value: str, timeout: int = 10) -> dict:
    """Ensure a checkbox is checked."""
    el = _find(strategy, value, timeout)
    if not el.is_selected():
        el.click()
    return ok(message="Checkbox checked")


@safe
def uncheck_checkbox(strategy: str, value: str, timeout: int = 10) -> dict:
    """Ensure a checkbox is unchecked."""
    el = _find(strategy, value, timeout)
    if el.is_selected():
        el.click()
    return ok(message="Checkbox unchecked")


@safe
def choose_radio(strategy: str, value: str, timeout: int = 10) -> dict:
    """Select a radio button."""
    el = _find(strategy, value, timeout)
    if not el.is_selected():
        el.click()
    return ok(message="Radio selected")


@safe
def submit_form(strategy: str = "tag", value: str = "form", timeout: int = 10) -> dict:
    """Submit a form element. Defaults to the first <form> on the page."""
    el = _find(strategy, value, timeout)
    el.submit()
    driver = get_driver()
    return ok({"url": driver.current_url, "title": driver.title}, "Form submitted")


@safe
def fill_form_by_label(fields: dict[str, str], timeout: int = 10) -> dict:
    """
    Fill form fields using flexible matching. Each key in *fields* is matched
    against input name, id, placeholder, or associated <label> text.  Values
    are typed into the matched field.

    Args:
        fields: Mapping of field identifier -> value to type.
        timeout: Wait timeout per field.

    Returns:
        Report of which fields were filled and which failed.
    """

    driver = get_driver()
    filled: list[str] = []
    failed: list[str] = []

    for key, text in fields.items():
        el = None
        # Try id
        els = driver.find_elements(By.ID, key)
        if els:
            el = els[0]
        # Try name
        if el is None:
            els = driver.find_elements(By.NAME, key)
            if els:
                el = els[0]
        # Try placeholder (CSS)
        if el is None:
            for attr in ("placeholder", "aria-label"):
                els = driver.find_elements(By.CSS_SELECTOR, f'[{attr}="{key}"]')
                if els:
                    el = els[0]
                    break
        # Try label text → for attribute → element
        if el is None:
            labels = driver.find_elements(
                By.XPATH, f"//label[contains(normalize-space(.), '{key}')]"
            )
            for lbl in labels:
                for_id = lbl.get_attribute("for")
                if for_id:
                    targets = driver.find_elements(By.ID, for_id)
                    if targets:
                        el = targets[0]
                        break

        if el is not None:
            el.clear()
            el.send_keys(text)
            filled.append(key)
        else:
            failed.append(key)

    msg = f"Filled {len(filled)} field(s)"
    if failed:
        msg += f"; could not find {len(failed)} field(s): {failed}"
    return ok({"filled": filled, "failed": failed}, msg)


@safe
def submit_and_return_text(
    strategy: str = "tag", value: str = "form", wait_seconds: int = 5, timeout: int = 10
) -> dict:
    """
    Submit the form, wait for navigation/DOM update, and return the visible
    text on the resulting page.
    """

    el = _find(strategy, value, timeout)
    old_url = get_driver().current_url
    el.submit()

    # Wait for URL change or a short fixed delay as fallback
    try:
        WebDriverWait(get_driver(), wait_seconds).until(EC.url_changes(old_url))
    except Exception:
        time.sleep(1)

    driver = get_driver()
    body = driver.find_element("tag name", "body")
    return ok(
        {
            "url": driver.current_url,
            "title": driver.title,
            "text": body.text,
        },
        "Form submitted and page text captured",
    )
