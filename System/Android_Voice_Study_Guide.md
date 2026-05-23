---
type: guide
status: active
cssclasses:
  - life-os-dashboard
review_needed: false
icon: "📱"
---

# 📱 Android Voice Study Guide

> **The complete path**: You speak → vault captures it → Claudian processes it → notes + flashcards + explore map.

---

## 🗺️ The Pipeline (two direct paths — no ChatGPT needed)

### Path A — Obsidian Mobile mic (fastest, zero friction)

```
📱 Open Obsidian Mobile → Inbox/Voice_Dumps/ → new note
       ↓
🎤 Tap keyboard mic → speak directly → text types itself
       ↓
💾 Save note (syncs to desktop via git/Obsidian Sync)
       ↓
🖥️ On desktop → say "Process my voice dump" to Claudian
       ↓
🧠 Notes + flashcards + explore paths created automatically
```

### Path B — Claude Android → copy to vault (adds AI pre-processing)

```
📱 Open Claude app → tap mic → speak your study notes
       ↓
🤖 Claude transcribes + understands context as you talk
       ↓
💬 Say: "Format this as a vault voice dump note"
       ↓
📋 Copy the markdown Claude gives you
       ↓
📱 Paste into Obsidian Mobile (Inbox/Voice_Dumps/) or GitHub app
       ↓
🖥️ On desktop → say "Process my voice dump" to Claudian
```

---

## Why Claude Android Can't Write Directly to Your Vault

> *"Why can't Claude just add it straight to the vault?"*

The Claude app on Android (claude.ai) and Claude Code on your desktop are two separate systems:

| | Claude Android App | Claude Code (Claudian) |
|---|---|---|
| **Lives on** | Cloud / claude.ai | Your PC, inside Obsidian |
| **File access** | ❌ Cannot touch your PC files | ✅ Full vault read/write |
| **Can transcribe voice** | ✅ Yes | ✅ Yes (if you paste it) |
| **Can process + format** | ✅ Yes (you copy the output) | ✅ Yes (runs automatically) |
| **Can write to vault** | ❌ No — the gap | ✅ Yes — the power |

**The gap**: Android Claude can prepare the note perfectly formatted — but you're the bridge who pastes it into Obsidian Mobile or GitHub. One paste, then Claudian takes over on desktop.

**Future option**: When the Agent Client plugin on desktop is running, it listens — but Android Claude can't call it remotely yet. This is a tooling limitation, not a conceptual one.

---

## 📲 Method A — Direct Dictation into Obsidian Mobile

**What you need**: Obsidian app on Android + vault synced (see setup below)

1. Open **Obsidian** on Android
2. Navigate to `Inbox/Voice_Dumps/`
3. Tap **`+`** → new note
4. Title: `Voice Dump 2026-05-23` *(today's date)*
5. In the note body — **tap the 🎤 microphone on your keyboard**
6. Speak your study notes — Android voice-to-text types as you talk
7. Tap mic again to stop
8. Add one line at the top: `domain: medicine` (or whichever domain)
9. Save — it auto-syncs to your desktop vault

> **Tip**: Android's keyboard mic (Google voice input) is surprisingly accurate for medical terms. Say terms slowly the first time if it struggles — it learns.

---

## 📲 Method B — Claude Android → Formatted Note → Paste

**Best for**: When you want Claude to already structure your thoughts before Claudian processes them

1. Open **Claude** on Android
2. Tap the mic (or type if you prefer)
3. Speak your study notes naturally — stream of consciousness is fine
4. When done, send this message:

> *"Format everything I just said as an Obsidian voice dump note. Use this exact structure:*
> ```
> ---
> type: voice-dump
> status: raw
> domain: medicine
> tags: [voice-dump, unprocessed]
> ---
> # Voice Dump [TODAY'S DATE]
>
> ## Raw Transcript
> [cleaned transcript]
>
> ## Key Topics
> [bullet list of main concepts]
> ```"*

5. Copy Claude's response
6. Open **Obsidian Mobile** → `Inbox/Voice_Dumps/` → new note → paste → save

---

## 📲 Method C — GitHub Mobile (No Obsidian Mobile needed)

**Best for**: Quick capture when Obsidian isn't installed, you have a transcript ready

1. Open **GitHub** app → `SeriousSeran/Obsidian`
2. Navigate to `Inbox/Voice_Dumps/`
3. Tap **`+`** → "Create new file"
4. Filename: `Voice Dump 2026-05-23.md`
5. Paste content with basic header:

```markdown
---
type: voice-dump
status: raw
domain: medicine
tags: [voice-dump, unprocessed]
---
# Voice Dump 2026-05-23

## Raw Transcript

[YOUR TEXT HERE]
```

6. Tap **"Commit new file"** → appears in vault immediately

---

## 🔧 Sync Setup (one-time, so mobile → desktop works)

For Method A to auto-sync, you need one of:

| Method | Cost | Effort |
|---|---|---|
| **Easy-git (already installed)** | Free | Tap "Pull" in Obsidian Mobile after creating note |
| **Obsidian Sync** | $4/month | Zero friction, instant |
| **Syncthing** | Free | One-time setup, works offline |

> **Quickest workaround without sync**: After saving the note on mobile, use GitHub app to commit it (Method C), then on desktop: `easy-git → Pull`. Takes 30 seconds.

---

## 🖥️ Back on Desktop — Trigger Claudian

Open the **Agent Client panel** (ribbon 🤖) or this terminal and say:

> **"Process my voice dump"**

Claudian runs the [[System/Voice_Dump_Processing_Protocol|7-step protocol]] and creates:
- ✅ Clean domain note in the right folder (`Medicine/Topics/` etc.)
- 📇 Flashcards ready in SR deck
- 🔭 "Explore Further" — 3–5 rabbit holes for your next session
- ✅ Tasks with due dates (+1 day SR review, +3 days explore #1, +7 days explore #2)

---

## 📇 After Processing — SR Review

New flashcards are in your deck immediately. To review:
- Click **📇 ribbon icon** in Obsidian
- Status bar shows: "X cards due"

**SR grades**: Again / Hard / Good / Easy — be honest, the algorithm schedules next review accordingly.

---

## 🔭 The Explore Further System

Every processed dump generates a list like:

> *"You studied ACE inhibitors → explore next:*
> *1. ARBs — how they differ and when to use each*
> *2. RAAS pathway — connect to heart failure management*
> *3. Renal protection in diabetic nephropathy*
> *4. OSCE: managing hypertensive emergency step-by-step"*

These become **due-dated tasks** so they survive into your next sessions:
```
- [ ] Explore: ARBs vs ACE inhibitors 📅 2026-05-26
- [ ] Explore: RAAS in heart failure 📅 2026-05-30
```

They appear on your daily note, home dashboard, and Tasks query.

---

## ⏰ Reminder Loop

| Day | What happens |
|---|---|
| Dump day | Claudian processes → notes + cards created |
| +1 day | SR: review new flashcards (📇 ribbon) |
| +3 days | Task: read Explore Further #1 |
| +7 days | Task: read Explore Further #2 |
| Weekly Review | All processed dumps surface in review |

---

## 💡 Tips for Speaking

- **Pause between concepts** — gives transcription time to catch up
- **Spell out abbreviations once**: "MI — myocardial infarction"
- **Narrate your confusion**: *"I don't understand why X causes Y"* → becomes a flashcard question
- **Ask questions out loud**: *"Wait, what's the difference between A and B?"* → Claudian answers these in Explore Further
- **No need to be clean** — Claudian strips filler words

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
