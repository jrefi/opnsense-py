from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class Vlan(OPNsenseModel):
    """A VLAN interface (interfaces/vlan)."""

    if_: str | None = None
    tag: int | None = None
    pcp: str | None = None
    proto: str | None = None
    descr: str | None = None
    vlanif: str | None = None
