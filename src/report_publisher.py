from __future__ import annotations

import re
from pathlib import Path
from shutil import copyfile


REPLAY_REPORT_PATTERN = re.compile(r"^replay_(\d{4}-\d{2}-\d{2})_report\.md$")


def _ensure_report_dirs(reports_dir: str | Path) -> tuple[Path, Path]:
    reports_path = Path(reports_dir)
    archive_path = reports_path / "archive"
    reports_path.mkdir(parents=True, exist_ok=True)
    archive_path.mkdir(parents=True, exist_ok=True)
    return reports_path, archive_path


def _copy_latest(source: Path, destination: Path) -> None:
    if source.exists():
        copyfile(source, destination)


def _copy_archive(source: Path, destination: Path) -> None:
    if source.exists() and not destination.exists():
        copyfile(source, destination)


def publish_investor_report(
    xlsx_path: str | Path,
    markdown_path: str | Path,
    report_date: str,
    reports_dir: str | Path = "reports",
) -> dict[str, Path]:
    """Publish the latest and archived human-facing investor report files."""
    reports_path, archive_path = _ensure_report_dirs(reports_dir)
    xlsx_source = Path(xlsx_path)
    markdown_source = Path(markdown_path)

    latest_xlsx = reports_path / "latest_investor_report.xlsx"
    latest_markdown = reports_path / "latest_investor_report.md"
    archive_xlsx = archive_path / f"investor_report_{report_date}.xlsx"
    archive_markdown = archive_path / f"investor_report_{report_date}.md"

    _copy_latest(xlsx_source, latest_xlsx)
    _copy_latest(markdown_source, latest_markdown)
    _copy_archive(xlsx_source, archive_xlsx)
    _copy_archive(markdown_source, archive_markdown)

    return {
        "latest_xlsx": latest_xlsx,
        "latest_markdown": latest_markdown,
        "archive_xlsx": archive_xlsx,
        "archive_markdown": archive_markdown,
    }


def publish_replay_report(
    xlsx_path: str | Path,
    markdown_path: str | Path,
    replay_date: str,
    reports_dir: str | Path = "reports",
) -> dict[str, Path]:
    """Publish the latest and archived human-facing historical replay files."""
    reports_path, archive_path = _ensure_report_dirs(reports_dir)
    xlsx_source = Path(xlsx_path)
    markdown_source = Path(markdown_path)

    latest_xlsx = reports_path / "latest_replay_report.xlsx"
    latest_markdown = reports_path / "latest_replay_report.md"
    archive_xlsx = archive_path / f"replay_{replay_date}.xlsx"
    archive_markdown = archive_path / f"replay_{replay_date}.md"

    _copy_latest(xlsx_source, latest_xlsx)
    _copy_latest(markdown_source, latest_markdown)
    _copy_archive(xlsx_source, archive_xlsx)
    _copy_archive(markdown_source, archive_markdown)

    return {
        "latest_xlsx": latest_xlsx,
        "latest_markdown": latest_markdown,
        "archive_xlsx": archive_xlsx,
        "archive_markdown": archive_markdown,
    }


def publish_latest_existing_replay(
    results_dir: str | Path,
    reports_dir: str | Path = "reports",
) -> dict[str, Path] | None:
    """Publish the newest replay report already present in results, if available."""
    results_path = Path(results_dir)
    candidates = []
    for markdown_path in results_path.glob("replay_*_report.md"):
        match = REPLAY_REPORT_PATTERN.match(markdown_path.name)
        if not match:
            continue
        replay_date = match.group(1)
        xlsx_path = results_path / f"replay_{replay_date}_portfolio.xlsx"
        if xlsx_path.exists():
            candidates.append((markdown_path.stat().st_mtime, replay_date, xlsx_path, markdown_path))

    if not candidates:
        return None

    _, replay_date, xlsx_path, markdown_path = max(candidates, key=lambda item: item[0])
    return publish_replay_report(
        xlsx_path=xlsx_path,
        markdown_path=markdown_path,
        replay_date=replay_date,
        reports_dir=reports_dir,
    )
