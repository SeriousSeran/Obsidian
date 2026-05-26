---
type: dashboard
domain: content
status: active
cssclasses:
  - life-os-dashboard
icon: "📹"
review_needed: false
---

# 📹 Content

> *"Teach what you know. Share what you learn."*

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[Content/Kanban/Content_Pipeline\|🏗️ Content Pipeline]] | Ideas → Outline → Script → Record → Publish |
| [[Content/Content_Operating_System\|⚙️ Content OS]] | Brand, voice, strategy |
| [[Content/Learning/Content_Learning_Library\|📚 Learning Library]] | Storytelling, editing, growth |

---

> [!study] Current Priorities
> - Capture ideas raw — process later
> - Shape one piece per week
> - Keep private content private

---

## Open Tasks

```tasks
not done
path includes Content
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Content"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Content"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[Templates/Content_Idea_Template]]

## Learning Resources

- [[Content/Learning/Content_Learning_Library]]
- [[Maps/Learning_Resource_Hub]]

## Related Reports

- [[System/reports/inbox_report]]

## Next Actions

- [ ] Add first content idea.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-26T19:09:45+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
