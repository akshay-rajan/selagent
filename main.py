"""Selenium MCP Server"""

from mcp.server.fastmcp import FastMCP

import helpers


mcp = FastMCP("Demo", json_response=True)


@mcp.tool()
def get_page_title(link: str) -> str:
    """
    Retrieve the title of the web page at the specified URL.
    Args:
        link (str): The URL of the web page to fetch.
    Returns:
        str: The text content of the <title> tag from the web page, or an empty string if not found.
    """
    return helpers.get_title(link)


@mcp.tool()
def get_page_links(link: str) -> list[str]:
    """
    Extract all hyperlinks (anchor hrefs) from the given web page URL.
    Args:
        link (str): The URL of the web page to fetch.
    Returns:
        list[str]: A list of all href values found in <a> tags on the page.
    """
    return helpers.get_links(link)


@mcp.tool()
def get_meta_description(link: str) -> str:
    """
    Retrieve the meta description content from the web page at the specified URL.
    Args:
        link (str): The URL of the web page to fetch.
    Returns:
        str: The content of the <meta name="description"> tag, or an empty string if not found.
    """
    return helpers.get_meta_description(link)


@mcp.tool()
def get_h1_texts(link: str) -> list[str]:
    """
    Extract all <h1> tag texts from the given web page URL.
    Args:
        link (str): The URL of the web page to fetch.
    Returns:
        list[str]: A list of text content from all <h1> tags on the page.
    """
    return helpers.get_h1_texts(link)


@mcp.tool()
def get_images(link: str) -> list[str]:
    """
    Extract all image source URLs from the given web page URL.
    Args:
        link (str): The URL of the web page to fetch.
    Returns:
        list[str]: A list of src values from all <img> tags on the page.
    """
    return helpers.get_images(link)


@mcp.tool()
def get_text_content(link: str) -> str:
    """
    Retrieve the main visible text content from the web page at the specified URL.
    Args:
        link (str): The URL of the web page to fetch.
    Returns:
        str: The concatenated visible text content of the page.
    """
    return helpers.get_text_content(link)


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
