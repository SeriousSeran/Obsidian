---
type: dashboard
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---
# Learning Resource Hub

> Legal books, official references, and learning paths for the Life OS.

## Rule

Use official, open, library, or publisher links. Do not add pirated textbook mirrors or Anna's Archive links.

## Domain Libraries

| Domain | Library | Use |
|---|---|---|
| Medicine | [[Medicine/Learning/Medicine_Learning_Library]] | Clinical learning, OSCE, cases |
| Money | [[Money/Learning/Money_Learning_Library]] | Finance, investing, business models |
| Mind | [[Mind/Learning/Mind_Learning_Library]] | Reflection, cognition, behaviour |
| Body | [[Body/Learning/Body_Learning_Library]] | Sleep, energy, movement, habits |
| Content | [[Content/Learning/Content_Learning_Library]] | Writing, publishing, audience |
| Projects | [[Projects/Learning/Projects_Learning_Library]] | Startup, product, positioning |

## How to Use a Resource

1. Capture the source in a domain learning note.
2. Extract only your own short summary, questions, and next actions.
3. Link useful ideas to projects, daily notes, or reviews.
4. Mark anything medical, financial, or reflective as `review_needed: true` when it could affect a real decision.

## Live Learning Notes

```dataview
TABLE domain, status, source, file.mtime AS "Updated"
FROM ""
WHERE contains(type, "learning") OR contains(file.path, "/Learning/")
SORT file.mtime DESC
LIMIT 25
```

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
