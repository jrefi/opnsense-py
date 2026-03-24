from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class MonitAlert(OPNsenseModel):
    """A Monit email alert definition (monit/alert)."""

    enabled: str | None = None
    recipient: str | None = None
    noton: str | None = None
    events: str | None = None
    format: str | None = None
    reminder: int | None = None
    description: str | None = None


class MonitService(OPNsenseModel):
    """A Monit service check (monit/service)."""

    enabled: str | None = None
    name: str | None = None
    type: str | None = None
    pidfile: str | None = None
    match: str | None = None
    path: str | None = None
    timeout: int | None = None
    starttimeout: int | None = None
    address: str | None = None
    interface: str | None = None
    start: str | None = None
    stop: str | None = None
    tests: str | None = None
    depends: str | None = None
    polltime: str | None = None
    description: str | None = None


class MonitTest(OPNsenseModel):
    """A Monit test condition (monit/test)."""

    name: str | None = None
    type: str | None = None
    condition: str | None = None
    action: str | None = None
    path: str | None = None
