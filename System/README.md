# Life OS System README

This folder contains the processing layer, reports, schemas, plugin setup, design notes, and agent maintenance rules for the Obsidian Life OS.

## CLI

Run commands from the repository root:

```bash
python System/scripts/life_os.py --help
python System/scripts/life_os.py inbox-report
python System/scripts/life_os.py link-health
python System/scripts/life_os.py root-triage
python System/scripts/life_os.py create-daily-note
python System/scripts/life_os.py create-weekly-review
python System/scripts/life_os.py process-voice-dumps
python System/scripts/life_os.py validate-notes
python System/scripts/life_os.py refresh-dashboards
```

## Reports

Reports are written to `System/reports/`. They are safe to regenerate and should be reviewed before broad changes.

## Dashboards

Start with [[Maps/Life_OS_Home]]. Plugin-powered dashboards use Dataview and Tasks, but they also include static links for graceful fallback.

## Learning Resources

The legal learning layer starts at [[Maps/Learning_Resource_Hub]]. It links to official/open resources and avoids pirated textbook mirrors. Policy: [[System/learning_resources/Legal_Resource_Policy]].

## Repo Boundary

Use [[System/Repo_Inventory]] to keep the repository clean. The root should contain the Life OS vault folders, GitHub/Obsidian config, `README.md`, and `AGENTS.md` only.

## Plugins

Setup docs live in:

- [[System/Obsidian_Plugin_Setup]]
- [[System/quickadd/QuickAdd_Setup]]
- [[System/periodic_notes/Periodic_Notes_Setup]]
- [[System/homepage/Homepage_Setup]]
- [[System/git/Obsidian_Git_Setup]]

## GitHub Actions

Workflows run daily maintenance, weekly maintenance, and validation. Generated changes open pull requests instead of silently rewriting `main`.

## Agent Use

Agents should read `AGENTS.md` and `System/LIFE_OS_SPEC.md` before changing files. Risky operations should start with dry-run reports.

## Safety Principles

Preserve raw input. Avoid publication. Use review gates. Mark medical, financial, and reflection material with `review_needed: true` when real decisions may be affected.

