"""Selenium MCP Server"""

from mcp.server.fastmcp import FastMCP

from src import navigation


mcp = FastMCP("selagent", json_response=True)


# ! NAVIGATION

@mcp.tool()
def open_url(url: str) -> dict:
    """Navigate to the given URL and wait for the page to load. Returns the loaded URL and page title."""
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



if __name__ == "__main__":
    mcp.run(transport="streamable-http")
