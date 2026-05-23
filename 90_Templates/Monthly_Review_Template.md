---
type: monthly-review
status: active
domain: daily
domains:
  - review
month: <% tp.date.now("YYYY-MM") %>
created: "<% tp.date.now("YYYY-MM-DD") %>"
review_needed: false
---

# Monthly Review — <% tp.date.now("MMMM YYYY") %> 📅

---

## Notes Created This Month 📝

```dataview
TABLE type, domains, status, file.mtime AS "Modified"
FROM ""
WHERE file.mtime >= date(this.created) - dur(30 days)
AND type != "monthly-review"
SORT file.mtime DESC
```

---

## Completed Tasks ✅

```tasks
done after <% tp.date.now("YYYY-MM-DD", -30) %>
sort by done
```

---

## What Moved Forward 🚀

> Projects, areas, goals that made real progress.

- 

---

## What Stalled 🧱

> What got stuck, avoided, or didn't move?

- 

---

## Medicine Progress 🩺

**Topics mastered:**
- 

**OSCE stations practiced:**
- 

**Weak areas to target next month:**
- 

---

## Projects Review 🔧

```dataview
TABLE status, file.mtime AS "Last Updated"
FROM "07_Projects"
WHERE type = "project"
SORT file.mtime DESC
```

---

## Money & Finance 💰

**Income this month:**
> 

**Key financial moves:**
- 

---

## Health of the System 🛠️

> Is the vault working for you? What's clunky? What's missing?

- 

---

## Direction Changes 🧭

> Did anything shift in your goals or priorities?

> 

---

## Top 3 Wins 🏆

1. 
2. 
3. 

---

## Next Month — Top Priorities 🎯

1. 
2. 
3. 

---

*[[01_Daily/Monthly_Reviews|← All Monthly Reviews]] | [[10_Maps_Of_Content/Life_OS_Home|Life OS →]]*
