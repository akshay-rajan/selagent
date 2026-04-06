# <img src="./logo.svg" width="20" height="20"> SelAgent

A Selenium-powered MCP server that exposes browser automation as tool calls. Designed to let AI agents navigate, interact with, and test web pages through natural language.

## Tools

### Browser

| Tool | Description |
|------|-------------|
| `configure_browser` | Set headless or visible mode (before first navigation) |
| `reset_browser` | Quit the current session and start a fresh one |
| `quit_browser` | Close the browser and release all resources |

### Navigation

| Tool | Description |
|------|-------------|
| `open_url` | Navigate to a URL and wait for page load |
| `get_current_url` | Return the current page URL |
| `get_page_title` | Return the page title |
| `get_page_source` | Return the full HTML source |
| `go_back` / `go_forward` | Browser history navigation |
| `refresh_page` | Reload the current page |

### Element Finding & Extraction

| Tool | Description |
|------|-------------|
| `find_element` | Find a single element by locator (id, name, class, css, xpath, tag, data-*) |
| `find_elements` | Find all matching elements |
| `get_text_from_element` | Get visible text of an element |
| `get_attribute_value` | Get an HTML attribute value |
| `get_all_text_on_page` | Return all visible text on the page |
| `extract_links` | Extract all `<a>` elements with href, id, text |
| `extract_images` | Extract all `<img>` elements with src, alt, id |
| `extract_inputs` | Extract all `<input>` elements with type, name, id, placeholder, value |
| `extract_buttons` | Extract all `<button>` elements with type, name, id, text |
| `extract_forms` | Extract all `<form>` elements with action, method, id, name |

### Actions

| Tool | Description |
|------|-------------|
| `click_element` | Click an element |
| `type_text` | Type text into an input/textarea (clears first by default) |
| `clear_input` | Clear the content of an input/textarea |
| `hover_element` | Hover the mouse over an element |
| `drag_and_drop` | Drag source element onto destination element |
| `upload_file` | Upload a file to a file-type input |

### Forms

| Tool | Description |
|------|-------------|
| `select_dropdown` | Select an option from a `<select>` dropdown |
| `check_checkbox` / `uncheck_checkbox` | Toggle checkbox state |
| `choose_radio` | Select a radio button |
| `fill_form_by_label` | Fill form fields by matching name, id, placeholder, or label text |
| `submit_form` | Submit a form element |
| `submit_and_return_text` | Submit a form and return the resulting page text |

### Explicit Waits

| Tool | Description |
|------|-------------|
| `wait_for_element` | Wait until an element is present (or visible) |
| `wait_for_text` | Wait until text appears on the page |
| `wait_for_url_change` | Wait until the URL changes |
| `wait_for_url_contains` | Wait until the URL contains a fragment |
| `wait_for_page_load` | Wait until `document.readyState` is complete |

### Assertions

| Tool | Description |
|------|-------------|
| `assert_text_present` / `assert_text_not_present` | Verify text presence on page |
| `assert_element_exists` | Verify an element exists in the DOM |
| `assert_element_visible` | Verify an element is visible |
| `assert_element_enabled` | Verify an element is enabled |

### Screenshots

| Tool | Description |
|------|-------------|
| `take_screenshot` | Capture a full-page screenshot (saves to temp if no path given) |

### Windows & Frames

| Tool | Description |
|------|-------------|
| `list_windows` | List all open window/tab handles |
| `switch_to_window` | Switch to a window/tab by handle |
| `close_window` | Close the current window/tab |
| `switch_to_frame` | Switch into an iframe by locator or index |
| `switch_to_default_content` | Exit all iframes back to the top-level page |

### Alerts

| Tool | Description |
|------|-------------|
| `accept_alert` | Accept (OK) the current alert |
| `dismiss_alert` | Dismiss (Cancel) the current alert |
| `get_alert_text` | Read alert text without acting on it |

### Scrolling

| Tool | Description |
|------|-------------|
| `scroll_to_element` | Scroll until an element is centered in viewport |
| `scroll_to_top` / `scroll_to_bottom` | Scroll to page extremes |
| `scroll_by` | Scroll by a relative pixel amount |

### Keyboard

| Tool | Description |
|------|-------------|
| `send_keys_to_element` | Send keys to a specific element |
| `press_key` | Press a special key globally (enter, tab, escape, etc.) |
| `key_combo` | Press a keyboard shortcut (e.g. ctrl+a, ctrl+shift+t) |

### JavaScript & Inspection

| Tool | Description |
|------|-------------|
| `execute_javascript` | Execute arbitrary JavaScript and return the result |
| `inspect_page` | Return a structured summary of all interactive elements on the page |


## Project Structure

```
SelAgent/
├── main.py              # MCP tool registration (entry point)
├── src/
│   ├── session.py       # Browser session management
│   ├── locators.py      # Locator strategy resolution
│   ├── utils.py         # Response builders, error handling, screenshots, windows, frames, JS, inspection
│   ├── navigation.py    # URL navigation, history, refresh
│   ├── elements.py      # Element finding and data extraction
│   ├── actions.py       # Click, type, hover, drag-and-drop, file upload
│   ├── forms.py         # Dropdowns, checkboxes, radios, form fill and submit
│   ├── waits.py         # Explicit waits for elements, text, URL, page load
│   ├── assertions.py    # Text and element assertions
│   ├── alerts.py        # Alert accept, dismiss, read text
│   ├── scroll.py        # Scrolling and viewport control
│   └── keyboard.py      # Keyboard interactions and shortcuts
```


## Prerequisites

- [UV Package Manager](https://docs.astral.sh/uv/#installation)

## Setting Up

```sh
# Initialize a new UV (an alternative to 'pip') project
uv init
```

```sh
# Automatically update the Claude Desktop configuration
uv run mcp install main.py
```

> The above command only works if the Claude Desktop config is in *C:\Users\\[username]\AppData\Roaming\Claude*.
> Otherwise we have to manually update the configuration.
> If installed from the Microsoft Store, the path would be *C:\Users\\[username]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude*

---

**Claude Configuration (Recommended):**

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "selagent": {
      "command": "C:\\path\\to\\uv.exe",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "C:\\path\\to\\SelAgent\\main.py"
      ]
    }
  }
}
```

> The above command only works if the Claude Desktop config is in *C:\Users\\[username]\AppData\Roaming\Claude*.
> If installed from the Microsoft Store, the path would be *C:\Users\\[username]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude*

**VS Code Configuration:**

1. `Ctrl + Shift + P` → `MCP: Add Server`
2. Select `Command` and enter `uv run --with mcp[cli] mcp run C:\path\to\SelAgent\main.py`

```json
// C:\Users\[username]\AppData\Roaming\Code\User\mcp.json
{
  "servers": {
    "selagent": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "C:\\path\\to\\SelAgent\\main.py"
      ]
    }
  }
}
```

---

- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
