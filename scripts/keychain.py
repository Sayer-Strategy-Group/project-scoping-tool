"""Credential loader for intake automation.

Reads API tokens from macOS Keychain first, falls back to environment variables,
then to a repo-local .env file (gitignored), then to the shared Sayer 1Password
vault via the `op` CLI.

Matches the credential pattern documented in CLAUDE.md:
    security find-generic-password -a "<account>" -s "<KEY_NAME>" -w

The Keychain account defaults to "harbuckconsulting" but is overridable per
machine via the SAYER_KEYCHAIN_ACCOUNT env var, so teammates can point the
lookup at their own Keychain account (e.g. their macOS username) without
editing this file.

Teammates need none of the local sources: the 1Password fallback reads
op://Shared/<KEY_NAME>/credential from the Sayer 1Password account. Install the
1Password app + CLI (`brew install 1password-cli`), enable CLI integration in
the app (Settings -> Developer -> Integrate with 1Password CLI), and sign in.
The vault is overridable via SAYER_OP_VAULT (default: "Shared").
"""

import os
import subprocess
from pathlib import Path
from typing import Optional


KEYCHAIN_ACCOUNT = os.environ.get("SAYER_KEYCHAIN_ACCOUNT", "harbuckconsulting")
OP_VAULT = os.environ.get("SAYER_OP_VAULT", "Shared")
REPO_ROOT = Path(__file__).resolve().parent.parent
DOTENV_PATH = REPO_ROOT / ".env"


def _from_keychain(service: str) -> Optional[str]:
    """Look up a password by service name in the macOS Keychain."""
    try:
        result = subprocess.run(
            [
                "security",
                "find-generic-password",
                "-a",
                KEYCHAIN_ACCOUNT,
                "-s",
                service,
                "-w",
            ],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None

    if result.returncode != 0:
        return None

    value = result.stdout.strip()
    return value or None


def _from_env(name: str) -> Optional[str]:
    value = os.environ.get(name)
    return value.strip() if value else None


def _from_dotenv(name: str) -> Optional[str]:
    if not DOTENV_PATH.exists():
        return None
    try:
        for raw in DOTENV_PATH.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            if key.strip() == name:
                return value.strip().strip('"').strip("'") or None
    except OSError:
        return None
    return None


def _from_1password(name: str) -> Optional[str]:
    """Read op://<OP_VAULT>/<name>/credential from the shared 1Password vault.

    Returns None (never raises) if the `op` CLI is missing, not signed in,
    or the item does not exist — the caller falls through to the error.
    """
    try:
        result = subprocess.run(
            ["op", "read", "op://{}/{}/credential".format(OP_VAULT, name)],
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None

    if result.returncode != 0:
        return None

    value = result.stdout.strip()
    return value or None


def get_secret(name: str) -> str:
    """Return the secret value for `name`.

    Resolution order: Keychain -> env -> .env -> 1Password (shared vault).
    Raises RuntimeError if nothing is found. `name` is used for the Keychain
    service, the env variable, and the 1Password item title (convention:
    HUBSPOT_API_KEY, FIREFLIES_API_KEY, LINEAR_API_KEY).
    """
    for source_fn in (_from_keychain, _from_env, _from_dotenv, _from_1password):
        value = source_fn(name)
        if value:
            return value

    raise RuntimeError(
        f"Secret '{name}' not found. Checked macOS Keychain "
        f"(account={KEYCHAIN_ACCOUNT}, service={name}), environment "
        f"variable {name}, {DOTENV_PATH}, and 1Password "
        f"(op://{OP_VAULT}/{name}/credential). Fix one of:\n"
        f"  - 1Password (team default): install the 1Password app + CLI "
        f"(brew install 1password-cli), enable CLI integration in the app, "
        f"sign in to the Sayer account, and confirm vault access with:\n"
        f'        op read "op://{OP_VAULT}/{name}/credential"\n'
        f"  - Keychain (personal override):\n"
        f'        security add-generic-password -a "{KEYCHAIN_ACCOUNT}" '
        f'-s "{name}" -w "<VALUE>"'
    )
