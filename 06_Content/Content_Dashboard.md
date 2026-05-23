---
type: dashboard
domain: content
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---

# 📹 Content

> *"Teach what you know. Share what you learn."*

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[06_Content/Kanban/Content_Pipeline\|🏗️ Content Pipeline]] | Ideas → Outline → Script → Record → Publish |
| [[06_Content/Content_Operating_System\|⚙️ Content OS]] | Brand, voice, strategy |
| [[06_Content/Learning/Content_Learning_Library\|📚 Learning Library]] | Storytelling, editing, growth |

---

> [!study] Current Priorities
> - Capture ideas raw — process later
> - Shape one piece per week
> - Keep private content private

---

## Open Tasks

```tasks
not done
path includes 06_Content
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "06_Content"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "06_Content"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[90_Templates/Content_Idea_Template]]

## Learning Resources

- [[06_Content/Learning/Content_Learning_Library]]
- [[10_Maps_Of_Content/Learning_Resource_Hub]]

## Related Reports

- [[99_System/reports/inbox_report]]

## Next Actions

- [ ] Add first content idea.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
