"""Response builders and Error-handling decorator."""

import os
import time
import tempfile
from functools import wraps
from typing import Any, Callable

from src.session import get_driver
from src.utils import ok, safe


def ok(data: Any = None, message: str = "OK") -> dict:
    """Build a success response dict."""

    return {"success": True, "message": message, "data": data}


def err(message: str, data: Any = None) -> dict:
    """Build an error response dict."""

    return {"success": False, "message": message, "data": data, "error": message}


def safe(fn: Callable) -> Callable:
    """Decorator: wraps a service function to convert exceptions into dictionaries using err()."""

    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> dict:
        try:
            return fn(*args, **kwargs)
        except Exception as exc:
            return err(f"{fn.__name__} failed: {exc}")

    return wrapper


@safe
def take_screenshot(file_path: str | None = None) -> dict:
    """
    Capture a full-page screenshot.

    Args:
        file_path: Optional path to save the PNG. If not provided, a temp
                   file is created in the system temp directory.

    Returns:
        Dict with the file path to the saved screenshot.
    """
    if file_path is None:
        tmp_dir = os.path.join(tempfile.gettempdir(), "selagent_screenshots")
        os.makedirs(tmp_dir, exist_ok=True)
        file_path = os.path.join(tmp_dir, f"screenshot_{int(time.time())}.png")

    get_driver().save_screenshot(file_path)
    return ok({"path": file_path}, f"Screenshot saved to {file_path}")


@safe
def list_windows() -> dict:
    """List all open window/tab handles and the current active handle."""
    driver = get_driver()
    return ok(
        {
            "current": driver.current_window_handle,
            "handles": driver.window_handles,
        }
    )


@safe
def switch_to_window(handle: str) -> dict:
    """Switch to the window/tab identified by *handle*."""
    get_driver().switch_to.window(handle)
    return ok(message=f"Switched to window {handle}")


@safe
def close_window() -> dict:
    """Close the current window/tab."""
    driver = get_driver()
    driver.close()
    handles = driver.window_handles
    if handles:
        driver.switch_to.window(handles[0])
    return ok(message="Window closed")


@safe
def switch_to_frame(
    strategy: str | None = None,
    value: str | None = None,
    index: int | None = None,
) -> dict:
    """
    Switch into an iframe.
    Provide either a locator (strategy + value) or an integer *index*.
    """
    driver = get_driver()
    if index is not None:
        driver.switch_to.frame(index)
    elif strategy and value:
        by, sel = resolve(strategy, value)
        el = driver.find_element(by, sel)
        driver.switch_to.frame(el)
    else:
        return {
            "success": False,
            "message": "Provide (strategy, value) or index",
            "error": "Missing arguments",
        }
    return ok(message="Switched to frame")


@safe
def switch_to_default_content() -> dict:
    """Switch back to the top-level page (exit all frames)."""
    get_driver().switch_to.default_content()
    return ok(message="Switched to default content")


@safe
def execute_javascript(script: str, *args: Any) -> dict:
    """
    Execute arbitrary JavaScript in the browser and return the result.

    Args:
        script: JavaScript code to execute.
        *args: Optional arguments available as ``arguments[0]``, etc. in the script.

    Returns:
        Dict with the script return value under 'data'.
    """
    result = get_driver().execute_script(script, *args)
    return ok(result, "JavaScript executed")
