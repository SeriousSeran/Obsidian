---
type: dashboard
domain: projects
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---
# Active Project Dashboard

## Start Here

- [[10_Maps_Of_Content/Projects_MOC]]
- [[07_Projects/Active/Life_OS_Project]]
- [[07_Projects/Product_Idea_Lab]]
- [[07_Projects/Learning/Projects_Learning_Library]]
- [[07_Projects/Kanban/Life_OS_Roadmap]]
- [[90_Templates/Project_Template]]

## Key Folders

- [[07_Projects/Active]]
- [[07_Projects/Project_Dashboards]]
- [[07_Projects/Learning]]

## Current Focus

- Keep every active project tied to a next action.
- Separate product ideas from active commitments.
- Review active projects weekly.

## Open Tasks

```tasks
not done
path includes 07_Projects
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "07_Projects"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "07_Projects"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[90_Templates/Project_Template]]

## Learning Resources

- [[07_Projects/Learning/Projects_Learning_Library]]
- [[10_Maps_Of_Content/Learning_Resource_Hub]]

## Related Reports

- [[99_System/reports/life_os_validation_report]]

## Next Actions

- [ ] Define the first active project.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T06:17:35+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
