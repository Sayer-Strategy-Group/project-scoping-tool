"""Pytest bootstrap: put `scripts/` on sys.path.

`scripts/hubspot_client.py` and `scripts/fireflies_client.py` use flat
imports (`from keychain import get_secret`, `from hubspot_models import ...`).
This file adds the scripts directory to `sys.path` so pytest can collect
and run modules that live there.
"""

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))
