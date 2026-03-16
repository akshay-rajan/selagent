# SelAgent

## Prerequisites

- [UV Package Manager](https://docs.astral.sh/uv/#installation)

## Setting Up

```sh
# Initialize a new UV (an alternative to 'pip') project
uv init .
```

```sh
# Install the MCP CLI
uv add "mcp[cli]"
```

```sh
# Automatically update the Claude Desktop configuration
uv run mcp install main.py
```

> The above command only works if the Claude Desktop config is in *C:\Users\[username]\AppData\Roaming\Claude*.
> Otherwise we have to manually update the configuration. 
> If installed from the Microsoft Store, the path would be *C:\Users\[username]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude*

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
