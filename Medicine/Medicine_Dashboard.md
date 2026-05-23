---
type: dashboard
domain: medicine
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---

# 🩺 Medicine

> *"Medicine is a science of uncertainty and an art of probability."* — William Osler

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[Medicine/Kanban/Medicine_Study_Pipeline\|📋 Study Pipeline]] | Visual board of all topics & OSCE stations |
| [[Medicine/OSCE/OSCE_Command_Center\|🏥 OSCE Command]] | Station tracking & exam readiness |
| [[Medicine/Viva/Viva_Question_Bank\|🎯 Viva Bank]] | High-yield Q&A for oral exams |
| [[Medicine/Topics/Clinical_Reasoning_Framework\|🔬 Clinical Reasoning]] | Framework for systematic thinking |
| [[Medicine/Learning/Medicine_Learning_Library\|📚 Learning Library]] | Books, courses, resources |

---

> [!viva] Current Priorities
> - Build high-yield topic notes (Templater → Medical Topic Template)
> - Practice one OSCE station per week
> - Link every topic to a viva question

---

## Open Tasks

```tasks
not done
path includes Medicine
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Medicine"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Medicine"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[Templates/Medical_Topic_Template]]
- [[Templates/Clinical_Case_Template]]

## Learning Resources

- [[Medicine/Learning/Medicine_Learning_Library]]
- [[Maps/Learning_Resource_Hub]]

## Related Reports

- [[System/reports/life_os_validation_report]]
- [[System/reports/link_health]]

## Next Actions

- [ ] Add first medical topic.
- [ ] Add first deidentified clinical case.
- [ ] Practice one OSCE station.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
