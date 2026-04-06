"""Scrolling and viewport control."""

from src.session import get_driver
from src.locators import resolve
from src.utils import ok, safe


@safe
def scroll_to_element(strategy: str, value: str) -> dict:
    """Scroll until the element is in the viewport."""
    by, sel = resolve(strategy, value)
    el = get_driver().find_element(by, sel)
    get_driver().execute_script("arguments[0].scrollIntoView({block:'center'});", el)
    return ok(message="Scrolled to element")


@safe
def scroll_to_top() -> dict:
    """Scroll to the top of the page."""
    get_driver().execute_script("window.scrollTo(0, 0);")
    return ok(message="Scrolled to top")


@safe
def scroll_to_bottom() -> dict:
    """Scroll to the bottom of the page."""
    get_driver().execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return ok(message="Scrolled to bottom")


@safe
def scroll_by(x: int = 0, y: int = 300) -> dict:
    """Scroll by a relative pixel amount."""
    get_driver().execute_script(f"window.scrollBy({x}, {y});")
    return ok(message=f"Scrolled by ({x}, {y})px")
