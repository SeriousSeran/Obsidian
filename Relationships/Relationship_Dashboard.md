---
type: dashboard
domain: relationships
domains:
  - relationships
status: active
review_needed: false
cssclasses:
  - life-os-dashboard
---
icon: "🤝"

# 🤝 Relationships

> *"You are the average of the five people you spend the most time with."* — Jim Rohn

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[Relationships/People/People_Index\|👥 People Index]] | All person notes — context, patterns, follow-ups |
| [[Templates/Person_Note_Template\|📋 Person Template]] | Create a new person note |

---

> [!pearl] How to use this domain
> - Remember important context about people you care about
> - Track follow-ups **without** turning people into tasks
> - Reflect on conversation patterns gently — no judgement

---

## Open Follow-ups ✅

```tasks
not done
path includes Relationships
sort by due
```

---

## People Notes 👥

```dataview
TABLE status, review, file.mtime AS "Updated"
FROM "Relationships/People"
SORT file.mtime DESC
LIMIT 20
```

---

## Recent Notes 📝

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Relationships"
SORT file.mtime DESC
LIMIT 10
```

---

*[[Maps/Life_OS_Home|← Life OS Home]]*

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-24T15:43:45+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
