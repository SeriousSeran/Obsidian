---
type: moc
domain: medicine
status: active
review_needed: false
---
# Medicine MOC

## Purpose

Turn medical learning into reviewable concepts, clinical cases, OSCE practice, and viva readiness.

## Key Dashboard

- [[02_Medicine/Medicine_Dashboard]]

## Key Folders

- [[02_Medicine]]
- [[02_Medicine/Topics]]
- [[02_Medicine/Clinical_Cases]]

## Important Notes

- [[02_Medicine/Medicine_Dashboard]]
- [[99_System/schemas/medical_topic.schema]]
- [[99_System/schemas/clinical_case.schema]]

## Active Questions

- What topics need spaced review?
- What clinical patterns are weak?
- Which notes need deidentification review?

## Templates

- [[99_System/schemas/medical_topic.schema]]
- [[99_System/schemas/clinical_case.schema]]

## Reports

- [[99_System/reports/life_os_validation_report]]
- [[99_System/reports/link_health]]

## Review Rhythm

Review this MOC weekly and before exam-focused study blocks.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "02_Medicine"
WHERE review_needed = true
SORT file.mtime DESC
```
