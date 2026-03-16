# SelAgent

## Web Scraping Utilities

SelAgent provides several web scraping tools accessible via MCP:

- **get_page_title(link: str) -> str**: Returns the &lt;title&gt; of the web page at the given URL.
- **get_page_links(link: str) -> list[str]**: Returns all hyperlinks (hrefs from &lt;a&gt; tags) found on the page.
- **get_meta_description(link: str) -> str**: Returns the content of the &lt;meta name="description"&gt; tag, if present.
- **get_h1_texts(link: str) -> list[str]**: Returns all text content from &lt;h1&gt; tags on the page.
- **get_images(link: str) -> list[str]**: Returns all image source URLs (src from &lt;img&gt; tags) found on the page.
- **get_text_content(link: str) -> str**: Returns the main visible text content of the page (&lt;body&gt; text).

All tools return all values found on the page. These utilities use Selenium and ChromeDriver under the hood.


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

> The above command only works if the Claude Desktop config is in *C:\Users\[username]\AppData\Roaming\Claude*.
> Otherwise we have to manually update the configuration. 
> If installed from the Microsoft Store, the path would be *C:\Users\[username]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude*


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
  },
  "preferences": {
    // Existing stuff...
  }
}
```

**VS Code Configuration:**

1. Enter `Ctrl + Shift + P`.
2. Search for and select `MCP: Add Server`.
3. Select `Command` and enter `uv run --with mcp[cli] mcp run C:\path\to\SelAgent\main.py`.


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
	},
	"inputs": []
}
```

---

- [Python MCP Github](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#installation)
