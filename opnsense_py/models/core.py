from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class SystemService(OPNsenseModel):
    """A running system service entry (core/service/search row)."""

    id: str | None = None
    name: str | None = None
    description: str | None = None
    locked: int | None = None
    running: int | None = None


class Tunable(OPNsenseModel):
    """A sysctl tunable override (core/tunables)."""

    tunable: str | None = None
    value: str | None = None
    descr: str | None = None
    enabled: str | None = None
