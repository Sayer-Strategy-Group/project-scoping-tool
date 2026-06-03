"""Pydantic v2 response models for HubSpot CRM v3 intake endpoints.

Generated from the HubSpot public OpenAPI specs saved in `.api-specs/`. The
scope is read-only intake: fetch one company/deal/contact, batch-read
contacts, walk associations, and pull engagement records (notes, calls,
meetings, emails).

Design rules, per the spec and HubSpot's actual behavior:

- `properties` is always `Dict[str, Optional[str]]`. HubSpot returns every
  property value as a nullable string regardless of its underlying type
  (`annualrevenue` comes back as `"5000000"`, not `5000000`). Do not add
  per-field typed attributes here — let the caller coerce.
- `id` is a string on every object.
- `extra='ignore'` on every model so additive vendor changes don't crash us.
- Python 3.9 type hints (Optional/List/Dict/Tuple from `typing`).
"""

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


_CONFIG = ConfigDict(extra="ignore", populate_by_name=True)


# ---------------------------------------------------------------------------
# Paging
# ---------------------------------------------------------------------------


class NextPage(BaseModel):
    model_config = _CONFIG

    after: str
    link: Optional[str] = None


class PreviousPage(BaseModel):
    model_config = _CONFIG

    before: str
    link: Optional[str] = None


class Paging(BaseModel):
    model_config = _CONFIG

    next: Optional[NextPage] = None
    prev: Optional[PreviousPage] = None


class ForwardPaging(BaseModel):
    model_config = _CONFIG

    next: Optional[NextPage] = None


# ---------------------------------------------------------------------------
# Associations
# ---------------------------------------------------------------------------


class AssociatedId(BaseModel):
    model_config = _CONFIG

    id: str
    type: str


class CollectionResponseAssociatedId(BaseModel):
    """Envelope used for list-associations responses AND as the nested value
    inside `SimplePublicObjectWithAssociations.associations[<objectType>]`.
    """

    model_config = _CONFIG

    results: List[AssociatedId] = Field(default_factory=list)
    paging: Optional[Paging] = None


# ---------------------------------------------------------------------------
# CRM object shapes
# ---------------------------------------------------------------------------


class SimplePublicObject(BaseModel):
    """Top-level CRM object, no associations envelope.

    Returned inside `BatchResponseSimplePublicObject.results`.
    """

    model_config = _CONFIG

    id: str
    properties: Dict[str, Optional[str]] = Field(default_factory=dict)
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    archived: Optional[bool] = None
    archived_at: Optional[str] = Field(default=None, alias="archivedAt")


class SimplePublicObjectWithAssociations(BaseModel):
    """Single-object GET response (company, deal, contact, engagement).

    `associations` is a dict keyed by the *target* object type (e.g.
    "contacts", "companies") whose values are `CollectionResponseAssociatedId`.
    The key set is portal- and request-dependent, so we model it as a dict.
    """

    model_config = _CONFIG

    id: str
    properties: Dict[str, Optional[str]] = Field(default_factory=dict)
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    archived: Optional[bool] = None
    archived_at: Optional[str] = Field(default=None, alias="archivedAt")
    associations: Optional[Dict[str, CollectionResponseAssociatedId]] = None


# ---------------------------------------------------------------------------
# Batch read
# ---------------------------------------------------------------------------


class BatchResponseSimplePublicObject(BaseModel):
    """Envelope for `POST /crm/v3/objects/{object}/batch/read`."""

    model_config = _CONFIG

    status: str  # "PENDING" | "PROCESSING" | "CANCELED" | "COMPLETE"
    results: List[SimplePublicObject] = Field(default_factory=list)
    started_at: str = Field(alias="startedAt")
    completed_at: str = Field(alias="completedAt")
    requested_at: Optional[str] = Field(default=None, alias="requestedAt")


# ---------------------------------------------------------------------------
# Owners (used for ping and, if ever needed, owner lookup)
# ---------------------------------------------------------------------------


class PublicTeam(BaseModel):
    model_config = _CONFIG

    id: str
    name: Optional[str] = None
    primary: Optional[bool] = None


class PublicOwner(BaseModel):
    model_config = _CONFIG

    id: str
    type: str  # "PERSON" | "QUEUE"
    archived: bool
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    email: Optional[str] = None
    first_name: Optional[str] = Field(default=None, alias="firstName")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    user_id: Optional[int] = Field(default=None, alias="userId")
    user_id_including_inactive: Optional[int] = Field(
        default=None, alias="userIdIncludingInactive"
    )
    teams: Optional[List[PublicTeam]] = None


class CollectionResponsePublicOwnerForwardPaging(BaseModel):
    model_config = _CONFIG

    results: List[PublicOwner] = Field(default_factory=list)
    paging: Optional[ForwardPaging] = None


__all__ = [
    "AssociatedId",
    "BatchResponseSimplePublicObject",
    "CollectionResponseAssociatedId",
    "CollectionResponsePublicOwnerForwardPaging",
    "ForwardPaging",
    "NextPage",
    "Paging",
    "PreviousPage",
    "PublicOwner",
    "PublicTeam",
    "SimplePublicObject",
    "SimplePublicObjectWithAssociations",
]
