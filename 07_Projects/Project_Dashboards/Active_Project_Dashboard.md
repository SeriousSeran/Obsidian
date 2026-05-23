---
type: dashboard
domain: projects
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---

# 🔧 Projects

> *"A goal without a plan is just a wish."* — Antoine de Saint-Exupéry

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[07_Projects/Kanban/Life_OS_Roadmap\|🏗️ Life OS Roadmap]] | Visual board — Inbox → Next → In Progress → Done |
| [[07_Projects/Active/Life_OS_Project\|▶️ Life OS Project]] | Primary active build |
| [[07_Projects/Product_Idea_Lab\|💡 Product Idea Lab]] | Future income engines and product concepts |
| [[07_Projects/Learning/Projects_Learning_Library\|📚 Learning Library]] | Building, shipping, execution resources |

---

> [!goal] Current Priorities
> - Every active project must have a **next action** attached
> - Separate product *ideas* from active *commitments*
> - Review all active projects every Friday

---

## Open Tasks ✅

```tasks
not done
path includes 07_Projects
sort by due
```

---

## Active Projects

```dataview
TABLE status, next_action, file.mtime AS "Updated"
FROM "07_Projects/Active"
SORT file.mtime DESC
```

---

## Needs Review 🔁

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "07_Projects"
WHERE review_needed = true
SORT file.mtime DESC
```

---

## Recent Notes 📝

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "07_Projects"
SORT file.mtime DESC
LIMIT 15
```

---

## Related Templates

- [[90_Templates/Project_Template]]

## Learning Resources

- [[07_Projects/Learning/Projects_Learning_Library]]
- [[10_Maps_Of_Content/Learning_Resource_Hub]]

## System Reports

- [[99_System/reports/life_os_validation_report]]

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->

---

*[[10_Maps_Of_Content/Life_OS_Home|← Life OS Home]]*
