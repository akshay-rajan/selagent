"""Click, type, clear, hover, drag-and-drop, file upload."""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.locators import resolve
from src.session import get_driver
from src.utils import ok, safe


def _find(strategy: str, value: str, timeout: int = 10):
    """Internal: locate a single element with an explicit wait."""
    by, sel = resolve(strategy, value)
    return WebDriverWait(get_driver(), timeout).until(
        EC.presence_of_element_located((by, sel))
    )


@safe
def click_element(strategy: str, value: str, timeout: int = 10) -> dict:
    """Click on the element identified by the given locator."""
    el = _find(strategy, value, timeout)
    el.click()
    return ok(message="Element clicked")


@safe
def type_text(
    strategy: str, value: str, text: str, clear_first: bool = True, timeout: int = 10
) -> dict:
    """Type text into an input/textarea element. Optionally clears existing content first."""
    el = _find(strategy, value, timeout)
    if clear_first:
        el.clear()
    el.send_keys(text)
    return ok(message="Typed text into element")


@safe
def clear_input(strategy: str, value: str, timeout: int = 10) -> dict:
    """Clear the content of an input/textarea element."""
    el = _find(strategy, value, timeout)
    el.clear()
    return ok(message="Input cleared")


@safe
def hover_element(strategy: str, value: str, timeout: int = 10) -> dict:
    """Hover over an element."""
    el = _find(strategy, value, timeout)
    ActionChains(get_driver()).move_to_element(el).perform()
    return ok(message="Hovered over element")


@safe
def drag_and_drop(
    src_strategy: str,
    src_value: str,
    dst_strategy: str,
    dst_value: str,
    timeout: int = 10,
) -> dict:
    """Drag an element and drop it onto another element."""
    src = _find(src_strategy, src_value, timeout)
    dst = _find(dst_strategy, dst_value, timeout)
    ActionChains(get_driver()).drag_and_drop(src, dst).perform()
    return ok(message="Drag and drop completed")


@safe
def upload_file(strategy: str, value: str, file_path: str, timeout: int = 10) -> dict:
    """Upload a file by sending the file path to a file-type input element."""
    el = _find(strategy, value, timeout)
    el.send_keys(file_path)
    return ok(message=f"File uploaded: {file_path}")
