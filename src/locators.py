"""Element Lookup Strategies."""

from selenium.webdriver.common.by import By


_STRATEGY_MAP: dict[str, str] = {
    "id":                 By.ID,
    "name":               By.NAME,
    "class":              By.CLASS_NAME,
    "class_name":         By.CLASS_NAME,
    "css":                By.CSS_SELECTOR,
    "css_selector":       By.CSS_SELECTOR,
    "xpath":              By.XPATH,
    "tag":                By.TAG_NAME,
    "tag_name":           By.TAG_NAME,
    "link_text":          By.LINK_TEXT,
    "partial_link_text":  By.PARTIAL_LINK_TEXT,
}


def resolve(strategy: str, value: str) -> tuple[str, str]:
    """
    Convert a (strategy, value) pair into a Selenium (By.***, selector) tuple.

    Args:
        strategy: One of the supported strategy names (id, name, class, css,
                  xpath, tag, link_text, partial_link_text) **or** a
                  ``data-*`` attribute name (e.g. ``data-testid``).
        value:    The selector value.

    Returns:
        A ``(By.***, selector_string)`` tuple ready for
        ``driver.find_element()`` / ``find_elements()``.

    Raises:
        ValueError: If the strategy is not recognised.
    """
    key = strategy.lower().strip()

    if key.startswith("data-"):
        return (By.CSS_SELECTOR, f'[{key}="{value}"]')

    by = _STRATEGY_MAP.get(key)
    if by is None:
        raise ValueError(
            f"Unknown locator strategy '{strategy}'. "
            f"Supported: {', '.join(sorted(_STRATEGY_MAP.keys()))}, data-*"
        )
    return (by, value)
