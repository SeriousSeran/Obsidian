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

- [[Mind/Mind_Dashboard]]

## Key Folders

- [[Mind]]
- [[Mind/Reflections]]
- [[Mind/Learning]]
- [[Mind/Reflections/Pattern_Library]]
- [[Mind/Reflections/Decision_Journal]]

## Important Notes

- [[Mind/Mind_Dashboard]]
- [[Mind/Learning/Mind_Learning_Library]]
- [[System/schemas/reflection.schema]]

## Active Questions

- What patterns keep repeating?
- What needs kindness before optimization?
- What decisions need more distance?

## Templates

- [[System/schemas/reflection.schema]]
- [[Templates/Reflection_Template]]

## Reports

- [[System/reports/life_os_validation_report]]

## Review Rhythm

Review lightly each week and deeply only when useful.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Mind"
WHERE review_needed = true
SORT file.mtime DESC
```
