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
