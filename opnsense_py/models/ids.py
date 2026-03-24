from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class IDSPolicy(OPNsenseModel):
    """An IDS/IPS policy (ids/policy)."""

    enabled: str | None = None
    prio: int | None = None
    action: str | None = None
    rulesets: str | None = None
    content: str | None = None
    new_action: str | None = None
    description: str | None = None


class IDSUserRule(OPNsenseModel):
    """A user-defined IDS/IPS rule (ids/rule)."""

    enabled: str | None = None
    source: str | None = None
    destination: str | None = None
    fingerprint: str | None = None
    description: str | None = None
    action: str | None = None
    bypass: str | None = None
