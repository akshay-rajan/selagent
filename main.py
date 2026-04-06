"""Selenium MCP Server"""

from mcp.server.fastmcp import FastMCP

from src import navigation, session, elements, actions, forms, waits, assertions
from src import alerts
from src import utils

mcp = FastMCP("selagent", json_response=True)


# ! BROWSER


@mcp.tool()
def configure_browser(headless: bool = True) -> dict:
    """
    Configure the browser to run in headless (default) or visible mode.
    To be called before any navigation, if the browser configuration needs to be changed.
    Only affects new sessions.
    """
    return session.configure(headless=headless)


@mcp.tool()
def reset_browser() -> dict:
    """Quit the current browser session and start a fresh one."""
    return navigation.reset_browser()


@mcp.tool()
def quit_browser() -> dict:
    """Close the browser entirely and release all resources."""
    return navigation.quit_browser()


# ! NAVIGATION


@mcp.tool()
def open_url(url: str) -> dict:
    """
    Navigate to the given URL and wait for the page to load.
    Returns the loaded URL and page title.
    """
    return navigation.open_url(url)


@mcp.tool()
def get_current_url() -> dict:
    """Return the current page URL."""
    return navigation.get_current_url()


@mcp.tool()
def get_page_title() -> dict:
    """Return the title of the current page."""
    return navigation.get_page_title()


@mcp.tool()
def get_page_source() -> dict:
    """Return the full HTML source of the current page."""
    return navigation.get_page_source()


@mcp.tool()
def go_back() -> dict:
    """Navigate back in browser history."""
    return navigation.go_back()


@mcp.tool()
def go_forward() -> dict:
    """Navigate forward in browser history."""
    return navigation.go_forward()


@mcp.tool()
def refresh_page() -> dict:
    """Reload the current page."""
    return navigation.refresh()


# ! ELEMENT FINDING & EXTRACTION


@mcp.tool()
def find_element(strategy: str, value: str, timeout: int = 10) -> dict:
    """
    Find a single element by locator strategy (id, name, class, css, xpath, tag, data-*).
    Returns tag, text, id, name, class, value, visibility, and enabled state.
    """
    return elements.find_element(strategy, value, timeout)


@mcp.tool()
def find_elements(strategy: str, value: str) -> dict:
    """
    Find all elements matching the locator.
    Returns a list of element summaries.
    """
    return elements.find_elements(strategy, value)


@mcp.tool()
def get_text_from_element(strategy: str, value: str) -> dict:
    """Get the visible text of a single element identified by the locator."""
    return elements.get_text(strategy, value)


@mcp.tool()
def get_attribute_value(strategy: str, value: str, attribute: str) -> dict:
    """Get a specific HTML attribute value from an element."""
    return elements.get_attribute(strategy, value, attribute)


@mcp.tool()
def get_all_text_on_page() -> dict:
    """Return all visible text on the current page."""
    return elements.get_all_text()


@mcp.tool()
def extract_links() -> dict:
    """Extract all <a> elements with their href, id, and text."""
    return elements.extract_links()


@mcp.tool()
def extract_images() -> dict:
    """Extract all <img> elements with their src, alt, and id."""
    return elements.extract_images()


@mcp.tool()
def extract_inputs() -> dict:
    """Extract all <input> elements with type, name, id, placeholder, and value."""
    return elements.extract_inputs()


@mcp.tool()
def extract_buttons() -> dict:
    """Extract all <button> elements with type, name, id, and text."""
    return elements.extract_buttons()


@mcp.tool()
def extract_forms() -> dict:
    """Extract all <form> elements with action, method, id, and name."""
    return elements.extract_forms()


# ! ACTIONS


@mcp.tool()
def click_element(strategy: str, value: str, timeout: int = 10) -> dict:
    """Click on the element identified by the locator strategy and value."""
    return actions.click_element(strategy, value, timeout)


@mcp.tool()
def type_text(
    strategy: str, value: str, text: str, clear_first: bool = True, timeout: int = 10
) -> dict:
    """Type text into an input or textarea. Clears existing content first by default."""
    return actions.type_text(strategy, value, text, clear_first, timeout)


@mcp.tool()
def clear_input(strategy: str, value: str, timeout: int = 10) -> dict:
    """Clear the content of an input or textarea element."""
    return actions.clear_input(strategy, value, timeout)


@mcp.tool()
def hover_element(strategy: str, value: str, timeout: int = 10) -> dict:
    """Hover the mouse over an element."""
    return actions.hover_element(strategy, value, timeout)


@mcp.tool()
def drag_and_drop(
    src_strategy: str,
    src_value: str,
    dst_strategy: str,
    dst_value: str,
    timeout: int = 10,
) -> dict:
    """Drag the source element and drop it onto the destination element."""
    return actions.drag_and_drop(
        src_strategy, src_value, dst_strategy, dst_value, timeout
    )


@mcp.tool()
def upload_file(strategy: str, value: str, file_path: str, timeout: int = 10) -> dict:
    """Upload a file by sending its absolute path to a file-type input element."""
    return actions.upload_file(strategy, value, file_path, timeout)


# ! FORMS


@mcp.tool()
def select_dropdown(
    strategy: str,
    value: str,
    option_text: str | None = None,
    option_value: str | None = None,
    option_index: int | None = None,
    timeout: int = 10,
) -> dict:
    """
    Select an option from a <select> dropdown.
    Provide one of option_text, option_value, or option_index.
    """
    return forms.select_dropdown(
        strategy,
        value,
        option_text=option_text,
        option_value=option_value,
        option_index=option_index,
        timeout=timeout,
    )


@mcp.tool()
def check_checkbox(strategy: str, value: str, timeout: int = 10) -> dict:
    """
    Ensure a checkbox is checked.
    No operation if already checked.
    """
    return forms.check_checkbox(strategy, value, timeout)


@mcp.tool()
def uncheck_checkbox(strategy: str, value: str, timeout: int = 10) -> dict:
    """
    Ensure a checkbox is unchecked.
    No operation if already unchecked.
    """
    return forms.uncheck_checkbox(strategy, value, timeout)


@mcp.tool()
def choose_radio(strategy: str, value: str, timeout: int = 10) -> dict:
    """Select a radio button."""
    return forms.choose_radio(strategy, value, timeout)


@mcp.tool()
def submit_form(strategy: str = "tag", value: str = "form", timeout: int = 10) -> dict:
    """
    Submit a form element.
    Defaults to the first <form> on the page.
    """
    return forms.submit_form(strategy, value, timeout)


@mcp.tool()
def fill_form_by_label(fields: dict[str, str], timeout: int = 10) -> dict:
    """
    Fill form fields using flexible matching.
    Keys are matched against input name, id, placeholder, or associated <label> text.
    Values are typed into the matched field.
    """
    return forms.fill_form_by_label(fields, timeout)


@mcp.tool()
def submit_and_return_text(
    strategy: str = "tag", value: str = "form", wait_seconds: int = 5, timeout: int = 10
) -> dict:
    """
    Submit a form, wait for navigation/DOM update,
    and return the visible text on the resulting page.
    """
    return forms.submit_and_return_text(strategy, value, wait_seconds, timeout)


# ! Explicit Waits


@mcp.tool()
def wait_for_element(
    strategy: str, value: str, timeout: int = 10, visible: bool = False
) -> dict:
    """Wait until an element is present (or visible) in the DOM."""
    return waits.wait_for_element(strategy, value, timeout, visible)


@mcp.tool()
def wait_for_text(text: str, timeout: int = 10) -> dict:
    """Wait until the given text appears anywhere on the page."""
    return waits.wait_for_text(text, timeout)


@mcp.tool()
def wait_for_url_change(current_url: str, timeout: int = 10) -> dict:
    """Wait until the page URL differs from the given URL."""
    return waits.wait_for_url_change(current_url, timeout)


@mcp.tool()
def wait_for_url_contains(fragment: str, timeout: int = 10) -> dict:
    """Wait until the page URL contains the given fragment."""
    return waits.wait_for_url_contains(fragment, timeout)


@mcp.tool()
def wait_for_page_load(timeout: int = 15) -> dict:
    """Wait until the page has fully loaded (document.readyState === 'complete')."""
    return waits.wait_for_page_load(timeout)


# ! Assertions


@mcp.tool()
def assert_text_present(text: str) -> dict:
    """
    Assert that the given text exists on the current page.
    Returns success or failure.
    """
    return assertions.assert_text_present(text)


@mcp.tool()
def assert_text_not_present(text: str) -> dict:
    """Assert that the given text does NOT exist on the current page."""
    return assertions.assert_text_not_present(text)


@mcp.tool()
def assert_element_exists(strategy: str, value: str) -> dict:
    """Assert that at least one element matching the locator exists in the DOM."""
    return assertions.assert_element_exists(strategy, value)


@mcp.tool()
def assert_element_visible(strategy: str, value: str) -> dict:
    """Assert that the element matching the locator is visible."""
    return assertions.assert_element_visible(strategy, value)


@mcp.tool()
def assert_element_enabled(strategy: str, value: str) -> dict:
    """Assert that the element matching the locator is enabled (not disabled)."""
    return assertions.assert_element_enabled(strategy, value)


# ! Take a screenshot
@mcp.tool()
def take_screenshot(file_path: str | None = None) -> dict:
    """
    Take a screenshot. Saves to a temp file if no path is given.
    Returns the file path.
    """
    return utils.take_screenshot(file_path)


# ! Window Navigation


@mcp.tool()
def list_windows() -> dict:
    """List all open browser windows/tabs and the current active handle."""
    return utils.list_windows()


@mcp.tool()
def switch_to_window(handle: str) -> dict:
    """Switch to the browser window/tab with the given handle."""
    return utils.switch_to_window(handle)


@mcp.tool()
def close_window() -> dict:
    """Close the current browser window/tab."""
    return utils.close_window()


#  ! iFrames


@mcp.tool()
def switch_to_frame(
    strategy: str | None = None, value: str | None = None, index: int | None = None
) -> dict:
    """
    Switch into an iframe.
    Provide a locator (strategy + value) or an integer index.
    """
    return utils.switch_to_frame(strategy, value, index)


@mcp.tool()
def switch_to_default_content() -> dict:
    """Switch back to the top-level page (exit all iframes)."""
    return utils.switch_to_default_content()


# ! Alerts


@mcp.tool()
def accept_alert() -> dict:
    """
    Accept (click OK on) the current browser alert.
    Returns the alert text.
    """
    return alerts.accept_alert()


@mcp.tool()
def dismiss_alert() -> dict:
    """
    Dismiss (click Cancel on) the current browser alert.
    Returns the alert text.
    """
    return alerts.dismiss_alert()


@mcp.tool()
def get_alert_text() -> dict:
    """Get the text of the current browser alert without accepting or dismissing it."""
    return alerts.get_alert_text()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
