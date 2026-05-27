---
type: dashboard
domain: money
status: active
cssclasses:
  - life-os-dashboard
icon: "💰"
review_needed: false
---

# 💰 Money

> *"Do not save what is left after spending; spend what is left after saving."* — Warren Buffett

---

## Command 🗺️

| Hub | Purpose |
|---|---|
| [[Money/Financial_Map/Financial_Command_Center\|📊 Financial Command]] | Cash flow, assets, liabilities |
| [[Money/Business_Ideas/Business_Model_Lab\|💡 Business Lab]] | Ideas, experiments, income engines |
| [[Money/Learning/Money_Learning_Library\|📚 Learning Library]] | Finance books & resources |

---

> [!goal] Current Priorities
> - Stabilize cash flow — facts, not guesses
> - Track one active business experiment
> - Separate income streams clearly

---

## Open Tasks

```tasks
not done
path includes Money
sort by due
```

## Needs Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Money"
WHERE review_needed = true
SORT file.mtime DESC
```

## Recent Notes

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Money"
SORT file.mtime DESC
LIMIT 15
```

## Related Templates

- [[Templates/Financial_Idea_Template]]

## Learning Resources

- [[Money/Learning/Money_Learning_Library]]
- [[Maps/Learning_Resource_Hub]]

## Related Reports

- [[System/reports/life_os_validation_report]]

## Next Actions

- [ ] Create a current cash flow note.
- [ ] List active business experiments.
- [ ] Fill the financial command center with facts, not guesses.

<!-- life-os-generated:start -->
## Generated System Snapshot

- Last refresh: 2026-05-27T19:28:59+05:30
- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]
<!-- life-os-generated:end -->
