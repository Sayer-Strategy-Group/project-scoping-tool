"""Credential loader for intake automation.

Reads API tokens from macOS Keychain first, falls back to environment variables,
then to a repo-local .env file (gitignored).

Matches the credential pattern documented in CLAUDE.md:
    security find-generic-password -a "<account>" -s "<KEY_NAME>" -w

The Keychain account defaults to "harbuckconsulting" but is overridable per
machine via the SAYER_KEYCHAIN_ACCOUNT env var, so teammates can point the
lookup at their own Keychain account (e.g. their macOS username) without
editing this file. Teammates who keep tokens in env vars or a .env file can
ignore the account entirely — the fallback chain still resolves them.
"""

import os
import subprocess
from pathlib import Path
from typing import Optional


KEYCHAIN_ACCOUNT = os.environ.get("SAYER_KEYCHAIN_ACCOUNT", "harbuckconsulting")
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


def get_secret(name: str) -> str:
    """Return the secret value for `name`, checking Keychain -> env -> .env.

    Raises RuntimeError if nothing is found. `name` is used for both
    the Keychain service and the env variable (convention: HUBSPOT_API_KEY,
    FIREFLIES_API_KEY, LINEAR_API_KEY).
    """
    for source_fn in (_from_keychain, _from_env, _from_dotenv):
        value = source_fn(name)
        if value:
            return value

    raise RuntimeError(
        f"Secret '{name}' not found. Checked macOS Keychain "
        f"(account={KEYCHAIN_ACCOUNT}, service={name}), environment "
        f"variable {name}, and {DOTENV_PATH}. Add the secret to Keychain with:\n"
        f'    security add-generic-password -a "{KEYCHAIN_ACCOUNT}" '
        f'-s "{name}" -w "<VALUE>"'
    )
