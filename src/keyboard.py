"""Keyboard interactions"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.session import get_driver
from src.locators import resolve
from src.utils import ok, safe

_KEY_MAP: dict[str, str] = {
    "enter": Keys.ENTER,
    "return": Keys.RETURN,
    "tab": Keys.TAB,
    "escape": Keys.ESCAPE,
    "esc": Keys.ESCAPE,
    "backspace": Keys.BACKSPACE,
    "delete": Keys.DELETE,
    "space": Keys.SPACE,
    "up": Keys.ARROW_UP,
    "down": Keys.ARROW_DOWN,
    "left": Keys.ARROW_LEFT,
    "right": Keys.ARROW_RIGHT,
    "home": Keys.HOME,
    "end": Keys.END,
    "pageup": Keys.PAGE_UP,
    "pagedown": Keys.PAGE_DOWN,
    "f1": Keys.F1,
    "f2": Keys.F2,
    "f3": Keys.F3,
    "f4": Keys.F4,
    "f5": Keys.F5,
    "f6": Keys.F6,
    "f7": Keys.F7,
    "f8": Keys.F8,
    "f9": Keys.F9,
    "f10": Keys.F10,
    "f11": Keys.F11,
    "f12": Keys.F12,
    "ctrl": Keys.CONTROL,
    "control": Keys.CONTROL,
    "alt": Keys.ALT,
    "shift": Keys.SHIFT,
    "meta": Keys.META,
    "command": Keys.COMMAND,
}


def _resolve_key(name: str) -> str:
    """Return a Keys constant for *name*, or the literal string if not special."""
    return _KEY_MAP.get(name.lower().strip(), name)


@safe
def send_keys(strategy: str, value: str, keys: str, timeout: int = 10) -> dict:
    """Send a string of keys to the element located by the given locator."""

    by, sel = resolve(strategy, value)
    el = WebDriverWait(get_driver(), timeout).until(
        EC.presence_of_element_located((by, sel))
    )
    el.send_keys(keys)
    return ok(message="Keys sent to element")


@safe
def press_key(key_name: str) -> dict:
    """
    Press a special key globally (not targeted at an element).

    Args:
        key_name: Human-readable key name, e.g. 'enter', 'tab', 'escape'.
    """
    key = _resolve_key(key_name)
    ActionChains(get_driver()).send_keys(key).perform()
    return ok(message=f"Key '{key_name}' pressed")


@safe
def key_combo(*key_names: str) -> dict:
    """
    Press a keyboard shortcut (e.g. ctrl+a, ctrl+shift+t).

    Args:
        key_names: Two or more key names, e.g. 'ctrl', 'a'.
    """
    resolved = [_resolve_key(k) for k in key_names]
    ac = ActionChains(get_driver())
    # Hold modifiers, press final key, release
    for k in resolved[:-1]:
        ac.key_down(k)
    ac.send_keys(resolved[-1])
    for k in reversed(resolved[:-1]):
        ac.key_up(k)
    ac.perform()
    return ok(message=f"Key combo {'+'.join(key_names)} pressed")
