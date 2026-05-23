# Life OS Specification

## Purpose

The Life OS turns raw life input into structured memory and reviewable action. It supports capture, processing, classification, linking, reviews, projects, medical learning, money planning, content creation, reflection, body tracking, relationships, long-term direction, and system health.

## System Layers

- Obsidian: visual interface for reading, writing, linking, search, graph, canvas, and review.
- GitHub: source of truth, history, branches, pull requests, and review gates.
- Markdown: memory layer for notes, templates, dashboards, reports, and Kanban boards.
- Python: processing layer for reports, validation, triage, voice dump skeletons, and dashboard refreshes.
- GitHub Actions: scheduled automation layer.
- Codex and Jules: agent worker layer for safe drafting and maintenance.
- Obsidian plugins: live dashboards, task queries, fast capture, periodic reviews, search, visual boards, and Git sync.

## Folder Architecture

- `Inbox/`: raw capture.
- `Daily/`: daily notes and periodic reviews.
- `Medicine/`: clinical learning, OSCE, viva, and deidentified cases.
- `Money/`: finance, business, assets, liabilities, and income ideas.
- `Mind/`: reflections and personal patterns without diagnosis.
- `Body/`: sleep, energy, health, habits, and routines.
- `Content/`: scripts, content ideas, brand systems, and publishing backlog.
- `Projects/`: active projects, product ideas, and project dashboards.
- `Relationships/`: people notes and conversation patterns.
- `Bucket_List/`: long-term goals and experiences.
- `Maps/`: dashboards and command centers.
- `Templates/`: reusable templates.
- `System/`: scripts, reports, schemas, plugin setup, design guidance, and agent rules.

## Capture Pipeline

Raw inputs enter `Inbox/` through QuickAdd, manual capture, voice dump transcripts, screenshots, or imported files. Capture should be fast and low-friction.

## Voice Dump Pipeline

Voice dumps are preserved as raw source. Audio files receive companion Markdown notes marked `needs_transcription: true`. Markdown transcripts can be turned into processed skeleton notes that link back to the raw transcript.

## Processing Pipeline

Processing extracts:

- core insight
- action items
- related domains
- possible projects
- links to existing notes
- review flags

Automation drafts structure. Humans review meaning.

## Review Pipeline

Daily notes hold immediate capture and priorities. Weekly reviews collect patterns and open loops. Monthly and quarterly reviews connect actions to direction.

## Domain Systems

Medicine, Money, Mind, Body, Content, Projects, Relationships, and Bucket List each get a home, a review rhythm, and a clear place in the command center.

## Plugin Layer

- Dataview: live review queues and recent-note tables.
- Tasks: open loops, due dates, and domain task dashboards.
- Templater: optional template intelligence while keeping templates plain-text friendly.
- QuickAdd: capture and creation menus.
- Periodic Notes and Calendar: daily, weekly, monthly, and quarterly review rhythm.
- Homepage: opens the command center.
- Kanban: visual pipelines for projects, content, and medicine.
- Omnisearch and Text Extractor: retrieval and OCR support.
- Obsidian Git: sync and local history.
- Minimal Theme and Style Settings: calm visual system.

## Automation Layer

Automation is safe by default. Reports can be generated directly. Meaningful content changes should be proposed through pull requests. Moving, archiving, and renaming require `--apply`.

## Agent Rules

Agents must follow `AGENTS.md`, preserve raw source material, avoid private exposure, and mark high-stakes content for review.

## Safety Model

The system may organize, report, validate, and draft. It may not diagnose, publish, send messages, delete meaningful notes, or make final medical or financial decisions.

## Roadmap

1. Keep capture reliable.
2. Maintain dashboards and review queues.
3. Add a local or web control panel.
4. Improve voice workflows.
5. Add richer project and review intelligence.

