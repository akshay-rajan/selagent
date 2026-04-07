"""Cookies, localStorage, and sessionStorage management."""

from typing import Any

from src.session import get_driver
from src.utils import ok, safe


@safe
def get_cookies() -> dict:
    """Return all cookies for the current domain."""
    return ok(get_driver().get_cookies())


@safe
def get_cookie(name: str) -> dict:
    """Return a single cookie by name, or an error if not found."""
    cookie = get_driver().get_cookie(name)
    if cookie is None:
        return {
            "success": False,
            "message": f"Cookie '{name}' not found",
            "error": f"Cookie '{name}' not found",
            "data": None,
        }
    return ok(cookie)


@safe
def add_cookie(name: str, value: str, **kwargs: Any) -> dict:
    """
    Add a cookie to the current domain.

    Args:
        name: Cookie name.
        value: Cookie value.
        **kwargs: Optional cookie attributes (path, domain, secure, etc.).
    """
    cookie: dict[str, Any] = {"name": name, "value": value, **kwargs}
    get_driver().add_cookie(cookie)
    return ok(message=f"Cookie '{name}' added")


@safe
def delete_cookie(name: str) -> dict:
    """Delete a specific cookie by name."""
    get_driver().delete_cookie(name)
    return ok(message=f"Cookie '{name}' deleted")


@safe
def clear_cookies() -> dict:
    """Delete all cookies for the current domain."""
    get_driver().delete_all_cookies()
    return ok(message="All cookies cleared")


@safe
def get_local_storage(key: str) -> dict:
    """Get a value from localStorage."""
    val = get_driver().execute_script(f"return window.localStorage.getItem('{key}');")
    return ok(val)


@safe
def set_local_storage(key: str, value: str) -> dict:
    """Set a key-value pair in localStorage."""
    get_driver().execute_script(f"window.localStorage.setItem('{key}', '{value}');")
    return ok(message=f"localStorage['{key}'] set")


@safe
def remove_local_storage(key: str) -> dict:
    """Remove a single key from localStorage."""
    get_driver().execute_script(f"window.localStorage.removeItem('{key}');")
    return ok(message=f"localStorage['{key}'] removed")


@safe
def clear_local_storage() -> dict:
    """Clear all localStorage entries."""
    get_driver().execute_script("window.localStorage.clear();")
    return ok(message="localStorage cleared")


@safe
def get_all_local_storage() -> dict:
    """Return all localStorage key-value pairs as a dict."""
    data = get_driver().execute_script(
        "var d = {};"
        "for (var i = 0; i < localStorage.length; i++) {"
        "   var k = localStorage.key(i);"
        "   d[k] = localStorage.getItem(k);"
        "}"
        "return d;"
    )
    return ok(data)


@safe
def get_session_storage(key: str) -> dict:
    """Get a value from sessionStorage."""
    val = get_driver().execute_script(f"return window.sessionStorage.getItem('{key}');")
    return ok(val)


@safe
def set_session_storage(key: str, value: str) -> dict:
    """Set a key-value pair in sessionStorage."""
    get_driver().execute_script(f"window.sessionStorage.setItem('{key}', '{value}');")
    return ok(message=f"sessionStorage['{key}'] set")


@safe
def remove_session_storage(key: str) -> dict:
    """Remove a single key from sessionStorage."""
    get_driver().execute_script(f"window.sessionStorage.removeItem('{key}');")
    return ok(message=f"sessionStorage['{key}'] removed")


@safe
def clear_session_storage() -> dict:
    """Clear all sessionStorage entries."""
    get_driver().execute_script("window.sessionStorage.clear();")
    return ok(message="sessionStorage cleared")


@safe
def get_all_session_storage() -> dict:
    """Return all sessionStorage key-value pairs as a dict."""
    data = get_driver().execute_script(
        "var d = {};"
        "for (var i = 0; i < sessionStorage.length; i++) {"
        "   var k = sessionStorage.key(i);"
        "   d[k] = sessionStorage.getItem(k);"
        "}"
        "return d;"
    )
    return ok(data)
