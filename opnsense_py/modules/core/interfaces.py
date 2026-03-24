from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.interfaces import Vlan
from opnsense_py.modules.base import BaseModule

_M = "interfaces"


def _std_crud(controller: str) -> tuple[str, str]:
    """Return (module, controller) tuple for standard interfaces CRUD."""
    return _M, controller


class InterfacesModule(BaseModule):
    """Wrapper for the OPNsense Interfaces API."""

    # -- Bridge Settings ---------------------------------------------------

    def search_bridges(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "bridge_settings", "search_item", request)

    def get_bridge(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "bridge_settings", "get_item", uuid)

    def add_bridge(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "bridge_settings", "add_item", data)

    def set_bridge(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "bridge_settings", "set_item", uuid, data)

    def del_bridge(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "bridge_settings", "del_item", uuid)

    def get_bridge_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/bridge_settings/get")

    def set_bridge_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/bridge_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def reconfigure_bridges(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/bridge_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- GIF Settings ------------------------------------------------------

    def search_gifs(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "gif_settings", "search_item", request)

    def get_gif(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "gif_settings", "get_item", uuid)

    def add_gif(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "gif_settings", "add_item", data)

    def set_gif(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "gif_settings", "set_item", uuid, data)

    def del_gif(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "gif_settings", "del_item", uuid)

    def get_gif_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/gif_settings/get")

    def set_gif_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/gif_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def get_gif_if_options(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/gif_settings/get_if_options")

    def reconfigure_gifs(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/gif_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- GRE Settings ------------------------------------------------------

    def search_gres(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "gre_settings", "search_item", request)

    def get_gre(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "gre_settings", "get_item", uuid)

    def add_gre(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "gre_settings", "add_item", data)

    def set_gre(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "gre_settings", "set_item", uuid, data)

    def del_gre(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "gre_settings", "del_item", uuid)

    def get_gre_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/gre_settings/get")

    def set_gre_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/gre_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def get_gre_if_options(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/gre_settings/get_if_options")

    def reconfigure_gres(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/gre_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- LAGG Settings -----------------------------------------------------

    def search_laggs(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "lagg_settings", "search_item", request)

    def get_lagg(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "lagg_settings", "get_item", uuid)

    def add_lagg(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "lagg_settings", "add_item", data)

    def set_lagg(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "lagg_settings", "set_item", uuid, data)

    def del_lagg(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "lagg_settings", "del_item", uuid)

    def get_lagg_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/lagg_settings/get")

    def set_lagg_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/lagg_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def reconfigure_laggs(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/lagg_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- Loopback Settings -------------------------------------------------

    def search_loopbacks(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "loopback_settings", "search_item", request)

    def get_loopback(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "loopback_settings", "get_item", uuid)

    def add_loopback(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "loopback_settings", "add_item", data)

    def set_loopback(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "loopback_settings", "set_item", uuid, data)

    def del_loopback(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "loopback_settings", "del_item", uuid)

    def get_loopback_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/loopback_settings/get")

    def set_loopback_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/loopback_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def reconfigure_loopbacks(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/loopback_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- Neighbor Settings -------------------------------------------------

    def search_neighbors(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "neighbor_settings", "search_item", request)

    def get_neighbor(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "neighbor_settings", "get_item", uuid)

    def add_neighbor(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "neighbor_settings", "add_item", data)

    def set_neighbor(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "neighbor_settings", "set_item", uuid, data)

    def del_neighbor(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "neighbor_settings", "del_item", uuid)

    def get_neighbor_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/neighbor_settings/get")

    def set_neighbor_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/neighbor_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def reconfigure_neighbors(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/neighbor_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- VIP Settings ------------------------------------------------------

    def search_vips(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "vip_settings", "search_item", request)

    def get_vip(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "vip_settings", "get_item", uuid)

    def add_vip(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "vip_settings", "add_item", data)

    def set_vip(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "vip_settings", "set_item", uuid, data)

    def del_vip(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "vip_settings", "del_item", uuid)

    def get_vip_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/vip_settings/get")

    def set_vip_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/vip_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def get_unused_vhid(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/vip_settings/get_unused_vhid")

    def reconfigure_vips(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/vip_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- VLAN Settings -----------------------------------------------------

    def search_vlans(self, request: SearchRequest | None = None) -> SearchResponse[Vlan]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/vlan_settings/search_item", json=req.model_dump())
        return SearchResponse[Vlan].model_validate(raw)

    def get_vlan(self, uuid: str | None = None) -> Vlan:
        raw = self._get_item(_M, "vlan_settings", "get_item", uuid)
        return Vlan.model_validate(raw.get("vlan", raw))

    def add_vlan(self, vlan: Vlan) -> ApiResponse:
        return self._add_item(_M, "vlan_settings", "add_item", {"vlan": vlan.model_dump(exclude_none=True)})

    def set_vlan(self, uuid: str, vlan: Vlan) -> ApiResponse:
        return self._set_item(_M, "vlan_settings", "set_item", uuid, {"vlan": vlan.model_dump(exclude_none=True)})

    def del_vlan(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "vlan_settings", "del_item", uuid)

    def get_vlan_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/vlan_settings/get")

    def set_vlan_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/vlan_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def reconfigure_vlans(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/vlan_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- VXLAN Settings ----------------------------------------------------

    def search_vxlans(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "vxlan_settings", "search_item", request)

    def get_vxlan(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "vxlan_settings", "get_item", uuid)

    def add_vxlan(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "vxlan_settings", "add_item", data)

    def set_vxlan(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "vxlan_settings", "set_item", uuid, data)

    def del_vxlan(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "vxlan_settings", "del_item", uuid)

    def get_vxlan_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/vxlan_settings/get")

    def set_vxlan_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/vxlan_settings/set", json=data)
        return ApiResponse.model_validate(raw)

    def reconfigure_vxlans(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/vxlan_settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- General Settings --------------------------------------------------

    def get_settings(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set_settings(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def reconfigure_settings(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- Overview ----------------------------------------------------------

    def get_interface(self, iface: str | None = None) -> dict[str, Any]:
        path = f"{_M}/overview/get_interface"
        if iface:
            path = f"{path}/{iface}"
        return self._client._get(path)

    def interfaces_info(self, details: bool = False) -> dict[str, Any]:
        return self._client._get(f"{_M}/overview/interfaces_info/{int(details)}")

    def reload_interface(self, identifier: str | None = None) -> dict[str, Any]:
        path = f"{_M}/overview/reload_interface"
        if identifier:
            path = f"{path}/{identifier}"
        return self._client._get(path)

    def export_interfaces(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/overview/export")
