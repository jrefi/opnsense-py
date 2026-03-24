from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class Route(OPNsenseModel):
    """A static route entry (routes/route)."""

    network: str | None = None
    gateway: str | None = None
    descr: str | None = None
    disabled: str | None = None
