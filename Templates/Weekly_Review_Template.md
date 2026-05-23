---
type: weekly-review
status: active
domain: daily
domains:
  - review
week: <% tp.date.now("YYYY-[W]WW") %>
created: "<% tp.date.now("YYYY-MM-DD") %>"
review_needed: false
---

# Weekly Review — <% tp.date.now("YYYY-[W]WW") %> 📋

> *Week of <% tp.date.now("MMMM D") %> → <% tp.date.now("MMMM D", 6) %>*

---

## Notes Created This Week 📝

```dataview
TABLE type, domains, status, file.mtime AS "Modified"
FROM ""
WHERE file.mtime >= date(this.created) - dur(7 days)
AND type != "weekly-review"
SORT file.mtime DESC
```

---

## Open Tasks 📌

```tasks
not done
sort by due
limit 30
```

---

## Completed This Week ✅

```tasks
done after <% tp.date.now("YYYY-MM-DD", -7) %>
sort by done
```

---

## Wins 🏆

> What went really well this week?

1. 
2. 
3. 

---

## Open Loops 🔄

> What's unfinished, incomplete, or lingering?

- 

---

## Medicine Progress 🩺

**Topics studied:**
- 

**OSCE practice:**
- 

**Cases reviewed:**
- 

**Weak areas:**
- 

---

## Projects Progress 🔧

```dataview
TABLE status, domains, file.mtime AS "Last Updated"
FROM "Projects"
WHERE type = "project"
SORT file.mtime DESC
```

---

## Money Review 💰

**Income / spending notes:**
- 

**Business ideas progressed:**
- 

---

## Content Progress 📹

```dataview
TABLE status, file.mtime AS "Updated"
FROM "Content"
SORT file.mtime DESC
LIMIT 5
```

---

## Mind & Body 🧠💪

**Energy this week:** 
**Sleep quality:** 
**Exercise:** 
**Key reflection:**
> 

---

## Direction Check 🧭

> Am I moving toward my goals? What's pulling me off track?

**Biggest threat to momentum:**
> 

**Biggest opportunity:**
> 

---

## Next Week — Top 3 Priorities 🎯

1. 
2. 
3. 

---

*[[Daily/Weekly_Reviews|← All Weekly Reviews]] | [[Maps/Life_OS_Home|Life OS →]]*
