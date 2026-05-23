---
type: dashboard
domain: mind
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---

# 🧠 Mind

> *"Know thyself."* — Socrates

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[Mind/Reflections/Pattern_Library\|🪞 Pattern Library]] | Recurring themes & personal patterns |
| [[Mind/Reflections/Decision_Journal\|📖 Decision Journal]] | Key decisions & outcomes |
| [[Mind/Learning/Mind_Learning_Library\|📚 Learning Library]] | Psychology, philosophy, mental models |

---

> [!review] Current Priorities
> - Preserve reflection without over-interpreting
> - Notice patterns, don't judge them
> - Turn insight into a kind next action

---

## Open Tasks

```tasks
not done
path includes Mind
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Mind"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Mind"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[Templates/Reflection_Template]]

## Learning Resources

- [[Mind/Learning/Mind_Learning_Library]]
- [[Maps/Learning_Resource_Hub]]

## Related Reports

- [[System/reports/voice_dump_processing_report]]

## Next Actions

- [ ] Process recent voice dumps.
- [ ] Choose one reflection to review gently.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
