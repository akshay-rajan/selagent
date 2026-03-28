"""URL loading, browser history, page metadata."""

from src.session import get_driver, reset as _reset, quit_browser as _quit
from src.utils import ok, safe


@safe
def open_url(url: str) -> dict:
    """Navigate to the given URL and wait for the page to load."""

    driver = get_driver()
    driver.get(url)

    return ok(
        data={"url": driver.current_url, "title": driver.title}, message="Page loaded"
    )


@safe
def get_current_url() -> dict:
    """Return the current page URL."""

    return ok(get_driver().current_url)


@safe
def get_page_title() -> dict:
    """Return the current page title."""

    return ok(get_driver().title)


@safe
def get_page_source() -> dict:
    """Return the full page HTML."""

    return ok(get_driver().page_source)


@safe
def go_back() -> dict:
    """Navigate back in browser history."""

    driver = get_driver()
    driver.back()
    return ok(data={"url": driver.current_url}, message="Navigated back")


@safe
def go_forward() -> dict:
    """Navigate forward in browser history."""

    driver = get_driver()
    driver.forward()
    return ok(data={"url": driver.current_url}, message="Navigated forward")


@safe
def refresh() -> dict:
    """Reload the current page."""

    driver = get_driver()
    driver.refresh()
    return ok(data={"url": driver.current_url}, message="Page refreshed")


def reset_browser() -> dict:
    """Quit and relaunch the browser session."""

    return _reset()


def quit_browser() -> dict:
    """Quit the browser entirely."""

    return _quit()
