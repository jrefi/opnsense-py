from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class OpenVPNInstance(OPNsenseModel):
    """An OpenVPN instance/server or client (openvpn/instance)."""

    enabled: str | None = None
    dev_type: str | None = None
    proto: str | None = None
    port: str | None = None
    local: str | None = None
    topology: str | None = None
    remote: str | None = None
    role: str | None = None
    server: str | None = None
    server_ipv6: str | None = None
    cert: str | None = None
    ca: str | None = None
    crl: str | None = None
    cert_depth: str | None = None
    remote_cert_tls: str | None = None
    verify_client_cert: str | None = None
    auth: str | None = None
    tls_key: str | None = None
    authmode: str | None = None
    local_group: str | None = None
    maxclients: int | None = None
    keepalive_interval: int | None = None
    keepalive_timeout: int | None = None
    reneg_sec: int | None = None
    register_dns: str | None = None
    dns_domain: str | None = None
    dns_servers: str | None = None
    tun_mtu: int | None = None
    carp_depend_on: str | None = None
    description: str | None = None


class OpenVPNOverwrite(OPNsenseModel):
    """An OpenVPN client-specific override (openvpn/Overwrite)."""

    enabled: str | None = None
    servers: str | None = None
    common_name: str | None = None
    block: str | None = None
    push_reset: str | None = None
    tunnel_network: str | None = None
    tunnel_networkv6: str | None = None
    local_networks: str | None = None
    remote_networks: str | None = None
    route_gateway: str | None = None
    redirect_gateway: str | None = None
    register_dns: str | None = None
    dns_domain: str | None = None
    dns_servers: str | None = None
    ntp_servers: str | None = None
    wins_servers: str | None = None
    description: str | None = None


class OpenVPNStaticKey(OPNsenseModel):
    """An OpenVPN static/TLS key (openvpn/statickey)."""

    mode: str | None = None
    key: str | None = None
    description: str | None = None
