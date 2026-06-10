# scripts/

Python automation for the scoping and delivery workflow. All scripts target
Python 3.9 for consistency with the system Python on the macOS dev machine.

## Setup

Install dependencies once:

```bash
pip3 install -r requirements.txt
```

**Team default — no personal API keys needed.** Credentials resolve from the
shared Sayer 1Password vault. One-time setup:

```bash
brew install 1password-cli
# Then in the 1Password app: Settings -> Developer -> Integrate with 1Password CLI
# Sign in to the Sayer 1Password account, then verify:
op read "op://Shared/FIREFLIES_API_KEY/credential"
op read "op://Shared/HUBSPOT_API_KEY/credential"
```

The vault name is overridable via `SAYER_OP_VAULT` (default: `Shared`).

**Personal overrides** (optional — checked *before* 1Password). Resolution order
per secret: **Keychain → env var → `.env` → 1Password**.

```bash
# Optional — override the Keychain account for this machine (default: harbuckconsulting)
export SAYER_KEYCHAIN_ACCOUNT="$(whoami)"

security add-generic-password -a "$SAYER_KEYCHAIN_ACCOUNT" -s HUBSPOT_API_KEY   -w 'pat-na1-...'
security add-generic-password -a "$SAYER_KEYCHAIN_ACCOUNT" -s FIREFLIES_API_KEY -w '...'
```

Env vars and a repo-local `.env` (gitignored) also work — anyone who keeps
tokens there can skip both Keychain and 1Password.

## `intake.py` — client intake automation

Scaffold a scoping folder from a HubSpot record URL:

```bash
# Verify both API tokens — no fetch, no writes
python3 scripts/intake.py --test-only

# Fetch everything and show what *would* be written
python3 scripts/intake.py --url 'https://app.hubspot.com/contacts/12345/record/0-3/67890' --dry-run

# Live run — creates {Client Name}/ under the repo root
python3 scripts/intake.py --url 'https://app.hubspot.com/contacts/12345/record/0-3/67890'

# Override folder name (defaults to HubSpot company name)
python3 scripts/intake.py --url '<URL>' --client-name 'Acme Corp'

# Overwrite an existing folder
python3 scripts/intake.py --url '<URL>' --force
```

Accepts any of the three standard HubSpot record URL shapes (deal, company,
contact), in either the modern `/record/{objectTypeId}/{id}` format or the
legacy `/{singular}/{id}` format.

### What gets scaffolded

Per the CLAUDE.md convention:

```
{Client Name}/
  {Client} Discovery {YYYY-MM-DD}.md      ← HubSpot notes + Fireflies summaries
  {Client} Meeting Recording.md           ← Full Fireflies transcripts
  {Client}_decisions.md                   ← Stamped from templates/decisions-template.md
  STATE.md                                ← Stamped from templates/client-state-template.md
```

## `hubspot_client.py` + `hubspot_models.py`

Typed pydantic v2 client for HubSpot CRM v3. Generated from HubSpot's public
OpenAPI specs (stored under `.api-specs/`). Read-only, intake-focused: ping,
fetch company/deal/contact with associations, batch-read contacts, walk
associations, fetch engagements (notes / calls / meetings / emails).

Models intentionally treat `properties` as `Dict[str, Optional[str]]` — HubSpot
returns every property as a nullable string, even numerics like
`annualrevenue`. Callers coerce.

See `hubspot-schema-notes.md` at repo root for the endpoint map and the quirks
documented during generation.

## `fireflies_client.py`

GraphQL wrapper for `https://api.fireflies.ai/graphql`. Ported from AIVA's
production client. Exposes `ping()`, `list_recent(days, limit)`,
`get_transcript(id)`, and `filter_by_emails(transcripts, emails)`.

## `keychain.py`

Small helper that loads secrets via macOS Keychain → env → `.env` → shared
1Password vault (`op` CLI). Used by both clients.

## Tests

Live contract tests live in `tests/` at repo root:

```bash
python3 -m pytest tests/test_hubspot_contract.py -v
```

URL-parser tests always run. Live API tests skip cleanly when
`HUBSPOT_API_KEY` is unavailable.
