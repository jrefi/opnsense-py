from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class IPsecConnection(OPNsenseModel):
    """An IPsec IKE connection (ipsec/connection)."""

    enabled: str | None = None
    proposals: str | None = None
    unique: str | None = None
    aggressive: str | None = None
    version: str | None = None
    mobike: str | None = None
    local_addrs: str | None = None
    local_port: str | None = None
    remote_addrs: str | None = None
    remote_port: str | None = None
    encap: str | None = None
    reauth_time: int | None = None
    rekey_time: int | None = None
    over_time: int | None = None
    dpd_delay: int | None = None
    dpd_timeout: int | None = None
    pools: str | None = None
    send_certreq: str | None = None
    send_cert: str | None = None
    keyingtries: int | None = None
    description: str | None = None


class IPsecLocal(OPNsenseModel):
    """An IPsec local authentication definition (ipsec/local)."""

    enabled: str | None = None
    connection: str | None = None
    round: int | None = None
    auth: str | None = None
    id: str | None = None
    eap_id: str | None = None
    certs: str | None = None
    pubkeys: str | None = None
    description: str | None = None


class IPsecRemote(OPNsenseModel):
    """An IPsec remote authentication definition (ipsec/remote)."""

    enabled: str | None = None
    connection: str | None = None
    round: int | None = None
    auth: str | None = None
    id: str | None = None
    eap_id: str | None = None
    groups: str | None = None
    certs: str | None = None
    cacerts: str | None = None
    pubkeys: str | None = None
    description: str | None = None


class IPsecChild(OPNsenseModel):
    """An IPsec child SA (tunnel) definition (ipsec/child)."""

    enabled: str | None = None
    connection: str | None = None
    reqid: int | None = None
    esp_proposals: str | None = None
    sha256_96: str | None = None
    start_action: str | None = None
    close_action: str | None = None
    dpd_action: str | None = None
    mode: str | None = None
    policies: str | None = None
    local_ts: str | None = None
    remote_ts: str | None = None
    rekey_time: int | None = None
    description: str | None = None


class IPsecPool(OPNsenseModel):
    """An IPsec address pool (ipsec/pool)."""

    enabled: str | None = None
    name: str | None = None
    addrs: str | None = None
    dns: str | None = None


class IPsecSession(OPNsenseModel):
    """A live IPsec IKE session (ipsec/sessions/search_phase1 row)."""

    id: str | None = None
    local_host: str | None = None
    remote_host: str | None = None
    local_id: str | None = None
    remote_id: str | None = None
    version: str | None = None
    state: str | None = None
    encr_alg: str | None = None
    encr_keysize: str | None = None
    integ_alg: str | None = None
    prf_alg: str | None = None
    dh_group: str | None = None


class IPsecLease(OPNsenseModel):
    """An IPsec address pool lease (ipsec/leases/search row)."""

    id: str | None = None
    address: str | None = None
    pool: str | None = None
    identity: str | None = None
    status: str | None = None
