---
type: report
status: active
review_needed: false
---
# QuickAdd Setup

## Choices

| Choice | Type | Target Folder | Filename Format | Template | Suggested Hotkey |
|---|---|---|---|---|---|
| Capture: Raw Idea | capture | `00_Inbox/Ideas` | `{{DATE}} {{VALUE}}` | none | Ctrl+Alt+I |
| Capture: Voice Dump Transcript | capture | `00_Inbox/Voice_Dumps` | `Voice Dump {{DATE}} {{TIME}}` | `90_Templates/Voice_Dump_Template.md` | Ctrl+Alt+V |
| Capture: Quick Task | capture | `00_Inbox` | `Quick Tasks` | none | Ctrl+Alt+T |
| Template: New Medical Topic | template | `02_Medicine/Topics` | `{{VALUE}}` | `90_Templates/Medical_Topic_Template.md` | none |
| Template: New Clinical Case | template | `02_Medicine/Clinical_Cases` | `Case {{DATE}} {{VALUE}}` | `90_Templates/Clinical_Case_Template.md` | none |
| Template: New Financial Idea | template | `03_Money/Business_Ideas` | `{{VALUE}}` | `90_Templates/Financial_Idea_Template.md` | none |
| Template: New Project | template | `07_Projects/Active` | `{{VALUE}}` | `90_Templates/Project_Template.md` | none |
| Template: New Content Idea | template | `06_Content/Ideas` | `{{VALUE}}` | `90_Templates/Content_Idea_Template.md` | none |
| Template: New Reflection | template | `04_Mind/Reflections` | `Reflection {{DATE}} {{TIME}}` | `90_Templates/Reflection_Template.md` | none |
| Template: New Book Note | template | `09_Bucket_List` | `Book - {{VALUE}}` | `90_Templates/Book_Note_Template.md` | none |
| Multi: Daily Capture Menu | multi | mixed | mixed | mixed | Ctrl+Alt+D |
| Multi: Life OS Command Menu | multi | mixed | mixed | mixed | Ctrl+Alt+O |

## Frontmatter

Use the standard properties in [[99_System/schemas/properties_schema]]. Capture notes should start raw, then become processed after review.

## Manual Setup

The proposed JSON in [[99_System/quickadd/quickadd_choices_proposed.json]] is a design reference. QuickAdd configuration can change between versions, so create the choices manually if import does not work.

