from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class DnsmasqHost(OPNsenseModel):
    """A Dnsmasq host override / DHCP static mapping (dnsmasq/host)."""

    host: str | None = None
    domain: str | None = None
    local: str | None = None
    ip: str | None = None
    cnames: str | None = None
    client_id: str | None = None
    hwaddr: str | None = None
    lease_time: int | None = None
    ignore: str | None = None
    descr: str | None = None
    comments: str | None = None


class DnsmasqDomainOverride(OPNsenseModel):
    """A Dnsmasq domain override (dnsmasq/domainoverride)."""

    domain: str | None = None
    ip: str | None = None
    srcip: str | None = None
    port: str | None = None
    descr: str | None = None
