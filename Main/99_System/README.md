# Life OS System README

This folder contains the processing layer, reports, schemas, plugin setup, design notes, and agent maintenance rules for the Obsidian Life OS.

## CLI

Run commands from the repository root:

```bash
python 99_System/scripts/life_os.py --help
python 99_System/scripts/life_os.py inbox-report
python 99_System/scripts/life_os.py link-health
python 99_System/scripts/life_os.py root-triage
python 99_System/scripts/life_os.py create-daily-note
python 99_System/scripts/life_os.py create-weekly-review
python 99_System/scripts/life_os.py process-voice-dumps
python 99_System/scripts/life_os.py validate-notes
python 99_System/scripts/life_os.py refresh-dashboards
```

## Reports

Reports are written to `99_System/reports/`. They are safe to regenerate and should be reviewed before broad changes.

## Dashboards

Start with [[10_Maps_Of_Content/Life_OS_Home]]. Plugin-powered dashboards use Dataview and Tasks, but they also include static links for graceful fallback.

## Learning Resources

The legal learning layer starts at [[10_Maps_Of_Content/Learning_Resource_Hub]]. It links to official/open resources and avoids pirated textbook mirrors. Policy: [[99_System/learning_resources/Legal_Resource_Policy]].

## Plugins

Setup docs live in:

- [[99_System/Obsidian_Plugin_Setup]]
- [[99_System/quickadd/QuickAdd_Setup]]
- [[99_System/periodic_notes/Periodic_Notes_Setup]]
- [[99_System/homepage/Homepage_Setup]]
- [[99_System/git/Obsidian_Git_Setup]]

## GitHub Actions

Workflows run daily maintenance, weekly maintenance, and validation. Generated changes open pull requests instead of silently rewriting `main`.

## Agent Use

Agents should read `AGENTS.md` and `99_System/LIFE_OS_SPEC.md` before changing files. Risky operations should start with dry-run reports.

## Safety Principles

Preserve raw input. Avoid publication. Use review gates. Mark medical, financial, and reflection material with `review_needed: true` when real decisions may be affected.

