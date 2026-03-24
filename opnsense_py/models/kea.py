from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class KeaSubnet4(OPNsenseModel):
    """A Kea DHCPv4 subnet (kea/subnet4)."""

    subnet: str | None = None
    next_server: str | None = None
    option_data_autocollect: str | None = None
    pools: str | None = None
    match_client_id: str | None = None
    ddns_forward_zone: str | None = None
    ddns_dns_server: str | None = None
    description: str | None = None


class KeaReservation4(OPNsenseModel):
    """A Kea DHCPv4 host reservation (kea/reservation)."""

    subnet: str | None = None
    ip_address: str | None = None
    hw_address: str | None = None
    hostname: str | None = None
    description: str | None = None


class KeaOption(OPNsenseModel):
    """A Kea DHCP custom option definition (kea/option)."""

    code: str | None = None
    encoding: str | None = None
    data: str | None = None
    force: str | None = None
    description: str | None = None


class KeaHaPeer(OPNsenseModel):
    """A Kea high-availability peer (kea/peer)."""

    name: str | None = None
    role: str | None = None
    url: str | None = None
