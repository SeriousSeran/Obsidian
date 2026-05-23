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

- [[Money/Money_Dashboard]]

## Key Folders

- [[Money]]
- [[Money/Financial_Map]]
- [[Money/Business_Ideas]]
- [[Money/Learning]]
- [[Money/Financial_Map/Financial_Command_Center]]
- [[Money/Business_Ideas/Business_Model_Lab]]

## Important Notes

- [[Money/Money_Dashboard]]
- [[Money/Learning/Money_Learning_Library]]
- [[System/schemas/financial_idea.schema]]

## Active Questions

- What improves cash stability?
- What assumptions need testing?
- Which ideas are experiments, not beliefs?

## Templates

- [[System/schemas/financial_idea.schema]]
- [[Templates/Financial_Idea_Template]]

## Reports

- [[System/reports/life_os_validation_report]]

## Review Rhythm

Review weekly for cash flow and monthly for strategy.

## Notes Needing Review

```dataview
TABLE type, status, file.mtime AS "Updated"
FROM "Money"
WHERE review_needed = true
SORT file.mtime DESC
```
