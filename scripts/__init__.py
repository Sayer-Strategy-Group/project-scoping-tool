"""Intake and delivery automation scripts for the scoping tool.

This package exists so `scripts/` is discoverable as a module both when
executed directly (e.g., `python3 scripts/hubspot_client.py`) and when
imported from outside (e.g., pytest). Individual modules use flat imports
(`from keychain import get_secret`) because they're historically invoked
with `scripts/` on `sys.path`; see tests/conftest.py for how test
collection wires that up.
"""
