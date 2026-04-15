"""Client intake CLI — net-new scoping workflow.

Given a HubSpot record URL (deal / company / contact), pulls the associated
company + contacts + engagements from HubSpot, matches Fireflies transcripts
by attendee email, and scaffolds a `{Client Name}/` folder under the repo
root per the convention in CLAUDE.md.

Usage:
    python3 scripts/intake.py --test-only
    python3 scripts/intake.py --url <HUBSPOT_URL> [--dry-run]
    python3 scripts/intake.py --url <HUBSPOT_URL> --client-name "Acme Corp"
    python3 scripts/intake.py --url <HUBSPOT_URL> --force   # overwrite existing

The script is read-only against HubSpot/Fireflies. The only writes are
to the filesystem under the repo root.
"""

from __future__ import annotations

import argparse
import re
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from fireflies_client import FirefliesClient
from hubspot_client import HubSpotClient, parse_record_url
from hubspot_models import SimplePublicObjectWithAssociations


REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"

MAX_ENGAGEMENTS_PER_TYPE = 25
FIREFLIES_LOOKBACK_DAYS = 180


# ---------------------------------------------------------------------------
# Phase 1 — API smoke test
# ---------------------------------------------------------------------------


def _smoke_test() -> int:
    """Verify both API tokens work. Returns 0 on success, 1 if anything fails."""
    all_ok = True

    print("-- HubSpot --")
    try:
        HubSpotClient().ping()
        print("  OK")
    except Exception as exc:  # noqa: BLE001 — report-and-continue for ping
        all_ok = False
        print(f"  FAIL: {exc}")

    print("-- Fireflies --")
    try:
        FirefliesClient().ping()
        print("  OK")
    except Exception as exc:  # noqa: BLE001
        all_ok = False
        print(f"  FAIL: {exc}")

    return 0 if all_ok else 1


# ---------------------------------------------------------------------------
# Phase 2 — HubSpot fetch
# ---------------------------------------------------------------------------


class HubSpotBundle:
    """All HubSpot data pulled for one intake run."""

    def __init__(
        self,
        portal_id: str,
        primary_object_type: str,
        primary: SimplePublicObjectWithAssociations,
        company: Optional[SimplePublicObjectWithAssociations],
        contacts: List[Any],
        engagements: Dict[str, List[SimplePublicObjectWithAssociations]],
    ) -> None:
        self.portal_id = portal_id
        self.primary_object_type = primary_object_type
        self.primary = primary
        self.company = company
        self.contacts = contacts
        self.engagements = engagements

    @property
    def client_name(self) -> str:
        if self.company is not None:
            name = self.company.properties.get("name")
            if name:
                return name
        # Fall back to dealname or the primary record id
        if self.primary_object_type == "deals":
            dn = self.primary.properties.get("dealname")
            if dn:
                return dn
        return f"Unknown ({self.primary_object_type}:{self.primary.id})"

    @property
    def contact_emails(self) -> List[str]:
        out: List[str] = []
        for c in self.contacts:
            email = c.properties.get("email") if c.properties else None
            if email:
                out.append(email)
        return out


def _associated_ids(
    record: SimplePublicObjectWithAssociations, to_object_type: str
) -> List[str]:
    if not record.associations:
        return []
    coll = record.associations.get(to_object_type)
    if coll is None:
        return []
    return [r.id for r in coll.results]


def _fetch_engagements(
    hs: HubSpotClient, from_type: str, from_id: str
) -> Dict[str, List[SimplePublicObjectWithAssociations]]:
    engagements: Dict[str, List[SimplePublicObjectWithAssociations]] = {}
    for eng_type in ("notes", "calls", "meetings", "emails"):
        records: List[SimplePublicObjectWithAssociations] = []
        try:
            ids = list(hs.iter_associations(from_type, from_id, eng_type))
        except Exception as exc:  # noqa: BLE001
            print(f"  WARN: could not list {eng_type} for {from_type}/{from_id}: {exc}")
            engagements[eng_type] = []
            continue
        for eid in ids[:MAX_ENGAGEMENTS_PER_TYPE]:
            try:
                records.append(hs.get_engagement(eng_type, eid))
            except Exception as exc:  # noqa: BLE001
                print(f"  WARN: skipped {eng_type} {eid}: {exc}")
        engagements[eng_type] = records
    return engagements


def fetch_hubspot(url: str) -> HubSpotBundle:
    portal_id, object_type, record_id = parse_record_url(url)
    print(f"HubSpot: portal={portal_id} type={object_type} id={record_id}")

    hs = HubSpotClient()

    if object_type == "deals":
        primary = hs.get_deal(record_id)
        company_ids = _associated_ids(primary, "companies")
        contact_ids = _associated_ids(primary, "contacts")
        company = hs.get_company(company_ids[0]) if company_ids else None
    elif object_type == "companies":
        primary = hs.get_company(record_id)
        company = primary
        contact_ids = _associated_ids(primary, "contacts")
    elif object_type == "contacts":
        primary = hs.get_contact(record_id)
        company_ids = _associated_ids(primary, "companies")
        company = hs.get_company(company_ids[0]) if company_ids else None
        # One contact means just this contact — list_associations not needed.
        contact_ids = [record_id]
    else:
        raise ValueError(f"Unsupported object_type from URL: {object_type}")

    contacts: List[Any] = []
    if contact_ids:
        batch = hs.batch_read_contacts(contact_ids)
        contacts = batch.results

    engagements = _fetch_engagements(hs, object_type, record_id)

    return HubSpotBundle(
        portal_id=portal_id,
        primary_object_type=object_type,
        primary=primary,
        company=company,
        contacts=contacts,
        engagements=engagements,
    )


# ---------------------------------------------------------------------------
# Phase 3 — Fireflies match
# ---------------------------------------------------------------------------


def fetch_fireflies(
    emails: List[str], days: int = FIREFLIES_LOOKBACK_DAYS
) -> List[Dict[str, Any]]:
    if not emails:
        print("Fireflies: no contact emails to match against — skipping")
        return []
    print(f"Fireflies: matching against {len(emails)} contact email(s), last {days}d")
    ff = FirefliesClient()
    recent = ff.list_recent(days=days, limit=25)
    matches = ff.filter_by_emails(recent, emails)
    full: List[Dict[str, Any]] = []
    for summary in matches:
        tid = summary.get("id")
        if not tid:
            continue
        try:
            full.append(ff.get_transcript(tid))
        except Exception as exc:  # noqa: BLE001
            print(f"  WARN: could not fetch transcript {tid}: {exc}")
    print(f"Fireflies: matched {len(full)} transcript(s)")
    return full


# ---------------------------------------------------------------------------
# Phase 4 — folder scaffold
# ---------------------------------------------------------------------------


_UNSAFE_FS_CHARS = re.compile(r'[/\\:*?"<>|]')


def _safe_folder_name(raw: str) -> str:
    cleaned = _UNSAFE_FS_CHARS.sub("", raw).strip()
    return cleaned or "Unknown Client"


def _fmt_property(props: Dict[str, Optional[str]], key: str) -> str:
    val = props.get(key)
    return val if val else "_(not set)_"


def _unix_ms_to_iso(ts: Any) -> str:
    try:
        ms = int(ts)
    except (TypeError, ValueError):
        return str(ts)
    seconds = ms / 1000 if ms > 1e12 else ms
    try:
        return datetime.utcfromtimestamp(seconds).strftime("%Y-%m-%d %H:%M UTC")
    except (OverflowError, OSError, ValueError):
        return str(ts)


def _render_discovery(
    hs: HubSpotBundle, ff: List[Dict[str, Any]], today: str
) -> str:
    lines: List[str] = []
    lines.append(f"# {hs.client_name} — Discovery Notes")
    lines.append("")
    lines.append(
        f"*Auto-generated by scripts/intake.py on {today}.*  "
        f"*Primary HubSpot record: {hs.primary_object_type[:-1]} {hs.primary.id} "
        f"in portal {hs.portal_id}.*"
    )
    lines.append("")

    # Company section
    if hs.company is not None:
        cp = hs.company.properties
        lines.append("## Company")
        lines.append("")
        lines.append(f"- **Name:** {_fmt_property(cp, 'name')}")
        lines.append(f"- **Industry:** {_fmt_property(cp, 'industry')}")
        lines.append(f"- **Size (employees):** {_fmt_property(cp, 'numberofemployees')}")
        lines.append(f"- **Annual revenue:** {_fmt_property(cp, 'annualrevenue')}")
        lines.append(f"- **Website:** {_fmt_property(cp, 'website')}")
        lines.append(f"- **Lifecycle stage:** {_fmt_property(cp, 'lifecyclestage')}")
        city = cp.get("city") or ""
        state = cp.get("state") or ""
        location = ", ".join(x for x in (city, state) if x) or "_(not set)_"
        lines.append(f"- **Location:** {location}")
        desc = cp.get("description")
        if desc:
            lines.append("")
            lines.append(f"**Description:** {desc}")
        lines.append("")

    # Deal section (only when we came in via a deal URL)
    if hs.primary_object_type == "deals":
        dp = hs.primary.properties
        lines.append("## Deal")
        lines.append("")
        lines.append(f"- **Deal name:** {_fmt_property(dp, 'dealname')}")
        lines.append(f"- **Amount:** {_fmt_property(dp, 'amount')}")
        lines.append(f"- **Stage:** {_fmt_property(dp, 'dealstage')}")
        lines.append(f"- **Close date:** {_fmt_property(dp, 'closedate')}")
        lines.append(f"- **Pipeline:** {_fmt_property(dp, 'pipeline')}")
        desc = dp.get("description")
        if desc:
            lines.append("")
            lines.append(f"**Deal description:** {desc}")
        lines.append("")

    # Contacts section
    lines.append(f"## Contacts ({len(hs.contacts)})")
    lines.append("")
    if hs.contacts:
        for c in hs.contacts:
            p = c.properties
            first = p.get("firstname") or ""
            last = p.get("lastname") or ""
            name = (first + " " + last).strip() or "_(unnamed)_"
            title = p.get("jobtitle") or ""
            email = p.get("email") or ""
            phone = p.get("phone") or p.get("mobilephone") or ""
            bits = [f"**{name}**"]
            if title:
                bits.append(title)
            if email:
                bits.append(email)
            if phone:
                bits.append(phone)
            lines.append(f"- {' — '.join(bits)}")
    else:
        lines.append("_No associated contacts found._")
    lines.append("")

    # Engagements summary
    lines.append("## HubSpot Engagements")
    lines.append("")
    any_engagements = False
    for eng_type, records in hs.engagements.items():
        if not records:
            continue
        any_engagements = True
        lines.append(f"### {eng_type.capitalize()} ({len(records)})")
        lines.append("")
        for rec in records:
            rp = rec.properties
            ts = rp.get("hs_timestamp") or rp.get("hs_meeting_start_time")
            body_key = {
                "notes": "hs_note_body",
                "calls": "hs_call_body",
                "meetings": "hs_meeting_body",
                "emails": "hs_email_text",
            }[eng_type]
            title_key = {
                "notes": None,
                "calls": "hs_call_title",
                "meetings": "hs_meeting_title",
                "emails": "hs_email_subject",
            }[eng_type]
            title = rp.get(title_key) if title_key else None
            body = rp.get(body_key) or ""
            header_parts = []
            if ts:
                header_parts.append(_unix_ms_to_iso(ts))
            if title:
                header_parts.append(title)
            header = " — ".join(header_parts) if header_parts else f"(id {rec.id})"
            lines.append(f"**{header}**")
            lines.append("")
            # Strip HTML crudely; full fidelity lives in HubSpot.
            clean = re.sub(r"<[^>]+>", "", body).strip()
            lines.append(clean if clean else "_(empty)_")
            lines.append("")
    if not any_engagements:
        lines.append("_No engagements (notes / calls / meetings / emails) on the record._")
        lines.append("")

    # Fireflies summaries (not full transcripts — those go in recording.md)
    lines.append(f"## Fireflies Transcripts ({len(ff)})")
    lines.append("")
    if ff:
        for t in ff:
            title = t.get("title") or f"(transcript {t.get('id')})"
            date_raw = t.get("date")
            date_str = _unix_ms_to_iso(date_raw) if date_raw else ""
            lines.append(f"### {title}")
            if date_str:
                lines.append(f"*{date_str}*")
            summary = t.get("summary") or {}
            overview = summary.get("overview")
            action_items = summary.get("action_items")
            if overview:
                lines.append("")
                lines.append("**Overview**")
                lines.append("")
                lines.append(overview if isinstance(overview, str) else str(overview))
            if action_items:
                lines.append("")
                lines.append("**Action Items**")
                lines.append("")
                if isinstance(action_items, list):
                    for item in action_items:
                        lines.append(f"- {item}")
                else:
                    lines.append(str(action_items))
            lines.append("")
    else:
        lines.append("_No Fireflies transcripts matched contact emails in the lookback window._")
        lines.append("")

    return "\n".join(lines)


def _render_recording(ff: List[Dict[str, Any]]) -> str:
    lines: List[str] = []
    lines.append("# Meeting Recordings — Full Transcripts")
    lines.append("")
    if not ff:
        lines.append("_No transcripts matched. Add participants in HubSpot contacts or "
                     "verify Fireflies attendance._")
        return "\n".join(lines)

    for t in ff:
        title = t.get("title") or f"(transcript {t.get('id')})"
        date_str = _unix_ms_to_iso(t.get("date")) if t.get("date") else ""
        lines.append(f"## {title}")
        if date_str:
            lines.append(f"*{date_str}*")
        participants = t.get("participants") or []
        if participants:
            lines.append(f"*Participants: {', '.join(participants)}*")
        lines.append("")
        sentences = t.get("sentences") or []
        if not sentences:
            lines.append("_(transcript body empty — check Fireflies permissions)_")
            lines.append("")
            continue
        last_speaker: Optional[str] = None
        for s in sentences:
            speaker = s.get("speaker_name") or "Unknown"
            text = s.get("text") or ""
            if speaker != last_speaker:
                lines.append("")
                lines.append(f"**{speaker}:** {text}")
                last_speaker = speaker
            else:
                lines.append(text)
        lines.append("")

    return "\n".join(lines)


def _stamp_template(template_path: Path, replacements: Dict[str, str]) -> str:
    text = template_path.read_text(encoding="utf-8")
    for key, val in replacements.items():
        text = text.replace(key, val)
    return text


def scaffold_folder(
    hs: HubSpotBundle,
    ff: List[Dict[str, Any]],
    *,
    dry_run: bool,
    override_name: Optional[str],
    force: bool,
) -> Path:
    today = datetime.now().strftime("%Y-%m-%d")
    raw_name = override_name or hs.client_name
    folder_name = _safe_folder_name(raw_name)
    folder = REPO_ROOT / folder_name

    files: List[Tuple[Path, str]] = []
    files.append(
        (folder / f"{folder_name} Discovery {today}.md", _render_discovery(hs, ff, today))
    )
    files.append((folder / f"{folder_name} Meeting Recording.md", _render_recording(ff)))
    files.append(
        (
            folder / f"{folder_name}_decisions.md",
            _stamp_template(
                TEMPLATES_DIR / "decisions-template.md",
                {"{Client Name}": folder_name, "{Name}": "Kyle", "{Date}": today},
            ),
        )
    )
    files.append(
        (
            folder / "STATE.md",
            _stamp_template(
                TEMPLATES_DIR / "client-state-template.md",
                {"{Client Name}": folder_name, "YYYY-MM-DD": today},
            ),
        )
    )

    print(f"Folder: {folder}")
    if dry_run:
        print("[dry-run] Would create the following files:")
        for path, body in files:
            size = len(body.encode("utf-8"))
            print(f"  {path.relative_to(REPO_ROOT)}  ({size:,} bytes)")
        return folder

    if folder.exists() and not force:
        existing = sorted(p.name for p in folder.iterdir())
        if existing:
            raise SystemExit(
                f"Folder {folder} already exists with files: {existing}. "
                "Re-run with --force to overwrite."
            )

    folder.mkdir(parents=True, exist_ok=True)
    for path, body in files:
        path.write_text(body, encoding="utf-8")
        print(f"  wrote {path.relative_to(REPO_ROOT)}")
    return folder


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="intake",
        description="Scaffold a scoping folder from a HubSpot record URL.",
    )
    p.add_argument(
        "--test-only",
        action="store_true",
        help="Verify both API tokens work and exit. No fetch, no writes.",
    )
    p.add_argument("--url", help="HubSpot record URL (deal / company / contact).")
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch data and print what would be created, but write nothing.",
    )
    p.add_argument(
        "--client-name",
        help="Override the folder name (defaults to HubSpot company name).",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Overwrite files if the target folder already exists.",
    )
    return p


def main(argv: Optional[List[str]] = None) -> int:
    args = _build_parser().parse_args(argv)

    if args.test_only:
        return _smoke_test()

    if not args.url:
        print("error: --url is required (or use --test-only)", file=sys.stderr)
        return 2

    try:
        hs = fetch_hubspot(args.url)
    except Exception as exc:  # noqa: BLE001
        print(f"HubSpot fetch failed: {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1

    emails = hs.contact_emails
    try:
        ff = fetch_fireflies(emails)
    except Exception as exc:  # noqa: BLE001
        print(f"Fireflies fetch failed (continuing): {exc}", file=sys.stderr)
        ff = []

    folder = scaffold_folder(
        hs, ff, dry_run=args.dry_run, override_name=args.client_name, force=args.force
    )

    print("")
    print("Summary")
    print(f"  Client:     {hs.client_name}")
    print(f"  Contacts:   {len(hs.contacts)}")
    for eng_type, records in hs.engagements.items():
        print(f"  {eng_type.capitalize():<10}  {len(records)}")
    print(f"  Transcripts: {len(ff)}")
    print(f"  Folder:     {folder}")
    print("")
    print("Next: read calibration/calibration.md, then run the scoping skill.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
