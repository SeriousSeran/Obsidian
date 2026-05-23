---
type: moc
domain: projects
status: active
review_needed: false
---
# Projects MOC

## Purpose

Track active projects, project decisions, next actions, and review status.

## Key Dashboard

- [[Projects/Project_Dashboards/Active_Project_Dashboard]]

## Key Folders

- [[Projects]]
- [[Projects/Active]]
- [[Projects/Project_Dashboards]]
- [[Projects/Learning]]

## Important Notes

- [[Projects/Project_Dashboards/Active_Project_Dashboard]]
- [[Projects/Active/Life_OS_Project]]
- [[Projects/Product_Idea_Lab]]
- [[Projects/Learning/Projects_Learning_Library]]
- [[System/schemas/project.schema]]

## Active Questions

- What is active now?
- What has a next action?
- What should be paused or archived?

## Templates

- [[System/schemas/project.schema]]
- [[Templates/Project_Template]]

## Reports

- [[System/reports/life_os_validation_report]]

## Review Rhythm

Review active projects weekly.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Projects"
WHERE review_needed = true
SORT file.mtime DESC
```
