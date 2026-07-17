"""Pytest bootstrap: put `scripts/` on sys.path + gate live API tests.

`scripts/hubspot_client.py` and `scripts/fireflies_client.py` use flat
imports (`from keychain import get_secret`, `from hubspot_models import ...`).
This file adds the scripts directory to `sys.path` so pytest can collect
and run modules that live there.

It also gates tests marked ``@pytest.mark.live`` (which hit real external
APIs, e.g. the production HubSpot portal). Those are SKIPPED by default so a
routine ``pytest`` run is hermetic regardless of whether a credential happens
to be resolvable on the machine. Opt in explicitly with ``--run-live`` or
``SAYER_RUN_LIVE_TESTS=1``.
"""

import os
import sys
from pathlib import Path

import pytest

_SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))


def pytest_addoption(parser):
    parser.addoption(
        "--run-live",
        action="store_true",
        default=False,
        help=(
            "Run live API contract tests that hit real external services "
            "(e.g. the production HubSpot portal). Off by default."
        ),
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        (
            "live: test hits a real external API (HubSpot portal). Skipped "
            "unless --run-live or SAYER_RUN_LIVE_TESTS=1."
        ),
    )


def pytest_collection_modifyitems(config, items):
    run_live = (
        config.getoption("--run-live")
        or os.environ.get("SAYER_RUN_LIVE_TESTS") == "1"
    )
    if run_live:
        return
    skip_live = pytest.mark.skip(
        reason="live API test — pass --run-live or set SAYER_RUN_LIVE_TESTS=1 to run"
    )
    for item in items:
        if "live" in item.keywords:
            item.add_marker(skip_live)
