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

- [[Content/Content_Dashboard]]

## Key Folders

- [[Content]]
- [[Content/Ideas]]
- [[Content/Learning]]

## Important Notes

- [[Content/Content_Dashboard]]
- [[Content/Content_Operating_System]]
- [[Content/Learning/Content_Learning_Library]]
- [[System/schemas/content_idea.schema]]

## Active Questions

- What audience is this for?
- What should be shipped this week?
- Which ideas are strongest after review?

## Templates

- [[System/schemas/content_idea.schema]]
- [[Templates/Content_Idea_Template]]

## Reports

- [[System/reports/inbox_report]]

## Review Rhythm

Review weekly and before publishing sessions.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Content"
WHERE review_needed = true
SORT file.mtime DESC
```
