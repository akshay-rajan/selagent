# <img src="./logo.svg" width="20" height="20"> SelAgent

A Selenium-powered MCP server that exposes browser automation as tool calls. Designed to let AI agents navigate, interact with, and test web pages through natural language.

## Usage

**Prerequisites:**
- [UV Package Manager](https://docs.astral.sh/uv/#installation)

### 1. Initialize the Project

SelAgent uses `uv` (a fast alternative to `pip`). Run the following in your project directory:

```sh
uv init
```

### 2. Configure the MCP Server

You can install SelAgent automatically or configure it manually for your preferred client.

**Option A: Automatic Installation (Claude Desktop)**

```sh
uv run mcp install main.py
```

<details>
<summary>Note on Automatic Installation</summary>

<p>The above command only works if the Claude Desktop config is in <em>C:\Users\[username]\AppData\Roaming\Claude</em>.<br>
Otherwise you must manually update the configuration.<br>
If installed from the Microsoft Store, the path would be <em>C:\Users\[username]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude</em></p>

</details>
<br>

**Option B: Manual Configuration for Claude Desktop**

Add the following to your `claude_desktop_config.json`:

```json
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

<details>
<summary>Config File Locations</summary>

<p>Standard install: <em>C:\Users\[username]\AppData\Roaming\Claude</em>.<br>
Microsoft Store install: <em>C:\Users\[username]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude</em></p>

</details>
<br>

**Option C: Manual Configuration for VS Code**

1. Press `Ctrl + Shift + P` and select `MCP: Add Server`
2. Select `Command` and enter: `uv run --with mcp[cli] mcp run C:\path\to\SelAgent\main.py`
3. Alternatively, update `C:\Users\[username]\AppData\Roaming\Code\User\mcp.json` directly:

```json
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

## Tools

#### Browser

- Set headless or visible mode (before first navigation)
- Quit the current session and start a fresh one
- Close the browser and release all resources

#### Navigation

- Navigate to a URL and wait for page load
- Return the current page URL
- Return the page title
- Return the full HTML source
- Browser history navigation
- Reload the current page

#### Element Finding & Extraction

- Find a single element by locator (id, name, class, css, xpath, tag, data-*)
- Find all matching elements
- Get visible text of an element
- Get an HTML attribute value
- Return all visible text on the page
- Extract all `<a>` elements with href, id, text
- Extract all `<img>` elements with src, alt, id
- Extract all `<input>` elements with type, name, id, placeholder, value
- Extract all `<button>` elements with type, name, id, text
- Extract all `<form>` elements with action, method, id, name

#### Actions

- Click an element
- Type text into an input/textarea (clears first by default)
- Clear the content of an input/textarea
- Hover the mouse over an element
- Drag source element onto destination element
- Upload a file to a file-type input

#### Forms

- Select an option from a `<select>` dropdown
- Toggle checkbox state
- Select a radio button
- Fill form fields by matching name, id, placeholder, or label text
- Submit a form element
- Submit a form and return the resulting page text

#### Explicit Waits

- Wait until an element is present (or visible)
- Wait until text appears on the page
- Wait until the URL changes
- Wait until the URL contains a fragment
- Wait until `document.readyState` is complete

#### Assertions

- Verify text presence on page
- Verify an element exists in the DOM
- Verify an element is visible
- Verify an element is enabled

#### Screenshots

- Capture a full-page screenshot (saves to temp if no path given)

#### Windows & Frames

- List all open window/tab handles
- Switch to a window/tab by handle
- Close the current window/tab
- Switch into an iframe by locator or index
- Exit all iframes back to the top-level page

#### Alerts

- Accept (OK) the current alert
- Dismiss (Cancel) the current alert
- Read alert text without acting on it

#### Scrolling

- Scroll until an element is centered in viewport
- Scroll to page extremes
- Scroll by a relative pixel amount

#### Keyboard

- Send keys to a specific element
- Press a special key globally (enter, tab, escape, etc.)
- Press a keyboard shortcut (e.g. ctrl+a, ctrl+shift+t)

#### JavaScript & Inspection

- Execute arbitrary JavaScript and return the result
- Return a structured summary of all interactive elements on the page

#### Cookies

- Return all cookies for the current domain
- Return a single cookie by name
- Add a cookie with the given name and value
- Delete a specific cookie by name
- Delete all cookies for the current domain

#### Local Storage

- Get a value from localStorage by key
- Set a key-value pair in localStorage
- Return all localStorage key-value pairs
- Clear all localStorage entries

#### Session Storage

- Get a value from sessionStorage by key
- Set a key-value pair in sessionStorage
- Return all sessionStorage key-value pairs
- Clear all sessionStorage entries

## Additional Resources

- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
