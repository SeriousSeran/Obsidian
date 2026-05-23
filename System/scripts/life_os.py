#!/usr/bin/env python3
"""Life OS command line engine for the Obsidian vault."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None


ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "System" / "reports"


def colombo_timezone() -> dt.tzinfo:
    if ZoneInfo:
        try:
            return ZoneInfo("Asia/Colombo")
        except Exception:
            pass
    return dt.timezone(dt.timedelta(hours=5, minutes=30), name="Asia/Colombo")


COLOMBO = colombo_timezone()

REQUIRED_FOLDERS = [
    ".github/workflows",
    ".obsidian/snippets",
    "Inbox",
    "Inbox/Voice_Dumps",
    "Inbox/Ideas",
    "Inbox/Screenshots",
    "Daily/Daily_Notes",
    "Daily/Weekly_Reviews",
    "Daily/Monthly_Reviews",
    "Daily/Quarterly_Reviews",
    "Medicine",
    "Medicine/Topics",
    "Medicine/Clinical_Cases",
    "Medicine/Kanban",
    "Medicine/Learning",
    "Medicine/OSCE",
    "Medicine/Viva",
    "Money",
    "Money/Financial_Map",
    "Money/Business_Ideas",
    "Money/Learning",
    "Mind",
    "Mind/Reflections",
    "Mind/Learning",
    "Body",
    "Body/Learning",
    "Content",
    "Content/Ideas",
    "Content/Kanban",
    "Content/Learning",
    "Projects",
    "Projects/Active",
    "Projects/Kanban",
    "Projects/Learning",
    "Projects/Project_Dashboards",
    "Relationships",
    "Relationships/People",
    "Bucket_List",
    "Bucket_List/Experiences",
    "Maps",
    "Templates",
    "System/design",
    "System/git",
    "System/homepage",
    "System/learning_resources",
    "System/periodic_notes",
    "System/quickadd",
    "System/reports",
    "System/schemas",
    "System/scripts",
    "System/search",
    "System/tests",
]

REQUIRED_DASHBOARDS = [
    "Maps/Life_OS_Home.md",
    "Maps/Task_Dashboard.md",
    "Maps/Learning_Resource_Hub.md",
    "Maps/Life_OS_Command_Center.canvas",
    "Medicine/Medicine_Dashboard.md",
    "Money/Money_Dashboard.md",
    "Mind/Mind_Dashboard.md",
    "Body/Body_Dashboard.md",
    "Content/Content_Dashboard.md",
    "Projects/Project_Dashboards/Active_Project_Dashboard.md",
    "Relationships/Relationship_Dashboard.md",
    "Bucket_List/Bucket_List_Dashboard.md",
]

REQUIRED_MOCS = [
    "Maps/Medicine_MOC.md",
    "Maps/Money_MOC.md",
    "Maps/Mind_MOC.md",
    "Maps/Body_MOC.md",
    "Maps/Content_MOC.md",
    "Maps/Projects_MOC.md",
    "Maps/Relationships_MOC.md",
    "Maps/Bucket_List_MOC.md",
]

TEMPLATE_FILES = [
    "Daily_Note_Template.md",
    "Weekly_Review_Template.md",
    "Monthly_Review_Template.md",
    "Quarterly_Review_Template.md",
    "Voice_Dump_Template.md",
    "Processed_Voice_Dump_Template.md",
    "Project_Template.md",
    "Medical_Topic_Template.md",
    "Clinical_Case_Template.md",
    "Financial_Idea_Template.md",
    "Content_Idea_Template.md",
    "Reflection_Template.md",
    "Book_Note_Template.md",
    "Person_Note_Template.md",
]

SCHEMA_FILES = [
    "properties_schema.md",
    "voice_dump.schema.md",
    "processed_voice_dump.schema.md",
    "daily_note.schema.md",
    "weekly_review.schema.md",
    "medical_topic.schema.md",
    "clinical_case.schema.md",
    "financial_idea.schema.md",
    "project.schema.md",
    "content_idea.schema.md",
    "reflection.schema.md",
]

REPORT_FILES = [
    "inbox_report.md",
    "link_health.md",
    "root_triage_report.md",
    "voice_dump_processing_report.md",
    "life_os_validation_report.md",
    "dashboard_refresh_report.md",
]

REQUIRED_LEARNING_RESOURCES = [
    "Medicine/Learning/Medicine_Learning_Library.md",
    "Money/Learning/Money_Learning_Library.md",
    "Mind/Learning/Mind_Learning_Library.md",
    "Body/Learning/Body_Learning_Library.md",
    "Content/Learning/Content_Learning_Library.md",
    "Projects/Learning/Projects_Learning_Library.md",
    "System/learning_resources/Legal_Resource_Policy.md",
]

REQUIRED_BASE_NOTES = [
    "Medicine/OSCE/OSCE_Command_Center.md",
    "Medicine/Viva/Viva_Question_Bank.md",
    "Medicine/Topics/Clinical_Reasoning_Framework.md",
    "Money/Financial_Map/Financial_Command_Center.md",
    "Money/Business_Ideas/Business_Model_Lab.md",
    "Mind/Reflections/Pattern_Library.md",
    "Mind/Reflections/Decision_Journal.md",
    "Body/Body_Operating_System.md",
    "Content/Content_Operating_System.md",
    "Projects/Active/Life_OS_Project.md",
    "Projects/Product_Idea_Lab.md",
    "Relationships/People/People_Index.md",
    "Bucket_List/Experiences/Experience_Index.md",
]

OBSIDIAN_LINK_RE = re.compile(r"!?\[\[([^\]#|]+)(?:[#|][^\]]*)?\]\]")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def now_colombo() -> dt.datetime:
    return dt.datetime.now(COLOMBO)


def today_text() -> str:
    return now_colombo().date().isoformat()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def ensure_folders() -> None:
    for folder in REQUIRED_FOLDERS:
        (ROOT / folder).mkdir(parents=True, exist_ok=True)


def ensure_reports() -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)


def report_frontmatter() -> list[str]:
    return [
        "---",
        "type: report",
        "status: active",
        "review_needed: false",
        "---",
    ]


def make_report(title: str, sections: list[tuple[str, list[str]]]) -> str:
    body = report_frontmatter()
    body.extend([
        f"# {title}",
        "",
        "> Generated by the Life OS engine.",
        "",
        f"Generated: {now_colombo().isoformat(timespec='seconds')}",
        "",
    ])
    for heading, lines in sections:
        body.extend([f"## {heading}", ""])
        body.extend(lines or ["- None."])
        body.append("")
    return "\n".join(body).rstrip() + "\n"


def write_report(name: str, title: str, sections: list[tuple[str, list[str]]]) -> Path:
    ensure_reports()
    path = REPORTS / name
    path.write_text(make_report(title, sections), encoding="utf-8")
    return path


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def extract_headings(text: str) -> set[str]:
    return {line.strip() for line in text.splitlines() if line.startswith("#")}


def extract_obsidian_links(text: str) -> list[str]:
    return [m.group(1).strip() for m in OBSIDIAN_LINK_RE.finditer(text)]


def note_index() -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    for path in markdown_files():
        stem = path.stem
        index[stem.lower()].append(path)
        index[rel(path.with_suffix("")).lower()].append(path)
    return index


def link_target_exists(target: str, index: dict[str, list[Path]]) -> bool:
    key = target.removesuffix(".md").lower()
    if key in index:
        return True
    direct = ROOT / target
    if direct.exists():
        return True
    if (ROOT / f"{target}.md").exists():
        return True
    return False


def classify_root_file(path: Path) -> tuple[str, str, str]:
    name = path.name.lower()
    if "medicine" in name or "clinical" in name or "osce" in name or "exam" in name:
        return "Medicine/", "medical learning or clinical study", "high"
    if "money" in name or "finance" in name or "commerce" in name or "sales" in name:
        return "Money/", "money, commerce, or business planning", "high"
    if "content" in name or "writing" in name or "brand" in name:
        return "Content/", "content or publishing system", "high"
    if "project" in name or "product" in name or "idea" in name:
        return "Projects/", "project or product material", "medium"
    if "health" in name or "body" in name or "physique" in name:
        return "Body/", "body, health, or training material", "high"
    if "reflection" in name or "mind" in name or "journal" in name:
        return "Mind/", "reflection or mind material", "medium"
    if "person" in name or "relationship" in name or "people" in name:
        return "Relationships/", "relationship or people material", "medium"
    if "bucket" in name or "someday" in name or "dream" in name:
        return "Bucket_List/", "long-term goal or experience", "medium"
    if "template" in name:
        return "Templates/", "template material", "high"
    return "Inbox/", "unclear root note", "low"


def inbox_report(_args: argparse.Namespace) -> Path:
    ensure_folders()
    inbox = ROOT / "Inbox"
    rows = []
    categories = Counter()
    for path in sorted(inbox.rglob("*")):
        if path.is_dir() or path.name.startswith("."):
            continue
        suffix = path.suffix.lower()
        path_text = rel(path)
        if "voice_dumps" in path_text.lower():
            category = "raw voice dump"
        elif suffix in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            category = "screenshot"
        elif suffix in {".md", ".txt"} and "idea" in path.name.lower():
            category = "raw idea"
        elif suffix in {".md", ".txt", ".m4a", ".mp3", ".wav"}:
            category = "unprocessed file"
        else:
            category = "unclear file"
        categories[category] += 1
        rows.append(f"| {path_text} | {category} | review |")

    summary = [f"- {name}: {count}" for name, count in sorted(categories.items())] or ["- Inbox is empty."]
    return write_report(
        "inbox_report.md",
        "Inbox Report",
        [
            ("Summary", summary),
            ("What needs attention", rows or ["- Nothing in the inbox right now."]),
            ("Safe changes made", ["- Created missing Life OS folders if needed."]),
            ("Human review needed", ["- Review raw captures before promoting them into domain notes."]),
            ("Suggested next actions", ["- Use QuickAdd for capture.", "- Run `process-voice-dumps` after adding transcripts."]),
        ],
    )


def link_health(_args: argparse.Namespace) -> Path:
    index = note_index()
    inbound: Counter[str] = Counter()
    broken: list[str] = []
    old_links: list[str] = []
    for path in markdown_files():
        text = read_text(path)
        for target in extract_obsidian_links(text):
            key = target.removesuffix(".md").lower()
            inbound[key] += 1
            inbound[target.removesuffix(".md").lower()] += 1
            if not link_target_exists(target, index):
                broken.append(f"| {rel(path)} | [[{target}]] |")
            if any(prefix in target for prefix in ["00 - ", "02 - ", "03 - ", "05 - ", "06 - ", "07 - ", "08 - ", "09 - ", "10 - ", "11 - "]):
                old_links.append(f"| {rel(path)} | [[{target}]] |")

    title_counts = Counter(p.stem.lower() for p in markdown_files() if p.name.lower() != "readme.md")
    duplicate_titles = [f"- {title}" for title, count in title_counts.items() if count > 1]
    legacy_mocs = [f"- {rel(p)}" for p in markdown_files() if "legacy" in p.name.lower() and "moc" in p.name.lower()]
    orphans = []
    orphan_exclusions = (
        "Daily/Daily_Notes/",
        "Daily/Weekly_Reviews/",
        "Daily/Monthly_Reviews/",
        "Daily/Quarterly_Reviews/",
        "Templates/",
        "System/design/",
        "System/git/",
        "System/homepage/",
        "System/learning_resources/",
        "System/periodic_notes/",
        "System/quickadd/",
        "System/schemas/",
        "System/search/",
        "System/migration_reports/",
        "System/reports/",
    )
    for path in markdown_files():
        key = path.stem.lower()
        path_key = rel(path.with_suffix("")).lower()
        path_text = rel(path)
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        if path_text.startswith(orphan_exclusions):
            continue
        if key not in inbound and path_key not in inbound and "Maps" not in path_text:
            orphans.append(f"- {path_text}")

    return write_report(
        "link_health.md",
        "Link Health Report",
        [
            ("Summary", [f"- Broken links: {len(broken)}", f"- Orphan notes: {len(orphans)}"]),
            ("What needs attention", ["| Source | Link |", "|---|---|", *(broken or ["| None | none |"])]),
            ("Safe changes made", ["- No note links were changed automatically."]),
            ("Human review needed", [*(orphans[:100] or ["- No orphan notes found."])]),
            ("Suggested next actions", [*(duplicate_titles or ["- No duplicate titles found."]), *(legacy_mocs or ["- No legacy MOCs found."]), *(old_links or ["- No links point to old folder structure."])]),
        ],
    )


def root_triage(args: argparse.Namespace) -> Path:
    rows = []
    moves = []
    for path in sorted(ROOT.iterdir()):
        if path.name.startswith(".") or path.is_dir():
            continue
        if path.name in {"README.md", "AGENTS.md"}:
            continue
        dest, reason, confidence = classify_root_file(path)
        target = ROOT / dest / path.name
        rows.append(f"| {path.name} | {dest}{path.name} | {reason} | {confidence} |")
        moves.append((path, target))

    changes = ["- Dry run only. No files moved."]
    if args.apply:
        changes = []
        for source, target in moves:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(target))
            changes.append(f"- Moved `{rel(target)}`.")

    return write_report(
        "root_triage_report.md",
        "Root Triage Report",
        [
            ("Summary", [f"- Mode: {'apply' if args.apply else 'dry run'}", f"- Root files needing triage: {len(rows)}"]),
            ("What needs attention", ["| Current path | Suggested destination | Reason | Confidence |", "|---|---|---|---|", *(rows or ["| None | none | root is clean | high |"])]),
            ("Safe changes made", changes),
            ("Human review needed", ["- Review low-confidence destinations before applying moves."]),
            ("Suggested next actions", ["- Run with `--apply` only when suggested moves are obvious."]),
        ],
    )


def create_daily_note(_args: argparse.Namespace) -> Path:
    ensure_folders()
    today = now_colombo().date()
    destination = ROOT / "Daily" / "Daily_Notes" / f"{today.isoformat()}.md"
    template = ROOT / "Templates" / "Daily_Note_Template.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        content = read_text(template) if template.exists() else default_daily_template()
        destination.write_text(apply_template_dates(content, date=today.isoformat()), encoding="utf-8")
    return destination


def create_weekly_review(_args: argparse.Namespace) -> Path:
    ensure_folders()
    today = now_colombo().date()
    iso_year, iso_week, _ = today.isocalendar()
    week = f"{iso_year}-W{iso_week:02d}"
    destination = ROOT / "Daily" / "Weekly_Reviews" / f"{week}.md"
    template = ROOT / "Templates" / "Weekly_Review_Template.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        content = read_text(template) if template.exists() else default_weekly_template()
        destination.write_text(apply_template_dates(content, date=today.isoformat(), week=week), encoding="utf-8")
    return destination


def validate_notes(_args: argparse.Namespace) -> Path:
    ensure_folders()
    for report in REPORT_FILES:
        (REPORTS / report).touch(exist_ok=True)
    missing_folders = [item for item in REQUIRED_FOLDERS if not (ROOT / item).is_dir()]
    missing_dashboards = [item for item in REQUIRED_DASHBOARDS if not (ROOT / item).is_file()]
    missing_mocs = [item for item in REQUIRED_MOCS if not (ROOT / item).is_file()]
    missing_schemas = [item for item in SCHEMA_FILES if not (ROOT / "System" / "schemas" / item).is_file()]
    missing_templates = [item for item in TEMPLATE_FILES if not (ROOT / "Templates" / item).is_file()]
    missing_learning = [item for item in REQUIRED_LEARNING_RESOURCES if not (ROOT / item).is_file()]
    missing_base_notes = [item for item in REQUIRED_BASE_NOTES if not (ROOT / item).is_file()]
    missing_reports = [item for item in REPORT_FILES if not (ROOT / "System" / "reports" / item).is_file()]
    root_clutter = [
        p.name
        for p in ROOT.iterdir()
        if p.is_file() and p.name not in {"README.md", "AGENTS.md"} and not p.name.startswith(".")
    ]
    review_flags = []
    for path in markdown_files():
        text = read_text(path)
        fm = parse_frontmatter(text)
        path_text = rel(path)
        if path_text.startswith(("Medicine/", "Money/", "Mind/")) and fm.get("review_needed") not in {"true", "false"}:
            review_flags.append(f"- {path_text}")

    return write_report(
        "life_os_validation_report.md",
        "Life OS Validation Report",
        [
            ("Summary", [f"- Missing folders: {len(missing_folders)}", f"- Missing dashboards: {len(missing_dashboards)}", f"- Missing templates: {len(missing_templates)}", f"- Missing learning resources: {len(missing_learning)}", f"- Missing base notes: {len(missing_base_notes)}"]),
            ("What needs attention", [*(f"- {item}" for item in missing_folders), *(f"- {item}" for item in missing_dashboards), *(f"- {item}" for item in missing_mocs), *(f"- {item}" for item in missing_schemas), *(f"- {item}" for item in missing_templates), *(f"- {item}" for item in missing_learning), *(f"- {item}" for item in missing_base_notes), *(f"- {item}" for item in missing_reports)] or ["- System structure is complete."]),
            ("Safe changes made", ["- Created missing required folders.", "- Ensured report files exist."]),
            ("Human review needed", [*(f"- Root clutter: {item}" for item in root_clutter), *review_flags] or ["- No obvious review blockers."]),
            ("Suggested next actions", ["- Open [[Maps/Life_OS_Home]].", "- Enable the Life OS CSS snippet.", "- Configure QuickAdd and Periodic Notes."]),
        ],
    )


def process_voice_dumps(_args: argparse.Namespace) -> Path:
    ensure_folders()
    folder = ROOT / "Inbox" / "Voice_Dumps"
    processed_dir = ROOT / "Mind" / "Reflections"
    actions = []
    review = []
    for path in sorted(folder.iterdir()):
        if path.is_dir() or path.name.startswith("."):
            continue
        if path.suffix.lower() in {".m4a", ".mp3", ".wav"}:
            companion = path.with_suffix(".md")
            if not companion.exists():
                companion.write_text(audio_companion_template(path), encoding="utf-8")
                actions.append(f"- Created transcription-needed note: `{rel(companion)}`.")
            else:
                review.append(f"- Audio already has companion note: `{rel(companion)}`.")
        elif path.suffix.lower() == ".md":
            text = read_text(path)
            fm = parse_frontmatter(text)
            if fm.get("processed") == "true":
                review.append(f"- Skipped already processed transcript: `{rel(path)}`.")
                continue
            processed = processed_dir / f"Processed_{path.stem}.md"
            if not processed.exists():
                processed.write_text(processed_voice_template(path), encoding="utf-8")
                actions.append(f"- Created processed skeleton: `{rel(processed)}`.")
            if "processed_note:" not in text:
                path.write_text(text.rstrip() + f"\n\nprocessed_note: [[{rel(processed.with_suffix(''))}]]\n", encoding="utf-8")
                actions.append(f"- Linked raw transcript to processed note: `{rel(path)}`.")

    return write_report(
        "voice_dump_processing_report.md",
        "Voice Dump Processing Report",
        [
            ("Summary", [f"- Safe changes made: {len(actions)}", f"- Human review items: {len(review)}"]),
            ("What needs attention", review or ["- No voice dumps need attention."]),
            ("Safe changes made", actions or ["- No voice dumps found."]),
            ("Human review needed", ["- Review generated processed skeletons before treating them as insight."]),
            ("Suggested next actions", ["- Transcribe audio manually or with a trusted tool.", "- Convert processed insights into tasks and project updates."]),
        ],
    )


def refresh_dashboards(_args: argparse.Namespace) -> Path:
    ensure_folders()
    generated = []
    dashboard_paths = [ROOT / path for path in REQUIRED_DASHBOARDS if path.endswith(".md")]
    for path in dashboard_paths:
        if not path.exists():
            continue
        text = read_text(path)
        marker_start = "<!-- life-os-generated:start -->"
        marker_end = "<!-- life-os-generated:end -->"
        generated_block = "\n".join([
            marker_start,
            "## Generated System Snapshot",
            "",
            f"- Last refresh: {now_colombo().isoformat(timespec='seconds')}",
            "- Reports: [[System/reports/life_os_validation_report|Validation]], [[System/reports/link_health|Link Health]], [[System/reports/inbox_report|Inbox]]",
            marker_end,
        ])
        if marker_start in text and marker_end in text:
            pattern = re.compile(re.escape(marker_start) + r".*?" + re.escape(marker_end), re.DOTALL)
            text = pattern.sub(generated_block, text)
        else:
            text = text.rstrip() + "\n\n" + generated_block + "\n"
        path.write_text(text, encoding="utf-8")
        generated.append(f"- Refreshed `{rel(path)}`.")

    return write_report(
        "dashboard_refresh_report.md",
        "Dashboard Refresh Report",
        [
            ("Summary", [f"- Dashboards refreshed: {len(generated)}"]),
            ("What needs attention", ["- Review generated sections if dashboard layout feels noisy."]),
            ("Safe changes made", generated or ["- No dashboards refreshed."]),
            ("Human review needed", ["- Keep generated sections only where useful."]),
            ("Suggested next actions", ["- Open the homepage and command center canvas in Obsidian."]),
        ],
    )


def apply_template_dates(content: str, *, date: str, week: str | None = None) -> str:
    result = content.replace("{{date}}", date)
    if week:
        result = result.replace("{{week}}", week)
    return result.rstrip() + "\n"


def default_daily_template() -> str:
    return """---
type: daily-note
status: active
date: {{date}}
review_needed: false
---
# {{date}}

## Capture

## Priorities

## Actions

## End of Day Review
"""


def default_weekly_template() -> str:
    return """---
type: weekly-review
status: active
week: {{week}}
review_needed: true
---
# Weekly Review {{week}}

## Wins

Not enough data.

## Open Loops

Not enough data.

## Projects

Not enough data.

## Direction

Not enough data.
"""


def audio_companion_template(path: Path) -> str:
    return f"""---
type: voice-dump
status: raw
source: {path.name}
needs_transcription: true
processed: false
review_needed: true
created: "{today_text()}"
---
# {path.stem}

## Raw Source

Audio file: [[{rel(path)}]]

## Transcript

Not transcribed yet.
"""


def processed_voice_template(raw_path: Path) -> str:
    return f"""---
type: processed-voice-dump
status: processed
source: {rel(raw_path)}
review_needed: true
created: "{today_text()}"
---
# Processed {raw_path.stem}

## Source

[[{rel(raw_path.with_suffix(''))}]]

## Core Insight

Not processed yet.

## Action Items

- [ ] Review transcript.

## Links

## Project Updates

## Review Notes
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Life OS engine for the Obsidian vault.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("inbox-report").set_defaults(func=inbox_report)
    sub.add_parser("link-health").set_defaults(func=link_health)
    root_parser = sub.add_parser("root-triage")
    root_parser.add_argument("--apply", action="store_true", help="Move root files into suggested destinations.")
    root_parser.set_defaults(func=root_triage)
    sub.add_parser("create-daily-note").set_defaults(func=create_daily_note)
    sub.add_parser("create-weekly-review").set_defaults(func=create_weekly_review)
    sub.add_parser("process-voice-dumps").set_defaults(func=process_voice_dumps)
    sub.add_parser("validate-notes").set_defaults(func=validate_notes)
    sub.add_parser("refresh-dashboards").set_defaults(func=refresh_dashboards)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    result = args.func(args)
    print(rel(result) if result.is_relative_to(ROOT) else result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
