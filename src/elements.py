"""Element finding and data extraction."""

from typing import Any
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.session import get_driver
from src.locators import resolve
from src.utils import ok, err, safe


@safe
def find_element(strategy: str, value: str, timeout: int = 10) -> dict:
    """
    Find a single element and return summary info.

    Args:
        strategy: Locator strategy (id, name, class, css, xpath, tag, data-*).
        value: Selector value.
        timeout: Seconds to wait.
    """

    by, sel = resolve(strategy, value)
    driver = get_driver()
    el = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, sel)))
    return ok(
        {
            "tag": el.tag_name,
            "text": el.text,
            "id": el.get_attribute("id"),
            "name": el.get_attribute("name"),
            "class": el.get_attribute("class"),
            "value": el.get_attribute("value"),
            "visible": el.is_displayed(),
            "enabled": el.is_enabled(),
        },
        "Element found",
    )


@safe
def find_elements(strategy: str, value: str) -> dict:
    """Find all matching elements and return a list of summaries."""
    by, sel = resolve(strategy, value)
    elements = get_driver().find_elements(by, sel)
    items = []
    for el in elements:
        items.append(
            {
                "tag": el.tag_name,
                "text": el.text[:200],
                "id": el.get_attribute("id"),
                "name": el.get_attribute("name"),
                "class": el.get_attribute("class"),
                "value": el.get_attribute("value"),
                "visible": el.is_displayed(),
            }
        )
    return ok(items, f"Found {len(items)} element(s)")


@safe
def get_text(strategy: str, value: str) -> dict:
    """Get the visible text of a single element."""
    by, sel = resolve(strategy, value)
    el = get_driver().find_element(by, sel)
    return ok(el.text)


@safe
def get_attribute(strategy: str, value: str, attribute: str) -> dict:
    """Get an attribute value from a single element."""
    by, sel = resolve(strategy, value)
    el = get_driver().find_element(by, sel)
    return ok(el.get_attribute(attribute))


@safe
def get_all_text() -> dict:
    """Return all visible text on the page."""
    body = get_driver().find_element("tag name", "body")
    return ok(body.text)


def _collect(tag: str, attrs: list[str]) -> list[dict]:
    elements = get_driver().find_elements("tag name", tag)
    items = []
    for el in elements:
        item = {a: el.get_attribute(a) for a in attrs}
        item["text"] = el.text[:200]
        items.append(item)
    return items


@safe
def extract_links() -> dict:
    """Return all <a> elements with href, text, and id."""
    return ok(_collect("a", ["href", "id"]))


@safe
def extract_images() -> dict:
    """Return all <img> elements with src, alt, and id."""
    return ok(_collect("img", ["src", "alt", "id"]))


@safe
def extract_inputs() -> dict:
    """Return all <input> elements with type, name, id, placeholder, value."""
    return ok(_collect("input", ["type", "name", "id", "placeholder", "value"]))


@safe
def extract_buttons() -> dict:
    """Return all <button> elements with type, name, id, text."""
    return ok(_collect("button", ["type", "name", "id"]))


@safe
def extract_forms() -> dict:
    """Return all <form> elements with action, method, id, name."""
    return ok(_collect("form", ["action", "method", "id", "name"]))
