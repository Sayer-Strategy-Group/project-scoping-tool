"""Credential loader for intake automation.

Reads API tokens from 1Password CLI first, falls back to macOS Keychain,
then environment variables, then a repo-local .env file (gitignored).

1Password lookup uses ``op item get`` with the vault UID to avoid issues
with special characters in vault names (the ``op://`` reference format
rejects ``&``).
"""

import os
import subprocess
from pathlib import Path
from typing import Optional


KEYCHAIN_ACCOUNT = "harbuckconsulting"
REPO_ROOT = Path(__file__).resolve().parent.parent
DOTENV_PATH = REPO_ROOT / ".env"

# 1Password vault UID and item-title mapping for secrets used by intake scripts.
# Uses vault UID (not name) because the vault name "AI & DevOps" contains '&'
# which breaks the op:// secret-reference URI format.
OP_VAULT_UID = "ez66lctiol3y7bs4yxbt4tfbr4"
OP_SECRET_MAP = {
    "HUBSPOT_API_KEY": ("Hubspot AIVA API Credentials", "credential"),
    "FIREFLIES_API_KEY": ("Fireflies API Credentials", "credential"),
}


def _from_1password(name: str) -> Optional[str]:
    """Look up a secret from 1Password CLI using ``op item get``."""
    mapping = OP_SECRET_MAP.get(name)
    if not mapping:
        return None
    item_title, field = mapping
    try:
        result = subprocess.run(
            [
                "op",
                "item",
                "get",
                item_title,
                "--vault",
                OP_VAULT_UID,
                "--fields",
                field,
                "--reveal",
            ],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None

    if result.returncode != 0:
        return None

    value = result.stdout.strip()
    return value or None


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
    """Return the secret value for `name`, checking 1Password -> Keychain -> env -> .env.

    Raises RuntimeError if nothing is found. `name` is used for both
    the Keychain service and the env variable (convention: HUBSPOT_API_KEY,
    FIREFLIES_API_KEY, LINEAR_API_KEY).
    """
    for source_fn in (_from_1password, _from_keychain, _from_env, _from_dotenv):
        value = source_fn(name)
        if value:
            return value

    op_hint = ""
    mapping = OP_SECRET_MAP.get(name)
    if mapping:
        op_hint = (
            f" 1Password vault {OP_VAULT_UID} "
            f"(item '{mapping[0]}', field '{mapping[1]}'),"
        )

    raise RuntimeError(
        f"Secret '{name}' not found. Checked:{op_hint} macOS Keychain "
        f"(account={KEYCHAIN_ACCOUNT}, service={name}), environment "
        f"variable {name}, and {DOTENV_PATH}."
    )
