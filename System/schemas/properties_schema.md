# Properties Schema

## Standard Properties

| Property | Meaning |
|---|---|
| `type` | Note kind used by Dataview, templates, and scripts |
| `status` | Current lifecycle state |
| `domain` | Primary domain |
| `domains` | Multiple related domains |
| `review_needed` | Whether a human should review before relying on it |
| `created` | Creation date |
| `updated` | Last meaningful update date |
| `source` | Raw source or originating note |
| `next_action` | Next concrete action |
| `review` | Review date or cadence |
| `due` | Due date for Tasks |
| `scheduled` | Scheduled date for Tasks |
| `risk` | Risk level or risk note |
| `platform` | Content platform |
| `audience` | Intended audience |
| `topic` | Topic label |
| `system` | Medical/body/system category |
| `patient_deidentified` | Whether clinical material is deidentified |
| `needs_transcription` | Whether audio needs transcription |
| `cssclasses` | Obsidian CSS classes |

## Allowed Types

- `voice-dump`
- `processed-voice-dump`
- `daily-note`
- `weekly-review`
- `monthly-review`
- `quarterly-review`
- `medical-topic`
- `clinical-case`
- `financial-idea`
- `project`
- `content-idea`
- `reflection`
- `book-note`
- `person-note`
- `learning-library`
- `dashboard`
- `moc`
- `report`
- `template`

## Allowed Statuses

- `raw`
- `draft`
- `active`
- `processed`
- `review-needed`
- `archived`
- `completed`
- `someday`
- `waiting`
- `blocked`

## Use

Templates and scripts should prefer these properties so Dataview dashboards stay reliable.

