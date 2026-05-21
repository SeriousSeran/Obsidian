---
type: dashboard
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---
# Life OS

> A calm command center for capture, learning, projects, money, content, reflection, and direction.

## Start Here

- [[01_Daily/Daily_Notes|Daily Notes]]
- [[00_Inbox|Inbox]]
- [[10_Maps_Of_Content/Task_Dashboard|Task Dashboard]]
- [[07_Projects/Project_Dashboards/Active_Project_Dashboard|Active Projects]]
- [[10_Maps_Of_Content/Learning_Resource_Hub|Learning Resource Hub]]
- [[99_System/reports/inbox_report|Inbox Report]]
- [[99_System/reports/life_os_validation_report|System Health]]
- [[10_Maps_Of_Content/Life_OS_Command_Center.canvas|Canvas Command Center]]

## Command Centers

| Domain | Dashboard | Purpose |
|---|---|---|
| Medicine | [[02_Medicine/Medicine_Dashboard]] | Clinical learning, OSCE, cases |
| Money | [[03_Money/Money_Dashboard]] | Stability, income, assets |
| Mind | [[04_Mind/Mind_Dashboard]] | Reflection and personal patterns |
| Body | [[05_Body/Body_Dashboard]] | Sleep, energy, health |
| Content | [[06_Content/Content_Dashboard]] | Scripts, brand, publishing |
| Projects | [[07_Projects/Project_Dashboards/Active_Project_Dashboard]] | Active builds and product ideas |

## Learning Libraries

| Domain | Library |
|---|---|
| Medicine | [[02_Medicine/Learning/Medicine_Learning_Library]] |
| Money | [[03_Money/Learning/Money_Learning_Library]] |
| Mind | [[04_Mind/Learning/Mind_Learning_Library]] |
| Body | [[05_Body/Learning/Body_Learning_Library]] |
| Content | [[06_Content/Learning/Content_Learning_Library]] |
| Projects | [[07_Projects/Learning/Projects_Learning_Library]] |

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

- [[01_Daily/Weekly_Reviews|Weekly Reviews]]
- [[01_Daily/Monthly_Reviews|Monthly Reviews]]
- [[01_Daily/Quarterly_Reviews|Quarterly Reviews]]

## System Reports

- [[99_System/reports/inbox_report]]
- [[99_System/reports/link_health]]
- [[99_System/reports/root_triage_report]]
- [[99_System/reports/voice_dump_processing_report]]
- [[99_System/reports/life_os_validation_report]]
- [[99_System/reports/dashboard_refresh_report]]

## Current Quests

- Become a clinically excellent doctor.
- Build a durable AI-assisted Life OS.
- Build financial stability and future income engines.
- Turn knowledge into teaching, content, and products.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T05:08:12+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
