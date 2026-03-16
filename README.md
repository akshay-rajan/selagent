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

*claude_desktop_config.json*
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
  },
  // Existing stuff...
  "preferences": {
    "menuBarEnabled": false,
    "coworkScheduledTasksEnabled": false,
    "ccdScheduledTasksEnabled": false,
    "coworkWebSearchEnabled": true,
    "sidebarMode": "chat"
  }
}
```

---

- [Python MCP Github](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#installation)
