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


@mcp.tool()
def get_elements_by_id(link: str, element_id: str) -> list[str]:
    """
    Get all elements by HTML id and return their text content.
    Args:
        link (str): The URL of the web page to fetch.
        element_id (str): The id attribute to search for.
    Returns:
        list[str]: Text content of all elements with the given id.
    """
    return helpers.get_elements_by_id(link, element_id)


@mcp.tool()
def get_elements_by_class_name(link: str, class_name: str) -> list[str]:
    """
    Get all elements by HTML class name and return their text content.
    Args:
        link (str): The URL of the web page to fetch.
        class_name (str): The class name to search for.
    Returns:
        list[str]: Text content of all elements with the given class name.
    """
    return helpers.get_elements_by_class_name(link, class_name)


@mcp.tool()
def get_elements_by_tag_name(link: str, tag_name: str) -> list[str]:
    """
    Get all elements by HTML tag name and return their text content.
    Args:
        link (str): The URL of the web page to fetch.
        tag_name (str): The tag name to search for (e.g., 'div', 'span').
    Returns:
        list[str]: Text content of all elements with the given tag name.
    """
    return helpers.get_elements_by_tag_name(link, tag_name)


@mcp.tool()
def get_elements_by_data_attribute(link: str, data_attr: str, value: str = None) -> list[str]:
    """
    Get all elements by data attribute (e.g., data-foo) and return their text content.
    Args:
        link (str): The URL of the web page to fetch.
        data_attr (str): The data attribute name (without 'data-').
        value (str, optional): The value to match. If not provided, matches any value for the attribute.
    Returns:
        list[str]: Text content of all elements with the given data attribute (and value, if specified).
    """
    return helpers.get_elements_by_data_attribute(link, data_attr, value)


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
