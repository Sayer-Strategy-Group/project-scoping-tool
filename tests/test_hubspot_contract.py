"""Live contract tests for the HubSpot CRM v3 client.

Pytest entry: ``pytest tests/test_hubspot_contract.py -v``

Dependencies (install into the same Python that runs pytest):
    pip install 'pydantic>=2,<3' pytest requests

Auth: the live tests need a HubSpot Private App token available under
``HUBSPOT_API_KEY`` — either in the macOS Keychain, an env var, or the
repo-local ``.env``. When the token is unavailable the live tests are
skipped (with a clear message); the URL-parser tests still run.

Required Private App scopes for this suite:
    crm.objects.owners.read
    crm.objects.companies.read
    crm.objects.contacts.read
    crm.objects.deals.read
    crm.schemas.custom.read  (only if hitting custom associations)

Tests are fixture-independent: each test fetches whatever the portal
currently has rather than hardcoded IDs. The only precondition is that the
portal has at least one company and one deal, which every live HubSpot
portal does.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

import pytest
import requests

from hubspot_client import HubSpotClient, parse_record_url
from hubspot_models import (
    BatchResponseSimplePublicObject,
    CollectionResponseAssociatedId,
    CollectionResponsePublicOwnerForwardPaging,
    SimplePublicObjectWithAssociations,
)


# ---------------------------------------------------------------------------
# Auth detection
# ---------------------------------------------------------------------------


def _token_available() -> bool:
    try:
        from keychain import get_secret  # noqa: WPS433

        get_secret("HUBSPOT_API_KEY")
        return True
    except Exception:  # noqa: BLE001 — any failure == token unavailable
        return False


_HAS_TOKEN = _token_available()
_SKIP_REASON = (
    "HUBSPOT_API_KEY not available (checked macOS Keychain -> env -> .env -> "
    "1Password op://Shared/HUBSPOT_API_KEY/credential). Sign in to the Sayer "
    "1Password account (op CLI) or add a personal override with: "
    "security add-generic-password -a 'harbuckconsulting' "
    "-s 'HUBSPOT_API_KEY' -w '<token>'"
)

requires_token = pytest.mark.skipif(not _HAS_TOKEN, reason=_SKIP_REASON)


# ---------------------------------------------------------------------------
# Shared client fixture + helpers to find a real record to fetch
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def client() -> HubSpotClient:
    return HubSpotClient()


def _first_record_id(
    client: HubSpotClient, object_type: str
) -> Optional[str]:
    """Return the first live record ID of `object_type`, or None if empty."""
    resp = requests.get(
        f"{client.base_url}/crm/v3/objects/{object_type}",
        headers=client.headers,
        params={"limit": 1, "archived": "false"},
        timeout=client.timeout,
    )
    resp.raise_for_status()
    payload: Dict[str, Any] = resp.json()
    results = payload.get("results") or []
    if not results:
        return None
    return results[0]["id"]


# ---------------------------------------------------------------------------
# URL parser (runs with or without a token)
# ---------------------------------------------------------------------------


class TestParseRecordUrl:
    def test_record_shape_contact(self) -> None:
        url = "https://app.hubspot.com/contacts/12345/record/0-1/6789"
        assert parse_record_url(url) == ("12345", "contacts", "6789")

    def test_record_shape_company(self) -> None:
        url = "https://app.hubspot.com/contacts/12345/record/0-2/1001"
        assert parse_record_url(url) == ("12345", "companies", "1001")

    def test_record_shape_deal(self) -> None:
        url = "https://app.hubspot.com/contacts/12345/record/0-3/2002"
        assert parse_record_url(url) == ("12345", "deals", "2002")

    def test_legacy_shape_company(self) -> None:
        url = "https://app.hubspot.com/contacts/999/company/555"
        assert parse_record_url(url) == ("999", "companies", "555")

    def test_legacy_shape_deal(self) -> None:
        url = "https://app.hubspot.com/contacts/999/deal/42"
        assert parse_record_url(url) == ("999", "deals", "42")

    def test_legacy_shape_contact(self) -> None:
        url = "https://app.hubspot.com/contacts/999/contact/42"
        assert parse_record_url(url) == ("999", "contacts", "42")

    def test_trailing_slash_tolerated(self) -> None:
        url = "https://app.hubspot.com/contacts/12345/record/0-2/1001/"
        assert parse_record_url(url) == ("12345", "companies", "1001")

    def test_query_string_tolerated(self) -> None:
        url = "https://app.hubspot.com/contacts/12345/record/0-2/1001?foo=bar"
        assert parse_record_url(url) == ("12345", "companies", "1001")

    def test_unknown_shape_raises(self) -> None:
        with pytest.raises(ValueError, match="did not match"):
            parse_record_url("https://app.hubspot.com/contacts/12345/settings/1")

    def test_empty_string_raises(self) -> None:
        with pytest.raises(ValueError):
            parse_record_url("")

    def test_unsupported_object_type_id_raises(self) -> None:
        # 0-5 is tickets — not supported by intake.
        url = "https://app.hubspot.com/contacts/12345/record/0-5/9"
        with pytest.raises(ValueError, match="objectTypeId"):
            parse_record_url(url)


# ---------------------------------------------------------------------------
# Live API contract tests
# ---------------------------------------------------------------------------


@pytest.mark.live
@requires_token
class TestLiveContract:
    def test_ping_returns_owner_collection(
        self, client: HubSpotClient
    ) -> None:
        resp = client.ping()
        assert isinstance(resp, CollectionResponsePublicOwnerForwardPaging)
        # A working token on a live portal should return at least the
        # authenticated user. Even a brand-new portal has one owner.
        assert len(resp.results) >= 1
        first = resp.results[0]
        assert first.id  # non-empty str
        assert first.type in {"PERSON", "QUEUE"}

    def test_get_company_returns_typed_model(
        self, client: HubSpotClient
    ) -> None:
        company_id = _first_record_id(client, "companies")
        if company_id is None:
            pytest.skip("portal has no companies")
        resp = client.get_company(company_id)
        assert isinstance(resp, SimplePublicObjectWithAssociations)
        assert resp.id == company_id
        # Properties always dict[str, Optional[str]].
        assert isinstance(resp.properties, dict)
        for k, v in resp.properties.items():
            assert isinstance(k, str)
            assert v is None or isinstance(v, str)
        # Associations envelope, when present, is dict[str, CollectionResponseAssociatedId].
        if resp.associations is not None:
            for k, coll in resp.associations.items():
                assert isinstance(k, str)
                assert isinstance(coll, CollectionResponseAssociatedId)

    def test_get_deal_returns_typed_model(
        self, client: HubSpotClient
    ) -> None:
        deal_id = _first_record_id(client, "deals")
        if deal_id is None:
            pytest.skip("portal has no deals")
        resp = client.get_deal(deal_id)
        assert isinstance(resp, SimplePublicObjectWithAssociations)
        assert resp.id == deal_id
        assert isinstance(resp.properties, dict)

    def test_association_walk(self, client: HubSpotClient) -> None:
        """Walk company -> contacts. Verifies list_associations envelope."""
        # Find a company that has at least one associated contact.
        # Ask for associations up-front on get_company so we don't need to
        # probe every company in the portal.
        list_resp = requests.get(
            f"{client.base_url}/crm/v3/objects/companies",
            headers=client.headers,
            params={
                "limit": 10,
                "associations": "contacts",
                "archived": "false",
            },
            timeout=client.timeout,
        )
        list_resp.raise_for_status()
        candidates = list_resp.json().get("results") or []
        target: Optional[str] = None
        for c in candidates:
            assoc = (c.get("associations") or {}).get("contacts") or {}
            if assoc.get("results"):
                target = c["id"]
                break
        if target is None:
            pytest.skip(
                "no company in first 10 has an associated contact — "
                "can't exercise association walk on this portal"
            )
        resp = client.list_associations("companies", target, "contacts")
        assert isinstance(resp, CollectionResponseAssociatedId)
        assert len(resp.results) >= 1
        first = resp.results[0]
        assert first.id
        assert first.type  # label like "company_to_contact"

    def test_batch_read_contacts(self, client: HubSpotClient) -> None:
        contact_id = _first_record_id(client, "contacts")
        if contact_id is None:
            pytest.skip("portal has no contacts")
        resp = client.batch_read_contacts([contact_id])
        assert isinstance(resp, BatchResponseSimplePublicObject)
        assert resp.status in {"PENDING", "PROCESSING", "CANCELED", "COMPLETE"}
        assert len(resp.results) == 1
        assert resp.results[0].id == contact_id
