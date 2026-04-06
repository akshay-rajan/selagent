"""Verify text, element visibility, existence, and enabled state."""

from src.session import get_driver
from src.locators import resolve
from src.utils import ok, err, safe


@safe
def assert_text_present(text: str) -> dict:
    """Assert that the given text exists somewhere in the page body."""
    body = get_driver().find_element("tag name", "body").text
    if text in body:
        return ok(message=f"Text '{text}' is present")
    return err(f"Text '{text}' not found on the page")


@safe
def assert_text_not_present(text: str) -> dict:
    """Assert that the given text does NOT exist in the page body."""
    body = get_driver().find_element("tag name", "body").text
    if text not in body:
        return ok(message=f"Text '{text}' is not present (as expected)")
    return err(f"Text '{text}' was found on the page but should not be")


@safe
def assert_element_exists(strategy: str, value: str) -> dict:
    """Assert that at least one element matching the locator exists in the DOM."""
    by, sel = resolve(strategy, value)
    els = get_driver().find_elements(by, sel)
    if els:
        return ok({"count": len(els)}, "Element exists")
    return err(f"No element found for ({strategy}, {value})")


@safe
def assert_element_visible(strategy: str, value: str) -> dict:
    """Assert that the matching element is visible on the page."""
    by, sel = resolve(strategy, value)
    els = get_driver().find_elements(by, sel)
    if not els:
        return err(f"No element found for ({strategy}, {value})")
    if els[0].is_displayed():
        return ok(message="Element is visible")
    return err("Element exists but is not visible")


@safe
def assert_element_enabled(strategy: str, value: str) -> dict:
    """Assert that the matching element is enabled (not disabled)."""
    by, sel = resolve(strategy, value)
    els = get_driver().find_elements(by, sel)
    if not els:
        return err(f"No element found for ({strategy}, {value})")
    if els[0].is_enabled():
        return ok(message="Element is enabled")
    return err("Element exists but is disabled")
