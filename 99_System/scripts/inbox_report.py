from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = ROOT / "99_System" / "reports"
REPORT = REPORT_DIR / "inbox_report.md"
WATCH_DIRS = ["00_Inbox/Voice_Dumps", "00_Inbox/Raw_Ideas"]
PROCESSED_MARKERS = ["status: processed", "status: done"]


def is_processed(path: Path) -> bool:
    if path.suffix.lower() != ".md":
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")[:2000].lower()
    return any(marker in text for marker in PROCESSED_MARKERS)


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(ZoneInfo("Asia/Colombo"))
    lines = [
        "# Inbox Report",
        "",
        f"Generated: {now.strftime('%Y-%m-%d %H:%M')} Asia/Colombo",
        "",
        "This report only scans and summarizes inbox files.",
        "",
    ]
    total = 0
    for rel in WATCH_DIRS:
        folder = ROOT / rel
        folder.mkdir(parents=True, exist_ok=True)
        files = [p for p in folder.rglob("*") if p.is_file() and p.name != ".gitkeep"]
        unprocessed = [p for p in files if not is_processed(p)]
        total += len(unprocessed)
        lines += [f"## {rel}", ""]
        if not unprocessed:
            lines += ["No unprocessed files found.", ""]
        else:
            for p in sorted(unprocessed):
                lines.append(f"- [ ] `{p.relative_to(ROOT).as_posix()}`")
            lines.append("")
    lines += ["## Summary", "", f"Total unprocessed files: **{total}**", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
