# Obsidian Life OS

This repository is designed as a GitHub-backed Obsidian vault.

Core idea:

- Obsidian is the human interface.
- GitHub is the source of truth and version history.
- GitHub Actions are the scheduled automation layer.
- Jules or other repo agents should work through issues and pull requests.

Safety rule: raw notes are preserved, generated changes should be reviewed through pull requests, and automation should not delete personal knowledge.

## First workflow

1. Capture raw thoughts in `00_Inbox/`.
2. Run inbox and link-health workflows.
3. Review generated reports in `99_System/reports/`.
4. Process specific items through GitHub Issues or agent pull requests.
5. Merge only after review.

## Main dashboards

- [[10_Maps_Of_Content/Life_OS_Home|Life OS Home]]
- [[10_Maps_Of_Content/Medicine_MOC|Medicine]]
- [[10_Maps_Of_Content/Money_MOC|Money]]
- [[10_Maps_Of_Content/Mind_MOC|Mind]]
- [[10_Maps_Of_Content/Content_MOC|Content]]
- [[10_Maps_Of_Content/Projects_MOC|Projects]]
