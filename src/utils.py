"""Response builders and Error-handling decorator."""

from functools import wraps
from typing import Any, Callable


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
