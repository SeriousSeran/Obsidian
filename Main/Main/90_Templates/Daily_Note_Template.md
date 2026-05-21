---
type: daily-note
status: active
domain: daily
domains:
  - daily
date: {{date}}
created: "{{date}}"
review_needed: false
---
# {{date}}

> Daily capture, direction, and close-down.

## Capture

## Priorities

## Actions

- [ ] 

## Medicine

## Money

## Body

## Notes Needing Review

```dataview
TABLE type, status, file.link AS Note
FROM ""
WHERE review_needed = true
SORT file.mtime DESC
LIMIT 10
```

## End of Day Review
