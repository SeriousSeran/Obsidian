---
type: dashboard
domain: content
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---
# Content Dashboard

## Start Here

- [[10_Maps_Of_Content/Content_MOC]]
- [[06_Content/Content_Operating_System]]
- [[06_Content/Learning/Content_Learning_Library]]
- [[06_Content/Kanban/Content_Pipeline]]
- [[90_Templates/Content_Idea_Template]]

## Key Folders

- [[06_Content/Ideas]]
- [[06_Content/Learning]]

## Current Focus

- Capture ideas.
- Shape useful pieces.
- Keep private content private.

## Open Tasks

```tasks
not done
path includes 06_Content
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "06_Content"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "06_Content"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[90_Templates/Content_Idea_Template]]

## Learning Resources

- [[06_Content/Learning/Content_Learning_Library]]
- [[10_Maps_Of_Content/Learning_Resource_Hub]]

## Related Reports

- [[99_System/reports/inbox_report]]

## Next Actions

- [ ] Add first content idea.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T06:14:59+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
