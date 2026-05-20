---
type: dashboard
domain: money
status: active
cssclasses:
  - life-os-dashboard
review_needed: true
---
# Money Dashboard

## Start Here

- [[10_Maps_Of_Content/Money_MOC]]
- [[90_Templates/Financial_Idea_Template]]

## Key Folders

- [[03_Money/Financial_Map]]
- [[03_Money/Business_Ideas]]

## Current Focus

- Stabilize cash flow.
- Separate assumptions from evidence.
- Track business experiments.

## Open Tasks

```tasks
not done
path includes 03_Money
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "03_Money"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "03_Money"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[90_Templates/Financial_Idea_Template]]

## Related Reports

- [[99_System/reports/life_os_validation_report]]

## Next Actions

- [ ] Create a current cash flow note.
- [ ] List active business experiments.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T04:35:19+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
