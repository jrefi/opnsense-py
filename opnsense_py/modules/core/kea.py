from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.kea import KeaHaPeer, KeaReservation4, KeaSubnet4
from opnsense_py.modules.base import BaseModule

_M = "kea"


class KeaModule(BaseModule):
    """Wrapper for the OPNsense Kea DHCP API."""

    # -- Control Agent -----------------------------------------------------

    def get_ctrl_agent(self) -> dict[str, Any]:
        return self._get_config(_M, "ctrl_agent")

    def set_ctrl_agent(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "ctrl_agent", data)

    # -- DHCPv4 ------------------------------------------------------------

    def get_dhcpv4(self) -> dict[str, Any]:
        return self._get_config(_M, "dhcpv4")

    def set_dhcpv4(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "dhcpv4", data)

    # DHCPv4 Subnets

    def search_v4_subnets(self, request: SearchRequest | None = None) -> SearchResponse[KeaSubnet4]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/dhcpv4/search_subnet", json=req.model_dump())
        return SearchResponse[KeaSubnet4].model_validate(raw)

    def get_v4_subnet(self, uuid: str | None = None) -> KeaSubnet4:
        raw = self._get_item(_M, "dhcpv4", "get_subnet", uuid)
        return KeaSubnet4.model_validate(raw.get("subnet4", raw))

    def add_v4_subnet(self, subnet: KeaSubnet4) -> ApiResponse:
        return self._add_item(_M, "dhcpv4", "add_subnet", {"subnet4": subnet.model_dump(exclude_none=True)})

    def set_v4_subnet(self, uuid: str, subnet: KeaSubnet4) -> ApiResponse:
        return self._set_item(_M, "dhcpv4", "set_subnet", uuid, {"subnet4": subnet.model_dump(exclude_none=True)})

    def del_v4_subnet(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "dhcpv4", "del_subnet", uuid)

    # DHCPv4 Reservations

    def search_v4_reservations(self, request: SearchRequest | None = None) -> SearchResponse[KeaReservation4]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/dhcpv4/search_reservation", json=req.model_dump())
        return SearchResponse[KeaReservation4].model_validate(raw)

    def get_v4_reservation(self, uuid: str | None = None) -> KeaReservation4:
        raw = self._get_item(_M, "dhcpv4", "get_reservation", uuid)
        return KeaReservation4.model_validate(raw.get("reservation", raw))

    def add_v4_reservation(self, reservation: KeaReservation4) -> ApiResponse:
        return self._add_item(_M, "dhcpv4", "add_reservation", {"reservation": reservation.model_dump(exclude_none=True)})

    def set_v4_reservation(self, uuid: str, reservation: KeaReservation4) -> ApiResponse:
        return self._set_item(_M, "dhcpv4", "set_reservation", uuid, {"reservation": reservation.model_dump(exclude_none=True)})

    def del_v4_reservation(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "dhcpv4", "del_reservation", uuid)

    def download_v4_reservations(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/dhcpv4/download_reservations")

    def upload_v4_reservations(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/dhcpv4/upload_reservations", json=data)
        return ApiResponse.model_validate(raw)

    # DHCPv4 HA Peers

    def search_v4_peers(self, request: SearchRequest | None = None) -> SearchResponse[KeaHaPeer]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/dhcpv4/search_peer", json=req.model_dump())
        return SearchResponse[KeaHaPeer].model_validate(raw)

    def get_v4_peer(self, uuid: str | None = None) -> KeaHaPeer:
        raw = self._get_item(_M, "dhcpv4", "get_peer", uuid)
        return KeaHaPeer.model_validate(raw.get("peer", raw))

    def add_v4_peer(self, peer: KeaHaPeer) -> ApiResponse:
        return self._add_item(_M, "dhcpv4", "add_peer", {"peer": peer.model_dump(exclude_none=True)})

    def set_v4_peer(self, uuid: str, peer: KeaHaPeer) -> ApiResponse:
        return self._set_item(_M, "dhcpv4", "set_peer", uuid, {"peer": peer.model_dump(exclude_none=True)})

    def del_v4_peer(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "dhcpv4", "del_peer", uuid)

    # -- DHCPv6 ------------------------------------------------------------

    def get_dhcpv6(self) -> dict[str, Any]:
        return self._get_config(_M, "dhcpv6")

    def set_dhcpv6(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "dhcpv6", data)

    # DHCPv6 Subnets

    def search_v6_subnets(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "dhcpv6", "search_subnet", request)

    def get_v6_subnet(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "dhcpv6", "get_subnet", uuid)

    def add_v6_subnet(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "dhcpv6", "add_subnet", data)

    def set_v6_subnet(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "dhcpv6", "set_subnet", uuid, data)

    def del_v6_subnet(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "dhcpv6", "del_subnet", uuid)

    # DHCPv6 Reservations

    def search_v6_reservations(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "dhcpv6", "search_reservation", request)

    def get_v6_reservation(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "dhcpv6", "get_reservation", uuid)

    def add_v6_reservation(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "dhcpv6", "add_reservation", data)

    def set_v6_reservation(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "dhcpv6", "set_reservation", uuid, data)

    def del_v6_reservation(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "dhcpv6", "del_reservation", uuid)

    def download_v6_reservations(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/dhcpv6/download_reservations")

    def upload_v6_reservations(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/dhcpv6/upload_reservations", json=data)
        return ApiResponse.model_validate(raw)

    # DHCPv6 HA Peers

    def search_v6_peers(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "dhcpv6", "search_peer", request)

    def get_v6_peer(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "dhcpv6", "get_peer", uuid)

    def add_v6_peer(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "dhcpv6", "add_peer", data)

    def set_v6_peer(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "dhcpv6", "set_peer", uuid, data)

    def del_v6_peer(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "dhcpv6", "del_peer", uuid)

    # DHCPv6 PD Pools

    def search_v6_pd_pools(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "dhcpv6", "search_pd_pool", request)

    def get_v6_pd_pool(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "dhcpv6", "get_pd_pool", uuid)

    def add_v6_pd_pool(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "dhcpv6", "add_pd_pool", data)

    def set_v6_pd_pool(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "dhcpv6", "set_pd_pool", uuid, data)

    def del_v6_pd_pool(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "dhcpv6", "del_pd_pool", uuid)

    # -- Leases ------------------------------------------------------------

    def search_leases(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/leases/search")

    # -- Service -----------------------------------------------------------

    def start(self) -> ApiResponse:
        return self._service_start(_M)

    def stop(self) -> ApiResponse:
        return self._service_stop(_M)

    def restart(self) -> ApiResponse:
        return self._service_restart(_M)

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)
