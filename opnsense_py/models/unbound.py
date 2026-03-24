from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class HostOverride(OPNsenseModel):
    """A DNS host override entry (unbound/host)."""

    enabled: str | None = None
    hostname: str | None = None
    domain: str | None = None
    rr: str | None = None
    mxprio: int | None = None
    mx: str | None = None
    ttl: int | None = None
    server: str | None = None
    txtdata: str | None = None
    addptr: str | None = None
    description: str | None = None


class HostAlias(OPNsenseModel):
    """A DNS host alias entry (unbound/alias)."""

    enabled: str | None = None
    host: str | None = None
    hostname: str | None = None
    domain: str | None = None
    description: str | None = None


class UnboundAcl(OPNsenseModel):
    """An Unbound access control list entry (unbound/acl)."""

    enabled: str | None = None
    name: str | None = None
    action: str | None = None
    networks: str | None = None
    description: str | None = None


class UnboundDot(OPNsenseModel):
    """An Unbound DNS-over-TLS or forward entry (unbound/dot)."""

    enabled: str | None = None
    type: str | None = None
    domain: str | None = None
    server: str | None = None
    port: str | None = None
    verify: str | None = None
    forward_tcp_upstream: str | None = None
    forward_first: str | None = None
    description: str | None = None


class UnboundDnsbl(OPNsenseModel):
    """An Unbound DNS blocklist entry (unbound/blocklist)."""

    enabled: str | None = None
    type: str | None = None
    lists: str | None = None
    allowlists: str | None = None
    blocklists: str | None = None
    wildcards: str | None = None
    source_nets: str | None = None
    address: str | None = None
    nxdomain: str | None = None
    cache_ttl: int | None = None
    description: str | None = None
