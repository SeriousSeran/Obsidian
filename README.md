# SeriousSeran Obsidian Life OS

This vault is designed to feel like a calm personal command center, not a file dump.

It uses Obsidian as the interface, GitHub as the source of truth, Markdown as memory, Python as the processing layer, and safe GitHub Actions as scheduled maintenance.

## Start Here

- [[Maps/Life_OS_Home]]
- [[Maps/Task_Dashboard]]
- [[Maps/Learning_Resource_Hub]]
- [[Maps/Life_OS_Command_Center.canvas]]
- [[System/Obsidian_Plugin_Setup]]
- [[System/LIFE_OS_SPEC]]
- [[System/Repo_Inventory]]

## Core Loop

Raw input -> processed insight -> linked notes -> tasks -> projects -> reviews -> direction.

## Commands

```bash
python System/scripts/life_os.py inbox-report
python System/scripts/life_os.py link-health
python System/scripts/life_os.py root-triage
python System/scripts/life_os.py create-daily-note
python System/scripts/life_os.py create-weekly-review
python System/scripts/life_os.py process-voice-dumps
python System/scripts/life_os.py validate-notes
python System/scripts/life_os.py refresh-dashboards
```

Enable the CSS snippet at `.obsidian/snippets/life-os.css` for the intended dashboard polish.

Learning resources use official, open, library, or publisher links only. See [[System/learning_resources/Legal_Resource_Policy]].

The repo boundary is documented in [[System/Repo_Inventory]] so the vault stays clean and only contains the Life OS base plus active vault content.

