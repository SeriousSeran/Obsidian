---
type: dashboard
status: active
cssclasses:
  - life-os-dashboard
icon: "🗺️"
review_needed: false
---

# 🏠 Life OS

> *"The secret of getting ahead is getting started."* — Mark Twain

---

## Command Centers 🗺️

| Domain | Dashboard | Kanban |
|---|---|---|
| 🩺 Medicine | [[Medicine/Medicine_Dashboard\|Medicine]] | [[Medicine/Kanban/Medicine_Study_Pipeline\|Study Pipeline]] |
| 💰 Money | [[Money/Money_Dashboard\|Money]] | — |
| 🧠 Mind | [[Mind/Mind_Dashboard\|Mind]] | — |
| 💪 Body | [[Body/Body_Dashboard\|Body]] | — |
| 📹 Content | [[Content/Content_Dashboard\|Content]] | [[Content/Kanban/Content_Pipeline\|Content Pipeline]] |
| 🔧 Projects | [[Projects/Project_Dashboards/Active_Project_Dashboard\|Projects]] | [[Projects/Kanban/Life_OS_Roadmap\|Roadmap]] |
| 🤝 Relationships | [[Relationships/Relationship_Dashboard\|Relationships]] | — |
| 🌍 Bucket List | [[Bucket_List/Bucket_List_Dashboard\|Bucket List]] | — |

---

> [!capture] A calm command center

## Start Here

- [[Daily/Daily_Notes|Daily Notes]]
- [[Inbox|Inbox]]
- [[Maps/Task_Dashboard|Task Dashboard]]
- [[Projects/Project_Dashboards/Active_Project_Dashboard|Active Projects]]
- [[Maps/Learning_Resource_Hub|Learning Resource Hub]]
- [[System/reports/inbox_report|Inbox Report]]
- [[System/reports/life_os_validation_report|System Health]]
- [[Maps/Life_OS_Command_Center.canvas|Canvas Command Center]]

## Command Centers

| Domain | Dashboard | Purpose |
|---|---|---|
| Medicine | [[Medicine/Medicine_Dashboard]] | Clinical learning, OSCE, cases |
| Money | [[Money/Money_Dashboard]] | Stability, income, assets |
| Mind | [[Mind/Mind_Dashboard]] | Reflection and personal patterns |
| Body | [[Body/Body_Dashboard]] | Sleep, energy, health |
| Content | [[Content/Content_Dashboard]] | Scripts, brand, publishing |
| Projects | [[Projects/Project_Dashboards/Active_Project_Dashboard]] | Active builds and product ideas |
| Relationships | [[Relationships/Relationship_Dashboard]] | People, follow-ups, conversation patterns |
| Bucket List | [[Bucket_List/Bucket_List_Dashboard]] | Long-term experiences and quests |

## Learning Libraries

| Domain | Library |
|---|---|
| Medicine | [[Medicine/Learning/Medicine_Learning_Library]] |
| Money | [[Money/Learning/Money_Learning_Library]] |
| Mind | [[Mind/Learning/Mind_Learning_Library]] |
| Body | [[Body/Learning/Body_Learning_Library]] |
| Content | [[Content/Learning/Content_Learning_Library]] |
| Projects | [[Projects/Learning/Projects_Learning_Library]] |

## Base Systems

- [[Medicine/OSCE/OSCE_Command_Center]]
- [[Medicine/Viva/Viva_Question_Bank]]
- [[Medicine/Topics/Clinical_Reasoning_Framework]]
- [[Money/Financial_Map/Financial_Command_Center]]
- [[Money/Business_Ideas/Business_Model_Lab]]
- [[Mind/Reflections/Pattern_Library]]
- [[Body/Body_Operating_System]]
- [[Content/Content_Operating_System]]
- [[Projects/Active/Life_OS_Project]]
- [[Projects/Product_Idea_Lab]]
- [[Relationships/Relationship_Dashboard]]
- [[Bucket_List/Bucket_List_Dashboard]]

## Live Review Queue

```dataview
TABLE type, status, domains, file.mtime AS "Updated"
FROM ""
WHERE review_needed = true
SORT file.mtime DESC
LIMIT 25
```

## Today's Open Loops

```tasks
not done
sort by due
limit 25
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM ""
SORT file.mtime DESC
LIMIT 20
```

## Reviews

- [[Daily/Weekly_Reviews|Weekly Reviews]]
- [[Daily/Monthly_Reviews|Monthly Reviews]]
- [[Daily/Quarterly_Reviews|Quarterly Reviews]]

## System Reports

- [[System/reports/inbox_report]]
- [[System/reports/link_health]]
- [[System/reports/root_triage_report]]
- [[System/reports/voice_dump_processing_report]]
- [[System/reports/life_os_validation_report]]
- [[System/reports/dashboard_refresh_report]]

## Current Quests

- Become a clinically excellent doctor.
- Build a durable AI-assisted Life OS.
- Build financial stability and future income engines.
- Turn knowledge into teaching, content, and products.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
