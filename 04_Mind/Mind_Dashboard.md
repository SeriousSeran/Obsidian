---
type: dashboard
domain: mind
status: active
cssclasses:
  - life-os-dashboard
review_needed: true
---
# Mind Dashboard

## Start Here

- [[10_Maps_Of_Content/Mind_MOC]]
- [[90_Templates/Reflection_Template]]

## Key Folders

- [[04_Mind/Reflections]]

## Current Focus

- Preserve reflection without overinterpreting it.
- Notice patterns.
- Turn insight into kind next actions.

## Open Tasks

```tasks
not done
path includes 04_Mind
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "04_Mind"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "04_Mind"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[90_Templates/Reflection_Template]]

## Related Reports

- [[99_System/reports/voice_dump_processing_report]]

## Next Actions

- [ ] Process recent voice dumps.
- [ ] Choose one reflection to review gently.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T04:35:19+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
