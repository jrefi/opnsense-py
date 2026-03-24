from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class DHCRelayRelay(OPNsenseModel):
    """A DHCP relay entry (dhcrelay/relay)."""

    enabled: str | None = None
    interface: str | None = None
    destination: str | None = None
    agent_info: str | None = None
    carp_depend_on: str | None = None


class DHCRelayDestination(OPNsenseModel):
    """A DHCP relay destination server (dhcrelay/destination)."""

    name: str | None = None
    server: str | None = None
