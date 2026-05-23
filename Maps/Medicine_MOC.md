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

- [[Medicine/Medicine_Dashboard]]

## Key Folders

- [[Medicine]]
- [[Medicine/Topics]]
- [[Medicine/Clinical_Cases]]
- [[Medicine/OSCE/OSCE_Command_Center]]
- [[Medicine/Viva/Viva_Question_Bank]]
- [[Medicine/Topics/Clinical_Reasoning_Framework]]
- [[Medicine/Learning]]

## Important Notes

- [[Medicine/Medicine_Dashboard]]
- [[Medicine/Learning/Medicine_Learning_Library]]
- [[Medicine/OSCE/Cardiovascular_Examination_Station]]
- [[Medicine/Topics/Heart_Failure_Core]]
- [[System/schemas/medical_topic.schema]]
- [[System/schemas/clinical_case.schema]]

## Active Questions

- What topics need spaced review?
- What clinical patterns are weak?
- Which notes need deidentification review?

## Templates

- [[System/schemas/medical_topic.schema]]
- [[System/schemas/clinical_case.schema]]
- [[Templates/Medical_Topic_Template]]
- [[Templates/Clinical_Case_Template]]

## Reports

- [[System/reports/life_os_validation_report]]
- [[System/reports/link_health]]

## Review Rhythm

Review this MOC weekly and before exam-focused study blocks.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Medicine"
WHERE review_needed = true
SORT file.mtime DESC
```
