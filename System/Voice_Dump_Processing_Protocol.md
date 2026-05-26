---
type: protocol
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
icon: "🎙️"
---

# 🎙️ Voice Dump Processing Protocol

> **Who reads this:** Claudian (me). Every time Seran says "process my voice dump" or "process my latest dump".

---

## The 7-Step Protocol

When Seran drops a voice dump in `Inbox/Voice_Dumps/`, Claudian runs this exact sequence:

---

### Step 1 — Read the raw dump

```
Read the most recent file in Inbox/Voice_Dumps/ that has status: raw
```

Pull out:
- **Domain(s)**: Which life area? Medicine / Money / Mind / Body / Content / Projects
- **Core insight**: What's the one-liner takeaway?
- **Concepts**: List every distinct idea, fact, or question mentioned
- **Questions Seran asked out loud**: These become flashcards
- **Tangents**: Things mentioned in passing that are worth exploring

---

### Step 2 — Classify & Route

| If content is... | Route to |
|---|---|
| Medical fact / clinical | `Medicine/Topics/[Topic].md` |
| Exam prep / OSCE | `Medicine/OSCE/` or `Medicine/Viva/` |
| Financial idea / money thought | `Money/Business_Ideas/` |
| Personal reflection / philosophy | `Mind/Reflections/` |
| Workout / health / sleep | `Body/` |
| Content idea (video / article) | `Content/Ideas/` |
| Project plan / idea | `Projects/Active/` |
| Multiple domains | Create separate notes for each |

---

### Step 3 — Create domain notes

For each major concept, either:
- **Link to existing note** if it already exists in the vault
- **Create new note** using `Templates/Medical_Topic_Template.md` (medicine) or appropriate template

Each new note should have:
- Proper YAML frontmatter (domain, tags, `review_needed: true`)
- The specific insight or knowledge from this dump
- `#flashcards` tag if it's medical

---

### Step 4 — Generate Flashcards

For every medical concept or fact mentioned:
```
**[Question about concept] ::** [Answer]
```

Rules:
- One card per discrete fact
- Questions should be what an examiner would ask
- Keep answers under 2 lines
- Include at least 3 cards per medical topic

---

### Step 5 — Build "Explore Further" (the explore map)

Look at what Seran studied and ask:
> *"What would a curious medical student naturally wonder next?"*

Generate 3–5 rabbit holes:
1. **Related condition** — "Since you studied X, you should also know Y because..."
2. **Deeper mechanism** — "The pathophysiology of X connects to Z which explains..."
3. **Clinical application** — "In OSCE this comes up as... try reading..."
4. **Exam angle** — "Viva question: how does X relate to [common exam scenario]"
5. **Cross-domain link** — "This connects to your Money/Mind/Body domain because..."

---

### Step 6 — Create Processed Note

Use `Templates/Processed_Voice_Dump_Template.md`:
- Fill in all sections from steps 3–5
- Add flashcards in the `#flashcards` section
- Set Tasks with due dates (+1 day review SR cards, +3 days explore #1, +7 days explore #2)
- Save to appropriate domain folder (NOT Inbox)

---

### Step 7 — Update the source voice dump

Mark the original voice dump as processed:
```yaml
status: processed
processed_into: [[path/to/processed/note]]
tags:
  - voice-dump
  - processed
```

Remove `unprocessed` tag. Add link to the processed note.

---

## Claudian's Rules for Voice Processing

1. **Never skip the explore section** — this is the most valuable part
2. **Minimum 3 flashcards** for any medical dump
3. **Don't over-clean** — preserve Seran's actual words in the "Full Notes" section
4. **Create wikilinks** to existing vault notes whenever possible
5. **Due dates on tasks** — always set concrete review dates, not "someday"
6. **Cross-domain thinking** — medicine can connect to Mind (stress physiology), Body (exercise medicine), Money (healthcare costs)

---

## Quick Trigger Phrases

Seran can say any of these to start processing:

| Phrase | Action |
|---|---|
| "Process my voice dump" | Run full 7-step protocol on latest raw dump |
| "Process all voice dumps" | Run protocol on ALL files with `status: raw` |
| "What did I study recently?" | Summarise last 5 processed dumps |
| "Make flashcards from my dump" | Skip to Step 4 on the latest dump |
| "What should I explore next?" | Run Step 5 on the latest processed note |

---

## Voice Dump Inbox View

```dataview
TABLE status, domain, created AS "Date", file.mtime AS "Updated"
FROM "Inbox/Voice_Dumps"
WHERE file.name != ".gitkeep"
SORT created DESC
```

---

*[[Maps/Home|← Home]] | [[Inbox|Inbox →]] | [[System/Agent_Client_Index|Agent Client →]]*
