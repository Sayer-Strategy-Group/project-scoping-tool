"""Fireflies GraphQL client.

Ported from /Users/harbuckconsulting/projects/AIVA/kh_ccStudio_migration/
scripts/integrations/fireflies/client.py with two adaptations:

1. Credentials load via Keychain (keychain.get_secret) instead of env/file.
2. Type hints use typing.Optional/Dict/List for Python 3.9 compatibility.

Single endpoint: https://api.fireflies.ai/graphql
Auth: Bearer token (API key).
"""

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

import requests

from keychain import get_secret


API_URL = "https://api.fireflies.ai/graphql"
DEFAULT_TIMEOUT = 30


class FirefliesClient:
    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or get_secret("FIREFLIES_API_KEY")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _query(
        self, query: str, variables: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {"query": query}
        if variables:
            payload["variables"] = variables

        resp = requests.post(
            API_URL, json=payload, headers=self.headers, timeout=DEFAULT_TIMEOUT
        )
        resp.raise_for_status()
        data = resp.json()

        if "errors" in data:
            raise RuntimeError(f"Fireflies API error: {data['errors']}")

        return data.get("data", {})

    def ping(self) -> Dict[str, Any]:
        """Minimal query to verify token validity. Returns authenticated user info."""
        query = """
        query Ping {
            user {
                user_id
                email
                name
            }
        }
        """
        return self._query(query).get("user") or {}

    def list_recent(self, days: int = 90, limit: int = 20) -> List[Dict[str, Any]]:
        """List transcript summaries within the last `days`.

        Returns summary-only records (no full sentences). Pages until the
        oldest returned transcript falls outside the window, or there are no
        more pages.
        """
        since = datetime.now(timezone.utc) - timedelta(days=days)
        since_ts = int(since.timestamp())

        all_transcripts: List[Dict[str, Any]] = []
        skip = 0

        while True:
            query = """
            query ListTranscripts($limit: Int, $skip: Int) {
                transcripts(limit: $limit, skip: $skip) {
                    id
                    title
                    date
                    duration
                    participants
                    summary {
                        overview
                        action_items
                        keywords
                    }
                }
            }
            """
            data = self._query(query, {"limit": limit, "skip": skip})
            transcripts = data.get("transcripts", []) or []

            if not transcripts:
                break

            for t in transcripts:
                t_date = t.get("date", 0)
                if isinstance(t_date, str):
                    t_date = int(t_date)
                t_ts = t_date / 1000 if t_date > 1e12 else t_date

                if t_ts < since_ts:
                    return all_transcripts

                all_transcripts.append(t)

            if len(transcripts) < limit:
                break
            skip += limit

        return all_transcripts

    def get_transcript(self, transcript_id: str) -> Dict[str, Any]:
        """Fetch a full transcript (sentences + summary)."""
        query = """
        query GetTranscript($id: String!) {
            transcript(id: $id) {
                id
                title
                date
                duration
                participants
                sentences {
                    speaker_name
                    text
                    start_time
                    end_time
                }
                summary {
                    overview
                    action_items
                    keywords
                    outline
                }
            }
        }
        """
        data = self._query(query, {"id": transcript_id})
        return data.get("transcript") or {}

    def filter_by_emails(
        self, transcripts: List[Dict[str, Any]], emails: List[str]
    ) -> List[Dict[str, Any]]:
        """Return transcripts whose participants list contains any of `emails`.

        Match is case-insensitive. Participants are emails in Fireflies.
        """
        wanted = {e.lower() for e in emails if e}
        if not wanted:
            return []
        matches: List[Dict[str, Any]] = []
        for t in transcripts:
            participants = {p.lower() for p in (t.get("participants") or [])}
            if participants & wanted:
                matches.append(t)
        return matches
