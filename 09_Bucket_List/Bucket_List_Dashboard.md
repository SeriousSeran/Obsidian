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
# Bucket List Dashboard

> Long-range experiences, skills, places, and quests worth making real.

## Experience Areas

- [[09_Bucket_List/Experiences/Experience_Index]]

| Area | Examples |
|---|---|
| Places | Countries, cities, nature |
| Skills | Music, languages, sport, craft |
| People | Trips, gifts, shared memories |
| Work | Projects, products, teaching |
| Body | Strength, endurance, health milestones |

## Active Dreams

```dataview
TABLE status, next_action, review, file.mtime AS "Updated"
FROM "09_Bucket_List"
WHERE file.name != "Bucket_List_Dashboard"
SORT file.mtime DESC
LIMIT 30
```

## Next Actions

- [ ] Add one experience you still care about.
- [ ] Attach one tiny next action to it.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T06:17:35+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
