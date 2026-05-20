---
type: moc
domain: body
status: active
review_needed: false
---
# Body MOC

## Purpose

Track health, physique, energy, sleep, training, and routines.

## Key Dashboard

- [[05_Body/Body_Dashboard]]

## Key Folders

- [[05_Body]]
- [[05_Body/Learning]]

## Important Notes

- [[05_Body/Body_Dashboard]]
- [[05_Body/Learning/Body_Learning_Library]]

## Active Questions

- What improves energy this week?
- What habits are measurable?
- What should be discussed with a qualified professional?

## Templates

- [[90_Templates/Daily_Note_Template]]

## Reports

- [[99_System/reports/life_os_validation_report]]

## Review Rhythm

Review weekly alongside the weekly review.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "05_Body"
WHERE review_needed = true
SORT file.mtime DESC
```
