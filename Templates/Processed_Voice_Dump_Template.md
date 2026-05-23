---
type: processed-voice-dump
status: processed
domain: "<% tp.file.cursor() %>"
domains:
  - "<% tp.file.cursor() %>"
source: voice-dump
source_note: ""
created: "<% tp.date.now("YYYY-MM-DD") %>"
review_needed: true
tags:
  - voice-dump
  - processed
icon: "✨"
---

# ✨ <% tp.file.title %>

> **Processed from:** `[[Inbox/Voice_Dumps/SOURCE_NOTE]]`  
> **Domain:** [medicine / money / mind / body / content]  
> **Date spoken:** <% tp.date.now("D MMM YYYY") %>

---

## 💡 Core Insight (1–2 sentences)

> The single most important thing Seran said in this dump.

---

## 🧠 Key Concepts Extracted

| Concept | Domain | Status |
|---|---|---|
| | | New / Revisiting |
| | | |

---

## 📋 Full Notes (cleaned)

> Structured version of the raw transcript. Remove filler words; keep meaning.

---

## 📇 Flashcards
#flashcards

> SR cards auto-extracted from this session. Review in Spaced Repetition ribbon (📇).

**[Concept 1] ::** 

**[Concept 2] ::** 

**[Concept 3] ::** 

---

## 🔭 Explore Further

> These are the rabbit holes this dump opened. Click one next time you study.

1. **[[]]** — Why: 
2. **[[]]** — Why: 
3. **[[]]** — Why: 

**Related existing notes:**
```dataview
LIST
FROM ""
WHERE contains(domains, this.domain)
AND file.name != this.file.name
SORT file.mtime DESC
LIMIT 5
```

---

## 🔗 Linked Notes Created

> Notes Claudian created from this dump.

- [[]]
- [[]]

---

## ✅ Action Items

- [ ] Review flashcards in SR deck 📅 <% tp.date.now("YYYY-MM-DD", 1) %>
- [ ] Read "Explore Further" #1 📅 <% tp.date.now("YYYY-MM-DD", 3) %>
- [ ] Read "Explore Further" #2 📅 <% tp.date.now("YYYY-MM-DD", 7) %>

---

*[[Inbox|← Inbox]] | [[Medicine/Medicine_Dashboard|Medicine →]] | [[Dashboard/Home|Home →]]*
