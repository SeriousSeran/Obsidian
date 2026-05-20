---
type: moc
domain: mind
status: active
review_needed: false
---
# Mind MOC

## Purpose

Hold reflections, decisions, values, emotional patterns, and personal meaning without turning them into diagnosis.

## Key Dashboard

- [[04_Mind/Mind_Dashboard]]

## Key Folders

- [[04_Mind]]
- [[04_Mind/Reflections]]

## Important Notes

- [[04_Mind/Mind_Dashboard]]
- [[99_System/schemas/reflection.schema]]

## Active Questions

- What patterns keep repeating?
- What needs kindness before optimization?
- What decisions need more distance?

## Templates

- [[99_System/schemas/reflection.schema]]

## Reports

- [[99_System/reports/life_os_validation_report]]

## Review Rhythm

Review lightly each week and deeply only when useful.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "04_Mind"
WHERE review_needed = true
SORT file.mtime DESC
```
