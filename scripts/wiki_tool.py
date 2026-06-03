#!/usr/bin/env python3
"""
wiki_tool.py -- Lint and management CLI for the project-scoping-tool wiki.

The wiki lives in wiki/. Claude writes all page content during sessions.
This script handles file management, staleness detection, and link validation.

Usage:
  python3 scripts/wiki_tool.py list          # All pages with last-modified date
  python3 scripts/wiki_tool.py lint          # Stale pages, broken [[links]], missing sections
  python3 scripts/wiki_tool.py sources       # Client folders with no wiki page
  python3 scripts/wiki_tool.py log           # Last 20 log entries
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Resolve repo root regardless of where this script is called from
REPO_ROOT = Path(__file__).parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
LOG_FILE = WIKI_DIR / "log.md"

# Staleness thresholds
STALE_DAYS_DEFAULT = 30
STALE_DAYS_ACTIVE_DELIVERY = 14

# Required sections per page type (checked by lint)
REQUIRED_SECTIONS = {
    "clients": [
        "## Profile",
        "## Engagement Summary",
        "## Scope & Estimate",
        "## Key Decisions",
        "## Open Items",
        "## Risks & Watchouts",
        "## Calibration Notes",
        "## Cross-links",
    ],
    "patterns": [
        "## Pattern Summary",
        "## Cross-links",
    ],
    "methodology": [
        "## Overview",
        "## Cross-links",
    ],
}

# Active delivery clients (use tighter staleness threshold).
# Intentionally empty in the shared repo — client slugs are not committed.
# Populate locally if you want tighter thresholds for your active engagements.
ACTIVE_DELIVERY_SLUGS: set = set()

# Directories to skip when checking for un-ingested client folders.
# Client engagement folders are gitignored (see .gitignore) and live locally only,
# so client names are intentionally NOT listed here. Only generic infra/asset dirs.
SKIP_DIRS = {
    # Repo infrastructure
    "wiki", "scripts", "templates", "calibration", "tests",
    ".git", ".claude", ".claude-plugin", ".api-specs", ".pytest_cache",
    "memory", "skills",
    # Non-client asset dirs
    "Gamma Examples", "Sayer Proposal Examples",
    "_archive", "_templates",
    "consulting-delivery-plugin",
    # Sub-dirs that appear at top level
    "discovery", "emails", "hubspot",
}


def get_all_wiki_pages() -> list:
    """Return all .md files in wiki/ excluding infrastructure files."""
    skip = {"schema.md", "index.md", "log.md"}
    pages = []
    for path in WIKI_DIR.rglob("*.md"):
        if path.name not in skip:
            pages.append(path)
    return sorted(pages)


def get_last_updated(path: Path) -> Optional[datetime]:
    """Extract 'Last updated: YYYY-MM-DD' from page frontmatter."""
    try:
        content = path.read_text(encoding="utf-8")
        match = re.search(r"Last updated:\s*(\d{4}-\d{2}-\d{2})", content)
        if match:
            return datetime.strptime(match.group(1), "%Y-%m-%d")
    except Exception:
        pass
    return None


def get_page_status(path: Path) -> str:
    """Extract Status line from page header."""
    try:
        content = path.read_text(encoding="utf-8")
        match = re.search(r"Status:\s*([^\n>]+)", content)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return "Unknown"


def get_all_wiki_slugs() -> set:
    """Return set of all wiki page slugs (filename without .md)."""
    return {p.stem for p in get_all_wiki_pages()}


def find_cross_links(content: str) -> list:
    """Extract all [[page-name]] references from content."""
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def cmd_list(args):
    """List all wiki pages with last-modified date and status."""
    pages = get_all_wiki_pages()
    today = datetime.today()

    print("\n{:<45} {:<28} {}".format("Page", "Updated", "Status/Section"))
    print("-" * 95)

    for path in pages:
        rel = str(path.relative_to(WIKI_DIR))
        last_updated = get_last_updated(path)
        if path.parent.name == "clients":
            status = get_page_status(path)
        else:
            status = path.parent.name

        if last_updated:
            age = (today - last_updated).days
            age_str = "{} ({}d ago)".format(last_updated.strftime("%Y-%m-%d"), age)
        else:
            age_str = "no date"

        print("{:<45} {:<28} {}".format(rel, age_str, status))

    print("\nTotal: {} pages".format(len(pages)))


def cmd_lint(args):
    """Check for stale pages, broken [[links]], and missing required sections."""
    pages = get_all_wiki_pages()
    today = datetime.today()
    all_slugs = get_all_wiki_slugs()
    issues = []
    warnings = []

    for path in pages:
        slug = path.stem
        rel = str(path.relative_to(WIKI_DIR))
        section = path.parent.name  # clients, patterns, methodology

        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            issues.append("READ ERROR {} -- {}".format(rel, e))
            continue

        # Staleness check
        last_updated = get_last_updated(path)
        threshold = STALE_DAYS_ACTIVE_DELIVERY if slug in ACTIVE_DELIVERY_SLUGS else STALE_DAYS_DEFAULT
        if last_updated:
            age = (today - last_updated).days
            if age > threshold:
                issues.append("STALE     {:<45} last updated {}d ago (threshold: {}d)".format(
                    rel, age, threshold))
        else:
            warnings.append("NO DATE   {:<45} missing 'Last updated:' frontmatter".format(rel))

        # Required sections check
        required = REQUIRED_SECTIONS.get(section, [])
        for section_header in required:
            if section_header not in content:
                issues.append("MISSING   {:<45} missing section '{}'".format(rel, section_header))

        # Broken cross-links
        links = find_cross_links(content)
        for link in links:
            if link not in all_slugs:
                warnings.append("BROKEN    {:<45} [[{}]] -> no such page".format(rel, link))

        # UNINGESED stub detection
        if "UNINGESED" in content:
            warnings.append("UNINGESED {:<45} stub page needs full ingest".format(rel))

    # Print results
    if not issues and not warnings:
        print("\n  Wiki is clean. No issues found.")
    else:
        if issues:
            print("\nISSUES ({}):".format(len(issues)))
            for i in issues:
                print("  {}".format(i))
        if warnings:
            print("\nWARNINGS ({}):".format(len(warnings)))
            for w in warnings:
                print("  {}".format(w))
        print("\nTotal: {} issues, {} warnings".format(len(issues), len(warnings)))


def cmd_sources(args):
    """Show client folders that have no corresponding wiki page."""
    all_slugs = get_all_wiki_slugs()
    missing = []

    for item in REPO_ROOT.iterdir():
        if not item.is_dir():
            continue
        if item.name.startswith(".") or item.name.startswith("_"):
            continue
        if item.name in SKIP_DIRS:
            continue
        # Convert folder name to expected wiki slug
        slug = item.name.lower().replace(" ", "-")
        if slug not in all_slugs:
            missing.append("UNINGESED  {}  (expected wiki/clients/{}.md)".format(
                item.name, slug))

    if not missing:
        print("\n  All client folders have wiki pages.")
    else:
        print("\nClient folders missing wiki pages ({}):".format(len(missing)))
        for m in missing:
            print("  {}".format(m))


def cmd_log(args):
    """Show last N log entries from wiki/log.md."""
    n = getattr(args, "n", 20)
    if not LOG_FILE.exists():
        print("wiki/log.md not found.")
        return
    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    # Filter to actual log entries (lines starting with a date like 2026-)
    entries = [l for l in lines if re.match(r"\d{4}-\d{2}-\d{2}", l)]
    print("\nLast {} log entries:".format(min(n, len(entries))))
    print("-" * 80)
    for entry in entries[-n:]:
        print(entry)


def main():
    parser = argparse.ArgumentParser(
        description="Wiki management CLI for project-scoping-tool"
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all wiki pages with dates and status")
    subparsers.add_parser("lint", help="Check for stale pages, broken links, missing sections")
    subparsers.add_parser("sources", help="Show client folders with no wiki page")

    log_parser = subparsers.add_parser("log", help="Show recent log entries")
    log_parser.add_argument("--n", type=int, default=20, help="Number of entries to show")

    args = parser.parse_args()

    if args.command == "list":
        cmd_list(args)
    elif args.command == "lint":
        cmd_lint(args)
    elif args.command == "sources":
        cmd_sources(args)
    elif args.command == "log":
        cmd_log(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
