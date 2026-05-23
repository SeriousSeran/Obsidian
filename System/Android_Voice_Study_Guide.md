---
type: guide
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
icon: "📱"
---

# 📱 Android Voice Study Guide

> **The complete path**: You read aloud → vault captures it → Claudian processes it → you get notes + flashcards + explore map.

---

## 🗺️ The Pipeline at a Glance

```
📱 You read aloud (Android)
       ↓
🤖 ChatGPT transcribes
       ↓
📥 Paste into Obsidian Mobile → Inbox/Voice_Dumps/
       ↓
🖥️ Open desktop + say "Process my voice dump"
       ↓
🧠 Claudian creates: domain notes + flashcards + explore paths
       ↓
📇 SR deck has new cards → review tomorrow
       ↓
🔭 Explore Further list → next study session rabbit holes
```

---

## 📲 Step-by-Step: On Your Android Phone

### Method A — ChatGPT Voice (Recommended)

1. Open **ChatGPT** on Android
2. Tap the 🎤 voice button (or hold mic icon)
3. Read your notes / textbook / lecture aloud — speak naturally
4. ChatGPT transcribes as you talk
5. When done, type: **"Clean up this transcript — fix grammar, keep all medical terms exact"**
6. Copy the cleaned text

**Then choose how to get it into the vault:**

---

### 📂 Getting it into the Vault

#### Option 1 — Obsidian Mobile (Best)
> Install Obsidian on Android, sync via iCloud/Git

1. Open Obsidian Mobile
2. Press `+` → new note
3. Title: `Voice Dump YYYY-MM-DD` (e.g., `Voice Dump 2026-05-23`)
4. Save to folder: **`Inbox/Voice_Dumps/`**
5. Paste transcript under `## Raw Transcript`
6. Tag domain (medicine / mind / etc.)
7. Done — syncs automatically

#### Option 2 — GitHub Mobile (No Obsidian needed)
1. Open **GitHub** app on Android
2. Go to `SeriousSeran/Obsidian`
3. Navigate to `Inbox/Voice_Dumps/`
4. Tap `+` (top right) → "Create new file"
5. Filename: `Voice Dump YYYY-MM-DD.md`
6. Paste this header:
```
---
type: voice-dump
status: raw
domain: medicine
tags: [voice-dump, unprocessed]
---
# Voice Dump YYYY-MM-DD

## Raw Transcript

[PASTE YOUR TEXT HERE]
```
7. Tap "Commit new file"

#### Option 3 — Send to Claude (This Chat)
1. Open **Claude** on Android (claude.ai)
2. Paste your transcript
3. Say: **"Store this as a voice dump and process it into my vault"**
4. Claude will respond with the processed content
5. On desktop, create the note manually from Claude's output

---

## 🖥️ Back on Desktop — Trigger Claudian

When you're back at your desk, open the **Agent Client panel** in Obsidian (ribbon 🤖) or this terminal and say:

> **"Process my voice dump"**

Claudian runs the [[System/Voice_Dump_Processing_Protocol|7-step protocol]] and creates:
- ✅ Clean domain note in the right folder
- 📇 Flashcards in SR deck  
- 🔭 "Explore Further" list (3-5 rabbit holes)
- ✅ Tasks with due dates (review tomorrow, explore in 3 days, deep dive in 7 days)

---

## 📇 Flashcard Integration

After processing, your SR deck automatically has new cards. To review:
- Click the **📇 ribbon icon** in Obsidian
- Or: `Ctrl+P` → "SR: Study Flashcards"
- Cards due: shown in status bar at the bottom

**SR tells you**: "Again / Hard / Good / Easy" — answer honestly, it schedules the next review.

---

## 🔭 The Explore Further System

Every processed dump generates **3–5 rabbit holes** like:

> *"You talked about ACE inhibitors — explore next: (1) ARBs and the difference, (2) how RAAS connects to heart failure, (3) renal protection in diabetes, (4) OSCE: managing hypertensive emergency"*

These become **Tasks with due dates** so you don't lose them:
```
- [ ] Explore: ARBs vs ACE inhibitors 📅 2026-05-26
- [ ] Explore: RAAS in heart failure 📅 2026-05-30
```

They appear on your **daily note** → **home dashboard** → SR queue.

---

## ⏰ Reminder Loop

| When | What happens |
|---|---|
| Day of dump | Process → notes + cards created |
| Day +1 | SR: review new flashcards |
| Day +3 | Task: explore rabbit hole #1 |
| Day +7 | Task: explore rabbit hole #2 |
| Weekly Review | All processed dumps summarised |

---

## 💡 Tips for Reading Aloud

- **Read slowly** — pause between concepts so transcription catches it
- **Say key terms clearly**: "ACE inhibitor... angiotensin converting enzyme"
- **Narrate what you're thinking**: "I'm not sure why X happens — I need to look up Y"
- **Include questions**: "Wait, does this mean Z?" — these become great flashcards
- **No need to be perfect** — Claudian cleans it up

---

## 📥 Current Voice Dump Queue

```dataview
TABLE status, domain, created AS "Date"
FROM "Inbox/Voice_Dumps"
WHERE file.name != ".gitkeep"
SORT created DESC
LIMIT 10
```

---

*[[Dashboard/Home|← Home]] | [[System/Voice_Dump_Processing_Protocol|Processing Protocol →]] | [[Medicine/Medicine_Dashboard|Medicine →]]*
