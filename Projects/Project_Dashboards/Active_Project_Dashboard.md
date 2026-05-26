---
type: dashboard
domain: projects
status: active
cssclasses:
  - life-os-dashboard
icon: "🔧"
review_needed: false
---

# 🔧 Projects

> *"A goal without a plan is just a wish."* — Antoine de Saint-Exupéry

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[Projects/Kanban/Life_OS_Roadmap\|🏗️ Life OS Roadmap]] | Visual board — Inbox → Next → In Progress → Done |
| [[Projects/Active/Life_OS_Project\|▶️ Life OS Project]] | Primary active build |
| [[Projects/Product_Idea_Lab\|💡 Product Idea Lab]] | Future income engines and product concepts |
| [[Projects/Learning/Projects_Learning_Library\|📚 Learning Library]] | Building, shipping, execution resources |

---

> [!goal] Current Priorities
> - Every active project must have a **next action** attached
> - Separate product *ideas* from active *commitments*
> - Review all active projects every Friday

---

## Open Tasks ✅

```tasks
not done
path includes Projects
sort by due
```

---

## Active Projects

```dataview
TABLE status, next_action, file.mtime AS "Updated"
FROM "Projects/Active"
SORT file.mtime DESC
```

---

## Needs Review 🔁

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Projects"
WHERE review_needed = true
SORT file.mtime DESC
```

---

## Recent Notes 📝

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Projects"
SORT file.mtime DESC
LIMIT 15
```

---

## Related Templates

- [[Templates/Project_Template]]

## Learning Resources

- [[Projects/Learning/Projects_Learning_Library]]
- [[Maps/Learning_Resource_Hub]]

## System Reports

- [[System/reports/life_os_validation_report]]

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-26T19:09:45+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->

---

*[[Maps/Life_OS_Home|← Life OS Home]]*
