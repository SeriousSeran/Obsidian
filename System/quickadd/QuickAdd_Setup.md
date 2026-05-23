---
type: report
status: active
review_needed: false
---
# QuickAdd Setup

## Choices

| Choice | Type | Target Folder | Filename Format | Template | Suggested Hotkey |
|---|---|---|---|---|---|
| Capture: Raw Idea | capture | `Inbox/Ideas` | `{{DATE}} {{VALUE}}` | none | Ctrl+Alt+I |
| Capture: Voice Dump Transcript | capture | `Inbox/Voice_Dumps` | `Voice Dump {{DATE}} {{TIME}}` | `Templates/Voice_Dump_Template.md` | Ctrl+Alt+V |
| Capture: Quick Task | capture | `Inbox` | `Quick Tasks` | none | Ctrl+Alt+T |
| Template: New Medical Topic | template | `Medicine/Topics` | `{{VALUE}}` | `Templates/Medical_Topic_Template.md` | none |
| Template: New Clinical Case | template | `Medicine/Clinical_Cases` | `Case {{DATE}} {{VALUE}}` | `Templates/Clinical_Case_Template.md` | none |
| Template: New Financial Idea | template | `Money/Business_Ideas` | `{{VALUE}}` | `Templates/Financial_Idea_Template.md` | none |
| Template: New Project | template | `Projects/Active` | `{{VALUE}}` | `Templates/Project_Template.md` | none |
| Template: New Content Idea | template | `Content/Ideas` | `{{VALUE}}` | `Templates/Content_Idea_Template.md` | none |
| Template: New Reflection | template | `Mind/Reflections` | `Reflection {{DATE}} {{TIME}}` | `Templates/Reflection_Template.md` | none |
| Template: New Book Note | template | `Bucket_List` | `Book - {{VALUE}}` | `Templates/Book_Note_Template.md` | none |
| Multi: Daily Capture Menu | multi | mixed | mixed | mixed | Ctrl+Alt+D |
| Multi: Life OS Command Menu | multi | mixed | mixed | mixed | Ctrl+Alt+O |

## Frontmatter

Use the standard properties in [[System/schemas/properties_schema]]. Capture notes should start raw, then become processed after review.

## Manual Setup

The proposed JSON in [[System/quickadd/quickadd_choices_proposed.json]] is a design reference. QuickAdd configuration can change between versions, so create the choices manually if import does not work.

