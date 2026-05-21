---
type: dashboard
domain: relationships
domains:
  - relationships
status: active
review_needed: true
cssclasses:
  - life-os-dashboard
---
# Relationship Dashboard

> A quiet place to remember people, patterns, and conversations with care.

## Start Here

- [[08_Relationships/People/People_Index]]
- [[90_Templates/Person_Note_Template]]

## Current Focus

- Remember important context.
- Track follow-ups without making people into tasks.
- Reflect on conversation patterns gently.

## Open Tasks

```tasks
not done
path includes 08_Relationships
sort by due
```

## People Notes

```dataview
TABLE status, review, file.mtime AS "Updated"
FROM "08_Relationships/People"
SORT file.mtime DESC
LIMIT 20
```

## Next Actions

- [ ] Create important person notes only when useful.
- [ ] Add follow-ups from daily notes.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
