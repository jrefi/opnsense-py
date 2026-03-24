from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class FilterRule(OPNsenseModel):
    """A firewall filter rule (filter/rule)."""

    enabled: str | None = None
    sequence: str | None = None
    action: str | None = None
    quick: str | None = None
    interface: str | None = None
    interfacenot: str | None = None
    direction: str | None = None
    ipprotocol: str | None = None
    protocol: str | None = None
    source_net: str | None = None
    source_not: str | None = None
    source_port: str | None = None
    destination_net: str | None = None
    destination_not: str | None = None
    destination_port: str | None = None
    gateway: str | None = None
    log: str | None = None
    statetype: str | None = None
    categories: str | None = None
    description: str | None = None


class FirewallAlias(OPNsenseModel):
    """A firewall alias (alias/alias)."""

    enabled: str | None = None
    name: str | None = None
    type: str | None = None
    proto: str | None = None
    interface: str | None = None
    counters: str | None = None
    updatefreq: str | None = None
    content: str | None = None
    categories: str | None = None
    description: str | None = None


class FirewallCategory(OPNsenseModel):
    """A firewall category (category/category)."""

    name: str | None = None
    auto: str | None = None
    color: str | None = None


class SNatRule(OPNsenseModel):
    """A source NAT (outbound) rule (source_nat/rule)."""

    enabled: str | None = None
    nonat: str | None = None
    sequence: str | None = None
    interface: str | None = None
    ipprotocol: str | None = None
    protocol: str | None = None
    source_net: str | None = None
    source_not: str | None = None
    source_port: str | None = None
    destination_net: str | None = None
    destination_not: str | None = None
    destination_port: str | None = None
    target: str | None = None
    target_port: str | None = None
    staticnatport: str | None = None
    log: str | None = None
    categories: str | None = None
    description: str | None = None


class NPTRule(OPNsenseModel):
    """A network prefix translation rule (npt/rule)."""

    enabled: str | None = None
    log: str | None = None
    sequence: str | None = None
    interface: str | None = None
    source_net: str | None = None
    destination_net: str | None = None
    trackif: str | None = None
    categories: str | None = None
    description: str | None = None


class OneToOneRule(OPNsenseModel):
    """A 1:1 NAT rule (one_to_one/rule)."""

    enabled: str | None = None
    log: str | None = None
    sequence: str | None = None
    interface: str | None = None
    type: str | None = None
    source_net: str | None = None
    source_not: str | None = None
    destination_net: str | None = None
    destination_not: str | None = None
    external: str | None = None
    natreflection: str | None = None
    categories: str | None = None
    description: str | None = None


class DNatRule(OPNsenseModel):
    """A destination NAT (port forward) rule (d_nat/rule)."""

    sequence: str | None = None
    disabled: str | None = None
    nordr: str | None = None
    interface: str | None = None
    ipprotocol: str | None = None
    protocol: str | None = None
    target: str | None = None
    local_port: str | None = None
    log: str | None = None
    natreflection: str | None = None
    descr: str | None = None
