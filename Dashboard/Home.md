---
type: homepage
status: active
cssclasses:
  - life-os-dashboard
icon: "🏠"
review_needed: false
---

# Welcome Back, Seran ☀️

> *Your calm command center. Capture → Think → Build → Review.*

---

## Quick Capture ⚡

> Use **QuickAdd** (`Ctrl+Alt+D`) to instantly log ideas, tasks, voice dumps, or new notes.

| Capture | Shortcut | Target |
|---|---|---|
| Raw Idea | `Ctrl+Alt+I` | `Inbox/Ideas` |
| Voice Dump | `Ctrl+Alt+V` | `Inbox/Voice_Dumps` |
| Quick Task | `Ctrl+Alt+T` | `Inbox` |
| Full Menu | `Ctrl+Alt+O` | Life OS Menu |

---

## Today's Focus 🎯

```tasks
not done
(due today) OR (scheduled today)
sort by priority
```

---

## Command Centers 🗺️

| Domain | Hub | Kanban | Status |
|---|---|---|---|
| 🩺 Medicine | [[Medicine/Medicine_Dashboard]] | [[Medicine/Kanban/Medicine_Study_Pipeline]] | Active |
| 💰 Money | [[Money/Money_Dashboard]] | — | Active |
| 🧠 Mind | [[Mind/Mind_Dashboard]] | — | Active |
| 💪 Body | [[Body/Body_Dashboard]] | — | Active |
| 📹 Content | [[Content/Content_Dashboard]] | [[Content/Kanban/Content_Pipeline]] | Active |
| 🔧 Projects | [[Projects/Project_Dashboards/Active_Project_Dashboard]] | [[Projects/Kanban/Life_OS_Roadmap]] | Active |
| 🤝 People | [[Relationships/Relationship_Dashboard]] | — | Active |
| 🌍 Bucket List | [[Bucket_List/Bucket_List_Dashboard]] | — | Active |

---

## 🎙️ Voice Dumps — Pending Processing

```dataview
TABLE status, domain, created AS "Spoken"
FROM "Inbox/Voice_Dumps"
WHERE file.name != ".gitkeep" AND status = "raw"
SORT created DESC
LIMIT 8
```

> Say **"Process my voice dump"** to Claudian → notes + flashcards + explore paths auto-created.  
> [[System/Android_Voice_Study_Guide|📱 Android Guide]] | [[System/Voice_Dump_Processing_Protocol|⚙️ Protocol]]

---

## Inbox — Needs Processing 📥

```dataview
TABLE file.mtime AS "Captured", type
FROM "Inbox"
WHERE file.name != ".gitkeep"
SORT file.mtime DESC
LIMIT 15
```

---

## Review Queue 🔁

```dataview
TABLE type, status, domains, file.mtime AS "Updated"
FROM ""
WHERE review_needed = true
SORT file.mtime DESC
LIMIT 10
```

---

## Overdue & Upcoming Tasks ⏰

```tasks
not done
due before in 3 days
sort by due
limit 20
```

---

## Recent Notes 📝

```dataview
TABLE type, status, file.mtime AS "Last Edited"
FROM ""
WHERE file.name != "Home"
SORT file.mtime DESC
LIMIT 12
```

---

## 🤖 AI Agents

| Agent | Access | Purpose |
|---|---|---|
| **Claudian** (Claude Code) | Agent Client panel or this terminal | Vault design, writing, analysis |
| **Gemini CLI** | Agent Client → switch agent | Research, multimodal, long context |
| **Jules (Google)** | jules.google.com → SeriousSeran/Obsidian | Scheduled maintenance, GitHub Actions |

> Open **Agent Client** panel (ribbon `🤖`) to chat with Claudian directly inside Obsidian.  
> [[Agent Client/Agent_Client_Index|→ Agent Client Hub]]

---

## 📱 Android → Vault

> Found something interesting on Android Claude? Do this:
> 1. Copy the insight / note
> 2. Create a new note in [[Inbox]] titled `📱 [topic]`
> 3. Paste content + add tag `#android-capture`
> 4. Claudian or Jules will process it into the right domain

```dataview
TABLE file.ctime AS "Captured"
FROM "Inbox"
WHERE contains(file.tags, "#android-capture")
SORT file.ctime DESC
LIMIT 8
```

---

## 📅 Google Calendar

> Connect once: `Ctrl+P` → "Google Calendar: Sign in with Google"  
> After auth, events appear here automatically.

```dataview
TABLE file.ctime AS "Date"
FROM "Daily/Daily_Notes"
SORT file.ctime DESC
LIMIT 5
```

---

## Navigation 🧭

- [[Maps/Life_OS_Home|Life OS Home]] — Full system map
- [[Maps/Task_Dashboard|Task Dashboard]] — All tasks by domain
- [[Maps/Learning_Resource_Hub|Learning Hub]] — Books, courses, resources
- [[Daily/Daily_Notes|Daily Notes]] — All past days
- [[Daily/Weekly_Reviews|Weekly Reviews]] — Weekly reflections
- [[Templates|Templates]] — All Templater templates
- [[System/Obsidian_Plugin_Setup|Plugin Setup Guide]] — Plugin reference
- [[Agent Client/Agent_Client_Index|Agent Client Hub]] — AI agent chat

---

## System Health 🛠️

- [[System/reports/life_os_validation_report|Validation Report]]
- [[System/reports/inbox_report|Inbox Report]]
- [[System/reports/link_health|Link Health]]
- [[System/reports/root_triage_report|Root Triage]]
