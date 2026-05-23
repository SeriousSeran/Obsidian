---
type: dashboard
domain: body
status: active
cssclasses:
  - life-os-dashboard
icon: "💪"
review_needed: false
---

# 💪 Body

> *"Take care of your body — it's the only place you have to live."* — Jim Rohn

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[Body/Body_Operating_System\|⚙️ Body OS]] | Sleep, energy, training system |
| [[Body/Learning/Body_Learning_Library\|📚 Learning Library]] | Health, fitness, nutrition resources |

---

> [!capture] Track Daily in Your Daily Note
> → **Sleep quality** · **Energy level** · **Exercise** · **Food**

---

## Open Tasks

```tasks
not done
path includes Body
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Body"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Body"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[Templates/Daily_Note_Template]]

## Learning Resources

- [[Body/Learning/Body_Learning_Library]]
- [[Maps/Learning_Resource_Hub]]

## Related Reports

- [[System/reports/life_os_validation_report]]

## Next Actions

- [ ] Add baseline body and energy notes.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-23T19:25:52+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
