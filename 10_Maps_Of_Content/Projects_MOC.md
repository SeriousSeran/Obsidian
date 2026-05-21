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

- [[07_Projects/Project_Dashboards/Active_Project_Dashboard]]

## Key Folders

- [[07_Projects]]
- [[07_Projects/Active]]
- [[07_Projects/Project_Dashboards]]
- [[07_Projects/Learning]]

## Important Notes

- [[07_Projects/Project_Dashboards/Active_Project_Dashboard]]
- [[07_Projects/Active/Life_OS_Project]]
- [[07_Projects/Product_Idea_Lab]]
- [[07_Projects/Learning/Projects_Learning_Library]]
- [[99_System/schemas/project.schema]]

## Active Questions

- What is active now?
- What has a next action?
- What should be paused or archived?

## Templates

- [[99_System/schemas/project.schema]]
- [[90_Templates/Project_Template]]

## Reports

- [[99_System/reports/life_os_validation_report]]

## Review Rhythm

Review active projects weekly.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "07_Projects"
WHERE review_needed = true
SORT file.mtime DESC
```
