---
type: moc
domain: relationships
domains:
  - relationships
status: active
review_needed: true
---
# People Index

> A respectful index for relationship context and follow-ups.

## Use This For

- People you genuinely want to remember
- Follow-ups
- Shared interests
- Conversation notes
- Boundaries and care

## Do Not Use This For

- Judging people
- Recording private information without purpose
- Diagnosing relationship dynamics

## People

```dataview
TABLE status, review, file.mtime AS "Updated"
FROM "08_Relationships/People"
WHERE file.name != "People_Index"
SORT file.name ASC
```
