---
type: homepage
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---

# Welcome Back, Seran ☀️

> *Your calm command center. Capture → Think → Build → Review.*

---

## Quick Capture ⚡

> Use **QuickAdd** (`Ctrl+Alt+D`) to instantly log ideas, tasks, voice dumps, or new notes.

| Capture | Shortcut | Target |
|---|---|---|
| Raw Idea | `Ctrl+Alt+I` | `00_Inbox/Ideas` |
| Voice Dump | `Ctrl+Alt+V` | `00_Inbox/Voice_Dumps` |
| Quick Task | `Ctrl+Alt+T` | `00_Inbox` |
| Full Menu | `Ctrl+Alt+O` | Life OS Menu |

---

## Today's Focus 🎯

```tasks
not done
(due today) OR (scheduled today)
sort by priority
```

---

## Command Centers 🗺️

| Domain | Hub | Kanban | Status |
|---|---|---|---|
| 🩺 Medicine | [[02_Medicine/Medicine_Dashboard]] | [[02_Medicine/Kanban/Medicine_Study_Pipeline]] | Active |
| 💰 Money | [[03_Money/Money_Dashboard]] | — | Active |
| 🧠 Mind | [[04_Mind/Mind_Dashboard]] | — | Active |
| 💪 Body | [[05_Body/Body_Dashboard]] | — | Active |
| 📹 Content | [[06_Content/Content_Dashboard]] | [[06_Content/Kanban/Content_Pipeline]] | Active |
| 🔧 Projects | [[07_Projects/Project_Dashboards/Active_Project_Dashboard]] | [[07_Projects/Kanban/Life_OS_Roadmap]] | Active |
| 🤝 People | [[08_Relationships/Relationship_Dashboard]] | — | Active |
| 🌍 Bucket List | [[09_Bucket_List/Bucket_List_Dashboard]] | — | Active |

---

## Inbox — Needs Processing 📥

```dataview
TABLE file.mtime AS "Captured", type
FROM "00_Inbox"
WHERE file.name != ".gitkeep"
SORT file.mtime DESC
LIMIT 15
```

---

## Review Queue 🔁

```dataview
TABLE type, status, domains, file.mtime AS "Updated"
FROM ""
WHERE review_needed = true
SORT file.mtime DESC
LIMIT 10
```

---

## Overdue & Upcoming Tasks ⏰

```tasks
not done
due before in 3 days
sort by due
limit 20
```

---

## Recent Notes 📝

```dataview
TABLE type, status, file.mtime AS "Last Edited"
FROM ""
WHERE file.name != "Home"
SORT file.mtime DESC
LIMIT 12
```

---

## Navigation 🧭

- [[10_Maps_Of_Content/Life_OS_Home|Life OS Home]] — Full system map
- [[10_Maps_Of_Content/Task_Dashboard|Task Dashboard]] — All tasks by domain
- [[10_Maps_Of_Content/Learning_Resource_Hub|Learning Hub]] — Books, courses, resources
- [[01_Daily/Daily_Notes|Daily Notes]] — All past days
- [[01_Daily/Weekly_Reviews|Weekly Reviews]] — Weekly reflections
- [[90_Templates|Templates]] — All Templater templates
- [[99_System/Obsidian_Plugin_Setup|Plugin Setup Guide]] — Plugin reference

---

## System Health 🛠️

- [[99_System/reports/life_os_validation_report|Validation Report]]
- [[99_System/reports/inbox_report|Inbox Report]]
- [[99_System/reports/link_health|Link Health]]
- [[99_System/reports/root_triage_report|Root Triage]]
