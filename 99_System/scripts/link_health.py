import re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = ROOT / "99_System" / "reports"
REPORT = REPORT_DIR / "link_health.md"
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
IGNORE_PARTS = {".git", ".obsidian"}


def markdown_files():
    for p in ROOT.rglob("*.md"):
        if any(part in IGNORE_PARTS for part in p.parts):
            continue
        yield p


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    md_files = list(markdown_files())
    stems = {p.stem.lower(): p for p in md_files}
    rels = {p.relative_to(ROOT).with_suffix("").as_posix().lower(): p for p in md_files}
    incoming_count = {p: 0 for p in md_files}
    broken = []

    for p in md_files:
        text = p.read_text(encoding="utf-8", errors="ignore")
        for target in LINK_RE.findall(text):
            key = target.strip().lower()
            found = stems.get(Path(key).name) or rels.get(key)
            if found:
                incoming_count[found] = incoming_count.get(found, 0) + 1
            else:
                broken.append((p, target))

    orphan_notes = [p for p, count in incoming_count.items() if count == 0 and "10_Maps_Of_Content" not in p.as_posix() and "90_Templates" not in p.as_posix() and p.name != "README.md"]

    now = datetime.now(ZoneInfo("Asia/Colombo"))
    lines = ["# Link Health Report", "", f"Generated: {now.strftime('%Y-%m-%d %H:%M')} Asia/Colombo", "", "## Broken links", ""]
    if broken:
        for src, target in sorted(broken, key=lambda x: x[0].as_posix()):
            lines.append(f"- `{src.relative_to(ROOT).as_posix()}` → `[[{target}]]`")
    else:
        lines.append("No broken links detected.")
    lines += ["", "## Possible orphan notes", ""]
    if orphan_notes:
        for p in sorted(orphan_notes):
            lines.append(f"- `{p.relative_to(ROOT).as_posix()}`")
    else:
        lines.append("No orphan notes detected.")
    lines += ["", "## Counts", "", f"Markdown files scanned: **{len(md_files)}**", f"Broken links: **{len(broken)}**", f"Possible orphans: **{len(orphan_notes)}**", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
