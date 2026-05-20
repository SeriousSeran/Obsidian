---
type: moc
domain: money
status: active
review_needed: false
---
# Money MOC

## Purpose

Track money, cash flow, assets, business ideas, experiments, and financial assumptions.

## Key Dashboard

- [[03_Money/Money_Dashboard]]

## Key Folders

- [[03_Money]]
- [[03_Money/Financial_Map]]
- [[03_Money/Business_Ideas]]

## Important Notes

- [[03_Money/Money_Dashboard]]
- [[99_System/schemas/financial_idea.schema]]

## Active Questions

- What improves cash stability?
- What assumptions need testing?
- Which ideas are experiments, not beliefs?

## Templates

- [[99_System/schemas/financial_idea.schema]]

## Reports

- [[99_System/reports/life_os_validation_report]]

## Review Rhythm

Review weekly for cash flow and monthly for strategy.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "03_Money"
WHERE review_needed = true
SORT file.mtime DESC
```
