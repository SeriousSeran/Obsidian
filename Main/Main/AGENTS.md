# Agent Rules for the Obsidian Life OS Vault

This repository is a private Obsidian Life OS vault. Obsidian is the human interface, GitHub is the source of truth, Markdown is the memory layer, Python scripts are the processing layer, GitHub Actions are the safe automation layer, and Obsidian plugins make the system feel like an app.

## Core Rules

- Do not delete meaningful notes.
- Preserve raw source material, especially voice dumps, transcripts, screenshots, and original reflections.
- Archive uncertain files instead of deleting them.
- Use dry-run reports before risky moves, migrations, or rewrites.
- Prefer pull requests for generated changes.
- Do not publish, send messages, or expose private content.
- Do not transcribe audio automatically.
- Do not aggressively rewrite personal notes.
- Use Dataview, Tasks, Templater, QuickAdd, Kanban, and Homepage patterns when they improve usability.
- Keep all plugin-powered pages readable as plain Markdown.

## Safety Rules

- Patient notes must be deidentified.
- Medical notes are study material, not final clinical advice.
- Financial notes are planning material, not guaranteed outcomes.
- Reflection notes are personal context, not diagnoses.
- Medical, financial, and reflection notes should use `review_needed: true` when the content may affect real decisions.
- Any note containing patient, money, legal, or mental health stakes should be treated as sensitive by default.

## Folder Classification

- `00_Inbox/` is for raw capture and unprocessed input.
- `01_Daily/` is for daily notes, weekly reviews, monthly reviews, and quarterly reviews.
- `02_Medicine/` is for medical learning, topics, cases, OSCE, viva, and clinical study.
- `03_Money/` is for finance, business planning, commerce, assets, cash flow, and monetization.
- `04_Mind/` is for reflections, values, identity, decisions, and inner life.
- `05_Body/` is for health, physique, training, sleep, nutrition, and energy.
- `06_Content/` is for writing, publishing ideas, brand systems, scripts, and content backlog.
- `07_Projects/` is for active projects, project dashboards, product ideas, and execution tracking.
- `08_Relationships/` is for people notes and conversation patterns.
- `09_Bucket_List/` is for long-term goals and experiences.
- `10_Maps_Of_Content/` is the dashboard and navigation layer.
- `90_Templates/` is for reusable note templates.
- `99_System/` is for scripts, reports, schemas, plugin setup, design guidance, agent instructions, and migration records.

## Agent Workflow

1. Read this file before changing the vault.
2. Use `99_System/LIFE_OS_SPEC.md` as the system design reference.
3. Run validation and reports before broad changes.
4. Make generated changes in a branch and open a pull request.
5. Explain what changed and what needs human review.

## Plugin Assumptions

The vault supports Dataview, Tasks, Templater, QuickAdd, Periodic Notes, Calendar, Homepage, Minimal Theme, Style Settings, Omnisearch, Text Extractor, Kanban, and Obsidian Git. Do not install plugin binaries into the repository.

