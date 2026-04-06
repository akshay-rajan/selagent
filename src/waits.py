"""Explicit waits for element presence, text, URL change, page load."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.session import get_driver
from src.locators import resolve
from src.utils import ok, safe


@safe
def wait_for_element(
    strategy: str, value: str, timeout: int = 10, visible: bool = False
) -> dict:
    """
    Wait until an element is present (or visible) in the DOM.

    Args:
        strategy: Locator strategy.
        value: Selector value.
        timeout: Max seconds to wait.
        visible: If True, wait for the element to also be visible.
    """
    by, sel = resolve(strategy, value)
    condition = (
        EC.visibility_of_element_located if visible else EC.presence_of_element_located
    )
    WebDriverWait(get_driver(), timeout).until(condition((by, sel)))
    return ok(message="Element found")


@safe
def wait_for_text(text: str, timeout: int = 10) -> dict:
    """Wait until the given text appears anywhere in the page body."""

    def _text_present(driver):
        body = driver.find_element("tag name", "body")
        return text in body.text

    WebDriverWait(get_driver(), timeout).until(_text_present)
    return ok(message=f"Text '{text}' appeared on page")


@safe
def wait_for_url_change(current_url: str, timeout: int = 10) -> dict:
    """Wait until the page URL differs from *current_url*."""
    WebDriverWait(get_driver(), timeout).until(EC.url_changes(current_url))
    return ok({"url": get_driver().current_url}, "URL changed")


@safe
def wait_for_url_contains(fragment: str, timeout: int = 10) -> dict:
    """Wait until the page URL contains the given fragment."""
    WebDriverWait(get_driver(), timeout).until(EC.url_contains(fragment))
    return ok({"url": get_driver().current_url}, f"URL contains '{fragment}'")


@safe
def wait_for_page_load(timeout: int = 15) -> dict:
    """Wait until document.readyState is 'complete'."""

    def _ready(driver):
        return driver.execute_script("return document.readyState") == "complete"

    WebDriverWait(get_driver(), timeout).until(_ready)
    return ok(message="Page fully loaded")
