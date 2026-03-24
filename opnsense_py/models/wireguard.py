from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class WireguardServer(OPNsenseModel):
    """A WireGuard server/instance (wireguard/server)."""

    enabled: str | None = None
    name: str | None = None
    pubkey: str | None = None
    privkey: str | None = None
    port: str | None = None
    mtu: int | None = None
    dns: str | None = None
    tunneladdress: str | None = None
    disableroutes: str | None = None
    gateway: str | None = None
    peers: str | None = None
    debug: str | None = None


class WireguardPeer(OPNsenseModel):
    """A WireGuard peer/client (wireguard/client)."""

    enabled: str | None = None
    name: str | None = None
    pubkey: str | None = None
    psk: str | None = None
    tunneladdress: str | None = None
    serveraddress: str | None = None
    serverport: str | None = None
    keepalive: int | None = None
