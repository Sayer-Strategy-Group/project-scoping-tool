"""HubSpot CRM v3 client — read-only, intake-focused.

Companion to `fireflies_client.py`. One narrow job: fetch a HubSpot record
(company / deal / contact) plus its associations and related engagement
records (notes / calls / meetings / emails), parsed into pydantic v2 models
so downstream intake code never touches raw dicts.

Auth via `keychain.get_secret("HUBSPOT_API_KEY")` (Private App token).

Scope is deliberately narrow — no writes, no search, no schema/property
metadata, no batch create/update. See `hubspot-schema-notes.md` for the
endpoint list and field-by-field notes.

Python 3.9 compatible: uses `typing.Optional / List / Dict / Tuple`, never
pipe-union syntax or subscripted builtins.
"""

import re
from typing import Any, Dict, Iterator, List, Optional, Sequence, Tuple

import requests

from hubspot_models import (
    BatchResponseSimplePublicObject,
    CollectionResponseAssociatedId,
    CollectionResponsePublicOwnerForwardPaging,
    SimplePublicObjectWithAssociations,
)
from keychain import get_secret


BASE_URL = "https://api.hubapi.com"
DEFAULT_TIMEOUT = 30


# Default property sets per object. Callers can override by passing an explicit
# `properties` list to any fetch method. These are the fields intake actually
# needs to scaffold a scoping folder.
DEFAULT_COMPANY_PROPERTIES: Tuple[str, ...] = (
    "name",
    "domain",
    "industry",
    "numberofemployees",
    "annualrevenue",
    "phone",
    "website",
    "lifecyclestage",
    "description",
    "city",
    "state",
    "country",
    "hs_lead_status",
    "createdate",
)

DEFAULT_DEAL_PROPERTIES: Tuple[str, ...] = (
    "dealname",
    "amount",
    "pipeline",
    "dealstage",
    "dealtype",
    "closedate",
    "hs_deal_stage_probability",
    "description",
    "hubspot_owner_id",
    "createdate",
)

DEFAULT_CONTACT_PROPERTIES: Tuple[str, ...] = (
    "firstname",
    "lastname",
    "email",
    "jobtitle",
    "phone",
    "mobilephone",
    "company",
    "hs_lead_status",
    "lifecyclestage",
    "hubspot_owner_id",
)

DEFAULT_NOTE_PROPERTIES: Tuple[str, ...] = (
    "hs_note_body",
    "hs_timestamp",
    "hubspot_owner_id",
)

DEFAULT_CALL_PROPERTIES: Tuple[str, ...] = (
    "hs_call_title",
    "hs_call_body",
    "hs_call_duration",
    "hs_timestamp",
    "hubspot_owner_id",
)

DEFAULT_MEETING_PROPERTIES: Tuple[str, ...] = (
    "hs_meeting_title",
    "hs_meeting_body",
    "hs_meeting_start_time",
    "hs_meeting_end_time",
    "hubspot_owner_id",
)

DEFAULT_EMAIL_PROPERTIES: Tuple[str, ...] = (
    "hs_email_subject",
    "hs_email_text",
    "hs_timestamp",
    "hubspot_owner_id",
)


_ENGAGEMENT_DEFAULTS: Dict[str, Tuple[str, ...]] = {
    "notes": DEFAULT_NOTE_PROPERTIES,
    "calls": DEFAULT_CALL_PROPERTIES,
    "meetings": DEFAULT_MEETING_PROPERTIES,
    "emails": DEFAULT_EMAIL_PROPERTIES,
}

_VALID_ENGAGEMENT_TYPES = frozenset(_ENGAGEMENT_DEFAULTS.keys())


# ---------------------------------------------------------------------------
# URL parser
# ---------------------------------------------------------------------------


# objectTypeId -> plural object-type name used in `/crm/v3/objects/{objectType}`
_OBJECT_TYPE_ID_TO_NAME: Dict[str, str] = {
    "0-1": "contacts",
    "0-2": "companies",
    "0-3": "deals",
}

# singular URL segment -> plural object-type name
_OBJECT_SINGULAR_TO_PLURAL: Dict[str, str] = {
    "contact": "contacts",
    "company": "companies",
    "deal": "deals",
}

# Shape 1: /contacts/{portal}/record/{objectTypeId}/{recordId}
_URL_SHAPE_RECORD = re.compile(
    r"^https?://app(?:-[a-z0-9]+)?\.hubspot\.com/contacts/(\d+)/record/(0-\d+)/(\d+)/?(?:\?.*)?$"
)

# Shape 2: /contacts/{portal}/{singular}/{recordId}
_URL_SHAPE_LEGACY = re.compile(
    r"^https?://app(?:-[a-z0-9]+)?\.hubspot\.com/contacts/(\d+)/(contact|company|deal)/(\d+)/?(?:\?.*)?$"
)


def parse_record_url(url: str) -> Tuple[str, str, str]:
    """Parse a HubSpot record URL into ``(portal_id, object_type, record_id)``.

    `object_type` is returned as the plural form used by the v3 API path
    (`"contacts"`, `"companies"`, `"deals"`), regardless of which URL shape
    the caller supplied.

    Raises ``ValueError`` if the URL doesn't match either of the two supported
    HubSpot record-URL shapes.
    """
    if not isinstance(url, str) or not url:
        raise ValueError("HubSpot record URL must be a non-empty string")

    stripped = url.strip()

    m = _URL_SHAPE_RECORD.match(stripped)
    if m:
        portal_id, object_type_id, record_id = m.group(1), m.group(2), m.group(3)
        try:
            object_type = _OBJECT_TYPE_ID_TO_NAME[object_type_id]
        except KeyError:
            raise ValueError(
                f"Unsupported HubSpot objectTypeId {object_type_id!r} in URL "
                f"{url!r}. Expected one of {sorted(_OBJECT_TYPE_ID_TO_NAME)} "
                f"(contact / company / deal)."
            )
        return portal_id, object_type, record_id

    m = _URL_SHAPE_LEGACY.match(stripped)
    if m:
        portal_id, singular, record_id = m.group(1), m.group(2), m.group(3)
        return portal_id, _OBJECT_SINGULAR_TO_PLURAL[singular], record_id

    raise ValueError(
        "HubSpot URL did not match either supported shape. Expected:\n"
        "  https://app[-region].hubspot.com/contacts/{portalId}/record/{0-1|0-2|0-3}/{id}\n"
        "  https://app[-region].hubspot.com/contacts/{portalId}/{contact|company|deal}/{id}\n"
        f"Got: {url!r}"
    )


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------


class HubSpotClient:
    """Typed, read-only HubSpot CRM v3 client for intake."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.api_key = api_key or get_secret("HUBSPOT_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    # -- low level ----------------------------------------------------------

    def _get(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        resp = requests.get(
            f"{self.base_url}{path}",
            headers=self.headers,
            params=params,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def _post(self, path: str, json_body: Dict[str, Any]) -> Dict[str, Any]:
        resp = requests.post(
            f"{self.base_url}{path}",
            headers=self.headers,
            json=json_body,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def _coerce_properties(
        properties: Optional[Sequence[str]], default: Sequence[str]
    ) -> str:
        """Join the `properties` query arg into the comma-form HubSpot expects."""
        vals = properties if properties is not None else default
        return ",".join(vals)

    # -- ping --------------------------------------------------------------

    def ping(self) -> CollectionResponsePublicOwnerForwardPaging:
        """Verify auth with the cheapest call that exercises a bearer token.

        ``GET /crm/v3/owners?limit=1``. Always returns something for a valid
        Private App with `crm.objects.owners.read` scope; raises on 401/403.
        """
        payload = self._get("/crm/v3/owners", params={"limit": 1})
        return CollectionResponsePublicOwnerForwardPaging.model_validate(payload)

    # -- single-object fetchers -------------------------------------------

    def _get_object(
        self,
        object_type: str,
        object_id: str,
        properties: Optional[Sequence[str]],
        default_properties: Sequence[str],
        associations: Optional[Sequence[str]] = None,
    ) -> SimplePublicObjectWithAssociations:
        params: Dict[str, Any] = {
            "properties": self._coerce_properties(properties, default_properties),
            "archived": "false",
        }
        if associations:
            params["associations"] = ",".join(associations)
        payload = self._get(
            f"/crm/v3/objects/{object_type}/{object_id}", params=params
        )
        return SimplePublicObjectWithAssociations.model_validate(payload)

    def get_company(
        self,
        company_id: str,
        properties: Optional[Sequence[str]] = None,
        associations: Optional[Sequence[str]] = ("contacts", "deals"),
    ) -> SimplePublicObjectWithAssociations:
        return self._get_object(
            "companies",
            company_id,
            properties,
            DEFAULT_COMPANY_PROPERTIES,
            associations,
        )

    def get_deal(
        self,
        deal_id: str,
        properties: Optional[Sequence[str]] = None,
        associations: Optional[Sequence[str]] = ("contacts", "companies"),
    ) -> SimplePublicObjectWithAssociations:
        return self._get_object(
            "deals",
            deal_id,
            properties,
            DEFAULT_DEAL_PROPERTIES,
            associations,
        )

    def get_contact(
        self,
        contact_id: str,
        properties: Optional[Sequence[str]] = None,
        associations: Optional[Sequence[str]] = ("companies", "deals"),
    ) -> SimplePublicObjectWithAssociations:
        return self._get_object(
            "contacts",
            contact_id,
            properties,
            DEFAULT_CONTACT_PROPERTIES,
            associations,
        )

    # -- batch-read contacts ----------------------------------------------

    def batch_read_contacts(
        self,
        ids: Sequence[str],
        properties: Optional[Sequence[str]] = None,
    ) -> BatchResponseSimplePublicObject:
        """POST /crm/v3/objects/contacts/batch/read — fetch many contacts at once.

        `ids` are HubSpot internal contact IDs (strings). Max 100 per call per
        HubSpot's batch limits; this client does not split larger lists.
        """
        body: Dict[str, Any] = {
            "properties": list(
                properties if properties is not None else DEFAULT_CONTACT_PROPERTIES
            ),
            "propertiesWithHistory": [],
            "inputs": [{"id": str(i)} for i in ids],
        }
        payload = self._post("/crm/v3/objects/contacts/batch/read", body)
        return BatchResponseSimplePublicObject.model_validate(payload)

    # -- engagement fetchers ----------------------------------------------

    def get_engagement(
        self,
        engagement_type: str,
        engagement_id: str,
        properties: Optional[Sequence[str]] = None,
        associations: Optional[Sequence[str]] = None,
    ) -> SimplePublicObjectWithAssociations:
        """GET a single engagement record: notes / calls / meetings / emails."""
        if engagement_type not in _VALID_ENGAGEMENT_TYPES:
            raise ValueError(
                f"engagement_type must be one of "
                f"{sorted(_VALID_ENGAGEMENT_TYPES)}; got {engagement_type!r}"
            )
        defaults = _ENGAGEMENT_DEFAULTS[engagement_type]
        return self._get_object(
            engagement_type, engagement_id, properties, defaults, associations
        )

    # -- associations -----------------------------------------------------

    def list_associations(
        self,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
    ) -> CollectionResponseAssociatedId:
        """GET /crm/v3/objects/{from}/{id}/associations/{to}.

        Returns the paged list of IDs (and association type labels) on the
        other side of the association. Used to walk deal -> contacts, company
        -> deals, contact -> engagements (notes / calls / meetings / emails).

        This is the legacy v3 associations endpoint. HubSpot is migrating
        callers to the v4 API; the v3 path still responds in practice but is
        no longer documented in the latest per-object specs. If a future
        deprecation breaks this, the fix is to switch to
        `/crm/v4/objects/{from}/{id}/associations/{to}` which returns the
        same `results` shape but with a richer `type` structure.
        """
        payload = self._get(
            f"/crm/v3/objects/{from_object_type}/{from_object_id}"
            f"/associations/{to_object_type}"
        )
        return CollectionResponseAssociatedId.model_validate(payload)

    def iter_associations(
        self,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
    ) -> Iterator[str]:
        """Yield every associated ID, walking `paging.next.after` cursors."""
        after: Optional[str] = None
        while True:
            params: Dict[str, Any] = {}
            if after is not None:
                params["after"] = after
            payload = self._get(
                f"/crm/v3/objects/{from_object_type}/{from_object_id}"
                f"/associations/{to_object_type}",
                params=params or None,
            )
            page = CollectionResponseAssociatedId.model_validate(payload)
            for assoc in page.results:
                yield assoc.id
            if page.paging is None or page.paging.next is None:
                return
            after = page.paging.next.after


__all__ = [
    "HubSpotClient",
    "parse_record_url",
    "DEFAULT_COMPANY_PROPERTIES",
    "DEFAULT_DEAL_PROPERTIES",
    "DEFAULT_CONTACT_PROPERTIES",
    "DEFAULT_NOTE_PROPERTIES",
    "DEFAULT_CALL_PROPERTIES",
    "DEFAULT_MEETING_PROPERTIES",
    "DEFAULT_EMAIL_PROPERTIES",
]
