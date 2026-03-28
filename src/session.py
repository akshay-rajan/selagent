"""Browser session manager"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Module-level singleton Chrome driver to reuse across tool calls
_driver: webdriver.Chrome | None = None
_headless: bool = True


def configure(*, headless: bool = True) -> dict:
    """Set headless mode for future sessions."""

    global _headless
    _headless = headless
    return {"success": True, "message": f"Headless set to {headless}"}


def _build_driver() -> webdriver.Chrome:
    opts = Options()
    if _headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts,
    )


def get_driver() -> webdriver.Chrome:
    """Return the current driver, creating one if needed."""

    global _driver
    if _driver is None:
        _driver = _build_driver()
    return _driver


def quit_browser() -> dict:
    """Quit the browser and release resources."""

    global _driver
    if _driver is not None:
        try:
            _driver.quit()
        except Exception:
            pass
        _driver = None
    return {"success": True, "message": "Browser closed"}


def reset() -> dict:
    """Quit the current session and start a fresh one."""

    quit_browser()
    get_driver()
    return {"success": True, "message": "Browser session reset"}
