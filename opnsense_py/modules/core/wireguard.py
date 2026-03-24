from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.wireguard import WireguardPeer, WireguardServer
from opnsense_py.modules.base import BaseModule

_M = "wireguard"


class WireguardModule(BaseModule):
    """Wrapper for the OPNsense WireGuard API."""

    # -- Servers -----------------------------------------------------------

    def get_server_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/server/get")

    def set_server_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/server/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_servers(self, request: SearchRequest | None = None) -> SearchResponse[WireguardServer]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/server/search_server", json=req.model_dump())
        return SearchResponse[WireguardServer].model_validate(raw)

    def get_server(self, uuid: str | None = None) -> WireguardServer:
        raw = self._get_item(_M, "server", "get_server", uuid)
        return WireguardServer.model_validate(raw.get("server", raw))

    def add_server(self, server: WireguardServer, uuid: str | None = None) -> ApiResponse:
        path = f"{_M}/server/add_server"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"server": server.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def set_server(self, uuid: str | None, server: WireguardServer) -> ApiResponse:
        path = f"{_M}/server/set_server"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"server": server.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_server(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "server", "del_server", uuid)

    def toggle_server(self, uuid: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/server/toggle_server/{uuid}")
        return ApiResponse.model_validate(raw)

    def key_pair(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/server/key_pair")

    # -- Clients -----------------------------------------------------------

    def get_client_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/client/get")

    def set_client_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/client/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_clients(self, request: SearchRequest | None = None) -> SearchResponse[WireguardPeer]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/client/search_client", json=req.model_dump())
        return SearchResponse[WireguardPeer].model_validate(raw)

    def get_client(self, uuid: str | None = None) -> WireguardPeer:
        raw = self._get_item(_M, "client", "get_client", uuid)
        return WireguardPeer.model_validate(raw.get("client", raw))

    def add_client(self) -> dict[str, Any]:
        """Note: this endpoint uses GET, not POST."""
        return self._client._get(f"{_M}/client/add_client")

    def add_client_builder(self, client: WireguardPeer) -> ApiResponse:
        raw = self._client._post(f"{_M}/client/add_client_builder", json={"client": client.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def get_client_builder(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/client/get_client_builder")

    def set_client(self, uuid: str, client: WireguardPeer) -> ApiResponse:
        return self._set_item(_M, "client", "set_client", uuid, {"client": client.model_dump(exclude_none=True)})

    def del_client(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "client", "del_client", uuid)

    def toggle_client(self, uuid: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/client/toggle_client/{uuid}")
        return ApiResponse.model_validate(raw)

    def get_server_info(self, uuid: str | None = None) -> dict[str, Any]:
        path = f"{_M}/client/get_server_info"
        if uuid:
            path = f"{path}/{uuid}"
        return self._client._get(path)

    def list_servers(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/client/list_servers")

    def psk(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/client/psk")

    # -- General -----------------------------------------------------------

    def get_general(self) -> dict[str, Any]:
        return self._get_config(_M, "general")

    def set_general(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "general", data)

    # -- Service -----------------------------------------------------------

    def start(self) -> ApiResponse:
        return self._service_start(_M)

    def stop(self) -> ApiResponse:
        return self._service_stop(_M)

    def restart(self) -> ApiResponse:
        return self._service_restart(_M)

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def show(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/show")

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)
