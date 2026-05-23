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
| [[02_Medicine/Kanban/Medicine_Study_Pipeline\|📋 Study Pipeline]] | Visual board of all topics & OSCE stations |
| [[02_Medicine/OSCE/OSCE_Command_Center\|🏥 OSCE Command]] | Station tracking & exam readiness |
| [[02_Medicine/Viva/Viva_Question_Bank\|🎯 Viva Bank]] | High-yield Q&A for oral exams |
| [[02_Medicine/Topics/Clinical_Reasoning_Framework\|🔬 Clinical Reasoning]] | Framework for systematic thinking |
| [[02_Medicine/Learning/Medicine_Learning_Library\|📚 Learning Library]] | Books, courses, resources |

---

> [!viva] Current Priorities
> - Build high-yield topic notes (Templater → Medical Topic Template)
> - Practice one OSCE station per week
> - Link every topic to a viva question

---

## Open Tasks

```tasks
not done
path includes 02_Medicine
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "02_Medicine"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "02_Medicine"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[90_Templates/Medical_Topic_Template]]
- [[90_Templates/Clinical_Case_Template]]

## Learning Resources

- [[02_Medicine/Learning/Medicine_Learning_Library]]
- [[10_Maps_Of_Content/Learning_Resource_Hub]]

## Related Reports

- [[99_System/reports/life_os_validation_report]]
- [[99_System/reports/link_health]]

## Next Actions

- [ ] Add first medical topic.
- [ ] Add first deidentified clinical case.
- [ ] Practice one OSCE station.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
