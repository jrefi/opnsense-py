from opnsense_py.models.base import ApiResponse, OPNsenseModel, SearchRequest, SearchResponse
from opnsense_py.models.cron import CronJob
from opnsense_py.models.dhcrelay import DHCRelayDestination, DHCRelayRelay
from opnsense_py.models.dnsmasq import DnsmasqDomainOverride, DnsmasqHost
from opnsense_py.models.firewall import (
    DNatRule,
    FilterRule,
    FirewallAlias,
    FirewallCategory,
    NPTRule,
    OneToOneRule,
    SNatRule,
)
from opnsense_py.models.ids import IDSPolicy, IDSUserRule
from opnsense_py.models.interfaces import Vlan
from opnsense_py.models.ipsec import IPsecChild, IPsecConnection, IPsecLocal, IPsecPool, IPsecRemote
from opnsense_py.models.kea import KeaHaPeer, KeaOption, KeaReservation4, KeaSubnet4
from opnsense_py.models.monit import MonitAlert, MonitService, MonitTest
from opnsense_py.models.openvpn import OpenVPNInstance, OpenVPNOverwrite, OpenVPNStaticKey
from opnsense_py.models.routes import Route
from opnsense_py.models.routing import Gateway
from opnsense_py.models.syslog import SyslogDestination
from opnsense_py.models.trafficshaper import ShaperPipe, ShaperQueue, ShaperRule
from opnsense_py.models.unbound import HostAlias, HostOverride, UnboundAcl, UnboundDnsbl, UnboundDot
from opnsense_py.models.wireguard import WireguardPeer, WireguardServer

__all__ = [
    # base
    "ApiResponse",
    "OPNsenseModel",
    "SearchRequest",
    "SearchResponse",
    # cron
    "CronJob",
    # dhcrelay
    "DHCRelayDestination",
    "DHCRelayRelay",
    # dnsmasq
    "DnsmasqDomainOverride",
    "DnsmasqHost",
    # firewall
    "DNatRule",
    "FilterRule",
    "FirewallAlias",
    "FirewallCategory",
    "NPTRule",
    "OneToOneRule",
    "SNatRule",
    # ids
    "IDSPolicy",
    "IDSUserRule",
    # interfaces
    "Vlan",
    # ipsec
    "IPsecChild",
    "IPsecConnection",
    "IPsecLocal",
    "IPsecPool",
    "IPsecRemote",
    # kea
    "KeaHaPeer",
    "KeaOption",
    "KeaReservation4",
    "KeaSubnet4",
    # monit
    "MonitAlert",
    "MonitService",
    "MonitTest",
    # openvpn
    "OpenVPNInstance",
    "OpenVPNOverwrite",
    "OpenVPNStaticKey",
    # routes
    "Route",
    # routing
    "Gateway",
    # syslog
    "SyslogDestination",
    # trafficshaper
    "ShaperPipe",
    "ShaperQueue",
    "ShaperRule",
    # unbound
    "HostAlias",
    "HostOverride",
    "UnboundAcl",
    "UnboundDnsbl",
    "UnboundDot",
    # wireguard
    "WireguardPeer",
    "WireguardServer",
]
