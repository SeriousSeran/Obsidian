---
type: dashboard
domain: bucket-list
domains:
  - bucket-list
status: active
review_needed: false
cssclasses:
  - life-os-dashboard
---
icon: "🌍"

# 🌍 Bucket List

> *"Life is either a daring adventure or nothing at all."* — Helen Keller

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[Bucket_List/Experiences/Experience_Index\|✨ Experience Index]] | All experiences — places, skills, people, work, body |

---

## Experience Areas

| Area | Examples |
|---|---|
| 🌏 Places | Countries, cities, hidden nature spots |
| 🎸 Skills | Music, languages, sport, crafts |
| 🤝 People | Trips, gifts, shared memories |
| 🔨 Work | Projects, products, things you taught |
| 💪 Body | Strength goals, endurance, health milestones |

---

> [!goal] How to use this
> - Add one experience you still genuinely care about
> - Attach one **tiny next action** to it so it's not just a dream
> - Review once a month — cross one off or get closer to one

---

## Active Dreams ✨

```dataview
TABLE status, next_action, file.mtime AS "Updated"
FROM "Bucket_List"
WHERE file.name != "Bucket_List_Dashboard"
SORT file.mtime DESC
LIMIT 30
```

---

*[[Maps/Life_OS_Home|← Life OS Home]]*
