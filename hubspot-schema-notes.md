# HubSpot CRM v3 — Schema Notes (intake scope)

Spec sources: per-object JSON specs saved under `.api-specs/hubspot-*-v3.json`,
pulled from the HubSpot public API spec collection on GitHub
(https://github.com/HubSpot/HubSpot-public-api-spec-collection) using the
highest-numbered rollout for each object.

- `hubspot-contacts-v3.json` — rollout 107729
- `hubspot-companies-v3.json` — rollout 424
- `hubspot-deals-v3.json` — rollout 424 (note: path uses objectTypeId `0-3`)
- `hubspot-calls-v3.json` — rollout 424
- `hubspot-meetings-v3.json` — rollout 424
- `hubspot-notes-v3.json` — rollout 424
- `hubspot-emails-v3.json` — rollout 424
- `hubspot-crm-owners-v3.json` — rollout 146888
- `hubspot-associations-v3.json` — rollout 120891 (v3 legacy shape)

## Auth

HTTP Bearer token (HubSpot Private App access token). Sent as
`Authorization: Bearer <token>`. Loaded via `keychain.get_secret("HUBSPOT_API_KEY")`.

## Endpoints in scope

| Purpose            | Method | Path                                                         |
|--------------------|--------|--------------------------------------------------------------|
| Auth ping          | GET    | `/crm/v3/owners?limit=1`                                     |
| Fetch company      | GET    | `/crm/v3/objects/companies/{companyId}`                      |
| Fetch deal         | GET    | `/crm/v3/objects/deals/{dealId}` (spec uses `0-3`, but `deals` alias resolves) |
| Fetch contact      | GET    | `/crm/v3/objects/contacts/{contactId}`                       |
| Batch-read contacts| POST   | `/crm/v3/objects/contacts/batch/read`                        |
| List associations  | GET    | `/crm/v3/objects/{objectType}/{id}/associations/{toObjectType}` (legacy v3 — deprecated in spec but still live) |
| Fetch engagement   | GET    | `/crm/v3/objects/{notes\|calls\|meetings\|emails}/{id}`      |

### Query parameters (single-object GETs)

All four single-object GETs accept the same parameter set:

| name                    | in    | type             | notes                                                   |
|-------------------------|-------|------------------|---------------------------------------------------------|
| `properties`            | query | `array[string]`  | Serialized as comma-joined list.                        |
| `propertiesWithHistory` | query | `array[string]`  | Not used by this client (intake is point-in-time).      |
| `associations`          | query | `array[string]`  | Comma-joined list of object-type names to include.      |
| `archived`              | query | `boolean`        | Default `false`; not exposed — intake wants only live.  |
| `idProperty`            | query | `string`         | Not used; we always resolve by internal `id`.           |

No `enum` constraints on any of these (HubSpot portals define properties and
association labels freely, so allowed values are portal-specific).

### Batch read input shape

`POST /crm/v3/objects/contacts/batch/read` body
(`BatchReadInputSimplePublicObjectId`):

```json
{
  "properties": ["firstname", "lastname", "email"],
  "propertiesWithHistory": [],
  "inputs": [{"id": "12345"}, {"id": "67890"}]
}
```

All three top-level keys are `required` per spec. `propertiesWithHistory` must
be present — send `[]` when unused.

## Response envelope — the single most important fact

Every property value returned by HubSpot CRM v3 is a **string or null** —
never typed. `annualrevenue` comes back as `"5000000"`, not `5000000`. Dates
and timestamps are ISO 8601 strings (for top-level `createdAt` / `updatedAt`)
or Unix-millis-as-string (inside `properties.createdate`). `id` is a string on
every object.

Consequence for modeling: `properties` is `Dict[str, Optional[str]]`,
not a per-field typed struct. The client returns the raw dict and lets
callers coerce. This is spec-accurate — see
`components.schemas.SimplePublicObjectWithAssociations.properties.properties`
in any object spec: `additionalProperties: {type: string, nullable: true}`.

### `SimplePublicObjectWithAssociations` (single-object response)

- `id`: str (required)
- `properties`: `Dict[str, Optional[str]]` (required; keys are portal-dependent)
- `propertiesWithHistory`: optional; ignored by this client
- `createdAt`: str, ISO 8601 (required)
- `updatedAt`: str, ISO 8601 (required)
- `archived`: optional bool
- `archivedAt`: optional str, ISO 8601
- `associations`: optional `Dict[str, CollectionResponseAssociatedId]` — the
  **key** is the target object-type name (e.g., `"contacts"`,
  `"companies"`) and the **value** is `{ "results": [{id, type}], "paging"?: ... }`

### `CollectionResponseAssociatedId` (list-associations response AND the
nested value under `associations`)

- `results`: `List[AssociatedId]` (required)
  - `AssociatedId`: `{id: str, type: str}` — where `type` is the association
    label (e.g., `"contact_to_company"`, `"contact_to_deal"`).
- `paging`: optional `Paging` (cursor-based).

### `Paging` / `ForwardPaging`

- `next`: optional `{after: str, link?: str}` — `after` is the opaque cursor
  to pass back to the next call.
- `prev`: optional `{before: str, link?: str}` (only on bidirectional `Paging`).

### `BatchResponseSimplePublicObject` (batch-read response)

- `status`: enum `"PENDING" | "PROCESSING" | "CANCELED" | "COMPLETE"` (required)
- `results`: `List[SimplePublicObject]` (required — same shape as single-object
  response minus `associations`)
- `startedAt`, `completedAt`: str ISO 8601 (required)
- `requestedAt`: optional str
- `links`: optional `Dict[str, str]`
- Error-partial responses (`BatchResponseSimplePublicObjectWithErrors`) add a
  `numErrors` / `errors` array. Intake treats any top-level non-200 as fatal.

### `PublicOwner` (for ping)

- `id`: str (required)
- `email`, `firstName`, `lastName`: optional str
- `userId`, `userIdIncludingInactive`: optional int
- `type`: enum `"PERSON" | "QUEUE"` (required)
- `archived`: bool (required)
- `createdAt`, `updatedAt`: str ISO 8601 (required)
- `teams`: optional list of `{id, name, primary}`

## Pagination

Cursor-based. `paging.next.after` is the cursor; pass it as `?after=<cursor>`
on the next request. Absent `paging.next` means end of results. Only the
owners list endpoint is used for pagination in this client (single-record
fetches and batch-read don't paginate in intake flow).

## HubSpot URL shapes (parser input)

1. `https://app.hubspot.com/contacts/{portalId}/record/{objectTypeId}/{recordId}`
   - `objectTypeId` values: `0-1` = contact, `0-2` = company, `0-3` = deal.
2. `https://app.hubspot.com/contacts/{portalId}/{contact|company|deal}/{recordId}`

The parser returns `(portal_id, object_type, record_id)` where `object_type`
is the normalized plural form: `"contacts"`, `"companies"`, `"deals"`. This
matches the `/crm/v3/objects/{objectType}/{id}` path segment used by the
single-object GET endpoints.
