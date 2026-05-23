---
type: dashboard
domain: body
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
---

# 💪 Body

> *"Take care of your body — it's the only place you have to live."* — Jim Rohn

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[05_Body/Body_Operating_System\|⚙️ Body OS]] | Sleep, energy, training system |
| [[05_Body/Learning/Body_Learning_Library\|📚 Learning Library]] | Health, fitness, nutrition resources |

---

> [!capture] Track Daily in Your Daily Note
> → **Sleep quality** · **Energy level** · **Exercise** · **Food**

---

## Open Tasks

```tasks
not done
path includes 05_Body
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "05_Body"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "05_Body"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[90_Templates/Daily_Note_Template]]

## Learning Resources

- [[05_Body/Learning/Body_Learning_Library]]
- [[10_Maps_Of_Content/Learning_Resource_Hub]]

## Related Reports

- [[99_System/reports/life_os_validation_report]]

## Next Actions

- [ ] Add baseline body and energy notes.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-21T20:38:48+05:30
- Reports: [[99_System/reports/life_os_validation_report|Validation]], [[99_System/reports/link_health|Link Health]], [[99_System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
