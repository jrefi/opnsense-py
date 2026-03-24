from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class RadvdEntry(OPNsenseModel):
    """A Router Advertisement daemon entry (radvd/settings/entry)."""

    enabled: str | None = None
    interface: str | None = None
    ra_flags: str | None = None
    ra_prio: str | None = None
    ra_interval: str | None = None
    ra_lifetime: str | None = None
    mtu: str | None = None
    description: str | None = None
