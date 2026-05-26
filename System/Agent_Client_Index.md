---
type: index
status: active
cssclasses:
  - life-os-dashboard
icon: "🤖"
---

# 🤖 Agent Client — AI Conversation Hub

> *Chat with Claudian (Claude Code), Gemini CLI, or Codex directly inside Obsidian.*

---

## How to Start a Chat

1. Open the **Agent Client** panel (ribbon icon or `Ctrl+P` → "Agent Client: Open Chat")
2. Select agent: **Claude Code** (default), Gemini CLI, or Codex
3. Chat is auto-context-aware — it reads your active note

---

## Agents Available

| Agent | ID | Best For |
|---|---|---|
| 🟣 **Claude Code (Claudian)** | `claude-code-acp` | Vault management, writing, analysis |
| 🔵 **Gemini CLI** | `gemini-cli` | Research, long-context, multimodal |
| 🟠 **Codex** | `codex-acp` | Code generation, technical tasks |

---

## Exported Sessions

> Auto-saved sessions from the Agent Client appear below.

```dataview
TABLE file.ctime AS "Date", file.size AS "Size"
FROM "Agent Client"
WHERE type != "index"
SORT file.ctime DESC
LIMIT 20
```

---

## Tips

- **Auto-mention note**: Your currently open note is automatically sent as context
- **Export**: Use the export button in Agent Client to save sessions here
- **Android bridge**: Type `!vault [instruction]` to send updates from any Claude session → drop the text in [[Inbox]] for processing

---

*[[Maps/Home|← Home]] | [[System/Obsidian_Plugin_Setup|Plugin Setup →]]*
