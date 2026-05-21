---
type: moc
domain: content
status: active
review_needed: false
---
# Content MOC

## Purpose

Turn ideas into useful writing, scripts, posts, and publishing experiments.

## Key Dashboard

- [[06_Content/Content_Dashboard]]

## Key Folders

- [[06_Content]]
- [[06_Content/Ideas]]
- [[06_Content/Learning]]

## Important Notes

- [[06_Content/Content_Dashboard]]
- [[06_Content/Content_Operating_System]]
- [[06_Content/Learning/Content_Learning_Library]]
- [[99_System/schemas/content_idea.schema]]

## Active Questions

- What audience is this for?
- What should be shipped this week?
- Which ideas are strongest after review?

## Templates

- [[99_System/schemas/content_idea.schema]]
- [[90_Templates/Content_Idea_Template]]

## Reports

- [[99_System/reports/inbox_report]]

## Review Rhythm

Review weekly and before publishing sessions.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "06_Content"
WHERE review_needed = true
SORT file.mtime DESC
```
