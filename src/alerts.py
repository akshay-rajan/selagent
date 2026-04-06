"""Alert handling - accept, dismiss, read text."""

from src.session import get_driver
from src.utils import ok, safe


@safe
def accept_alert() -> dict:
    """Accept (click OK on) the current browser alert."""
    alert = get_driver().switch_to.alert
    text = alert.text
    alert.accept()
    return ok({"text": text}, "Alert accepted")


@safe
def dismiss_alert() -> dict:
    """Dismiss (click Cancel on) the current browser alert."""
    alert = get_driver().switch_to.alert
    text = alert.text
    alert.dismiss()
    return ok({"text": text}, "Alert dismissed")


@safe
def get_alert_text() -> dict:
    """Return the text of the current browser alert without acting on it."""
    return ok(get_driver().switch_to.alert.text)
