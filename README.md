# SeriousSeran Obsidian Life OS

This vault is designed to feel like a calm personal command center, not a file dump.

It uses Obsidian as the interface, GitHub as the source of truth, Markdown as memory, Python as the processing layer, and safe GitHub Actions as scheduled maintenance.

## Start Here

- [[10_Maps_Of_Content/Life_OS_Home]]
- [[10_Maps_Of_Content/Task_Dashboard]]
- [[10_Maps_Of_Content/Life_OS_Command_Center.canvas]]
- [[99_System/Obsidian_Plugin_Setup]]
- [[99_System/LIFE_OS_SPEC]]

## Core Loop

Raw input -> processed insight -> linked notes -> tasks -> projects -> reviews -> direction.

## Commands

```bash
python 99_System/scripts/life_os.py inbox-report
python 99_System/scripts/life_os.py link-health
python 99_System/scripts/life_os.py root-triage
python 99_System/scripts/life_os.py create-daily-note
python 99_System/scripts/life_os.py create-weekly-review
python 99_System/scripts/life_os.py process-voice-dumps
python 99_System/scripts/life_os.py validate-notes
python 99_System/scripts/life_os.py refresh-dashboards
```

Enable the CSS snippet at `.obsidian/snippets/life-os.css` for the intended dashboard polish.

