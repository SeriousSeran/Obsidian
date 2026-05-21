---
type: dashboard
domain: medicine
status: active
cssclasses:
  - life-os-dashboard
review_needed: true
---
# Medicine Dashboard

## Start Here

- [[10_Maps_Of_Content/Medicine_MOC]]
- [[02_Medicine/Learning/Medicine_Learning_Library]]
- [[02_Medicine/OSCE/OSCE_Command_Center]]
- [[02_Medicine/Viva/Viva_Question_Bank]]
- [[02_Medicine/Topics/Clinical_Reasoning_Framework]]
- [[02_Medicine/Kanban/Medicine_Study_Pipeline]]
- [[90_Templates/Medical_Topic_Template]]
- [[90_Templates/Clinical_Case_Template]]

## Key Folders

- [[02_Medicine/Topics]]
- [[02_Medicine/Clinical_Cases]]
- [[02_Medicine/OSCE]]
- [[02_Medicine/Viva]]
- [[02_Medicine/Learning]]

## Current Focus

- Build high-yield concepts.
- Keep cases deidentified.
- Connect OSCE and viva learning to questions.

## Open Tasks

```tasks
not done
path includes 02_Medicine
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "02_Medicine"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "02_Medicine"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[90_Templates/Medical_Topic_Template]]
- [[90_Templates/Clinical_Case_Template]]

## Learning Resources

- [[02_Medicine/Learning/Medicine_Learning_Library]]
- [[10_Maps_Of_Content/Learning_Resource_Hub]]

## Related Reports

- [[99_System/reports/life_os_validation_report]]
- [[99_System/reports/link_health]]

## Next Actions

- [ ] Add first medical topic.
- [ ] Add first deidentified clinical case.
- [ ] Practice one OSCE station.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T06:17:35+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
