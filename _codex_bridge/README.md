# Codex Bridge

This folder is a local file bridge between Obsidian and Codex.

## Workflow

1. In Obsidian, run `Codex Bridge: Export active note context` or `Create Codex request from active note`.
2. In Codex, read files from this folder and write Markdown replies into `replies/`.
3. In Obsidian, run `Append latest bridge reply to active note` or `Create note from latest bridge reply`.

No network API token is stored by this plugin for local bridge workflows.
