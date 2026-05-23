---
type: daily-note
status: active
domain: daily
domains:
  - daily
date: <% tp.date.now("YYYY-MM-DD") %>
created: "<% tp.date.now("YYYY-MM-DD") %>"
review_needed: false
---

# <% tp.date.now("dddd, MMMM D YYYY") %> 🗓️

> *[[<% tp.date.yesterday("YYYY-MM-DD", 0, tp.file.title, "YYYY-MM-DD") %>|← Yesterday]] | [[<% tp.date.tomorrow("YYYY-MM-DD", 0, tp.file.title, "YYYY-MM-DD") %>|Tomorrow →]]*

---

## Morning Intentions 🌅

**Today's #1 Priority:**
> 

**3 Things I'll Focus On:**
1. 
2. 
3. 

---

## Tasks — Due Today ✅

```tasks
not done
(due today) OR (scheduled today)
sort by priority
```

---

## Capture 📥

> Dump anything here. Process later.

- 

---

## Medicine 🩺

**Studied:**
- 

**Clinical pearls:**
- 

**OSCE notes:**
- 

---

## Money 💰

**Financial thoughts / actions:**
- 

---

## Body 💪

- Sleep quality: 
- Energy level: 
- Exercise: 

---

## Mind 🧠

**Reflection / observations:**
> 

---

## Needs Review 🔁

```dataview
TABLE type, status, file.link AS Note
FROM ""
WHERE review_needed = true
SORT file.mtime DESC
LIMIT 8
```

---

## End of Day ✨

**What went well:**
> 

**What I'll do differently:**
> 

**Gratitude:**
> 

---

*[[10_Maps_Of_Content/Life_OS_Home|← Life OS]] | [[10_Maps_Of_Content/Task_Dashboard|Task Dashboard →]]*
