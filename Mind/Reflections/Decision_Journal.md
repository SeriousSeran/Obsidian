---
type: reflection
domain: mind
domains:
  - mind
status: active
review_needed: true
---
# Decision Journal

> Capture decisions before outcomes distort the memory.

## Decision Template

| Field | Notes |
|---|---|
| Decision |  |
| Date |  |
| Options |  |
| Why this option |  |
| Main uncertainty |  |
| Reversal point |  |
| Review date |  |

## Open Decisions

```dataview
TABLE status, next_action, review, file.mtime AS "Updated"
FROM "Mind"
WHERE contains(file.name, "Decision") OR type = "reflection"
SORT file.mtime DESC
LIMIT 20
```
