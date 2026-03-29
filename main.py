"""Selenium MCP Server"""

from mcp.server.fastmcp import FastMCP

from src import navigation, session, elements


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


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
