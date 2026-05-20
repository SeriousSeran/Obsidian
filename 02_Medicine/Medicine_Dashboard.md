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
- [[02_Medicine/Kanban/Medicine_Study_Pipeline]]
- [[90_Templates/Medical_Topic_Template]]
- [[90_Templates/Clinical_Case_Template]]

## Key Folders

- [[02_Medicine/Topics]]
- [[02_Medicine/Clinical_Cases]]

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

## Related Reports

- [[99_System/reports/life_os_validation_report]]
- [[99_System/reports/link_health]]

## Next Actions

- [ ] Add first medical topic.
- [ ] Add first deidentified clinical case.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T04:35:19+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
