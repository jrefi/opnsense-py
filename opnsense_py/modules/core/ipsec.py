from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.ipsec import IPsecChild, IPsecConnection, IPsecLease, IPsecLocal, IPsecPool, IPsecRemote, IPsecSession
from opnsense_py.modules.base import BaseModule

_M = "ipsec"


class IpsecModule(BaseModule):
    """Wrapper for the OPNsense IPsec API."""

    # -- Connections -------------------------------------------------------

    def get_connections(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/connections/get")

    def set_connections(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/connections/set", json=data)
        return ApiResponse.model_validate(raw)

    def is_connections_enabled(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/connections/is_enabled")

    def toggle_connections(self, enabled: bool | None = None) -> ApiResponse:
        path = f"{_M}/connections/toggle"
        if enabled is not None:
            path = f"{path}/{int(enabled)}"
        return ApiResponse.model_validate(self._client._post(path))

    def connection_exists(self, uuid: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/connections/connection_exists/{uuid}")

    def swanctl(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/connections/swanctl")

    # Connections CRUD

    def search_connections(self, request: SearchRequest | None = None) -> SearchResponse[IPsecConnection]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/connections/search_connection", json=req.model_dump())
        return SearchResponse[IPsecConnection].model_validate(raw)

    def get_connection(self, uuid: str | None = None) -> IPsecConnection:
        raw = self._get_item(_M, "connections", "get_connection", uuid)
        return IPsecConnection.model_validate(raw.get("connection", raw))

    def add_connection(self, connection: IPsecConnection) -> ApiResponse:
        return self._add_item(_M, "connections", "add_connection", {"connection": connection.model_dump(exclude_none=True)})

    def set_connection(self, uuid: str | None, connection: IPsecConnection) -> ApiResponse:
        path = f"{_M}/connections/set_connection"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"connection": connection.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_connection(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "connections", "del_connection", uuid)

    def toggle_connection(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "connections", "toggle_connection", uuid, enabled)

    # Children CRUD

    def search_children(self, request: SearchRequest | None = None) -> SearchResponse[IPsecChild]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/connections/search_child", json=req.model_dump())
        return SearchResponse[IPsecChild].model_validate(raw)

    def get_child(self, uuid: str | None = None) -> IPsecChild:
        raw = self._get_item(_M, "connections", "get_child", uuid)
        return IPsecChild.model_validate(raw.get("child", raw))

    def add_child(self, child: IPsecChild) -> ApiResponse:
        return self._add_item(_M, "connections", "add_child", {"child": child.model_dump(exclude_none=True)})

    def set_child(self, uuid: str | None, child: IPsecChild) -> ApiResponse:
        path = f"{_M}/connections/set_child"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"child": child.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_child(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "connections", "del_child", uuid)

    def toggle_child(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "connections", "toggle_child", uuid, enabled)

    # Local auth CRUD

    def search_locals(self, request: SearchRequest | None = None) -> SearchResponse[IPsecLocal]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/connections/search_local", json=req.model_dump())
        return SearchResponse[IPsecLocal].model_validate(raw)

    def get_local(self, uuid: str | None = None) -> IPsecLocal:
        raw = self._get_item(_M, "connections", "get_local", uuid)
        return IPsecLocal.model_validate(raw.get("local", raw))

    def add_local(self, local: IPsecLocal) -> ApiResponse:
        return self._add_item(_M, "connections", "add_local", {"local": local.model_dump(exclude_none=True)})

    def set_local(self, uuid: str | None, local: IPsecLocal) -> ApiResponse:
        path = f"{_M}/connections/set_local"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"local": local.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_local(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "connections", "del_local", uuid)

    def toggle_local(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "connections", "toggle_local", uuid, enabled)

    # Remote auth CRUD

    def search_remotes(self, request: SearchRequest | None = None) -> SearchResponse[IPsecRemote]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/connections/search_remote", json=req.model_dump())
        return SearchResponse[IPsecRemote].model_validate(raw)

    def get_remote(self, uuid: str | None = None) -> IPsecRemote:
        raw = self._get_item(_M, "connections", "get_remote", uuid)
        return IPsecRemote.model_validate(raw.get("remote", raw))

    def add_remote(self, remote: IPsecRemote) -> ApiResponse:
        return self._add_item(_M, "connections", "add_remote", {"remote": remote.model_dump(exclude_none=True)})

    def set_remote(self, uuid: str | None, remote: IPsecRemote) -> ApiResponse:
        path = f"{_M}/connections/set_remote"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"remote": remote.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_remote(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "connections", "del_remote", uuid)

    def toggle_remote(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "connections", "toggle_remote", uuid, enabled)

    # -- Key Pairs ---------------------------------------------------------

    def get_key_pairs(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/key_pairs/get")

    def set_key_pairs(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/key_pairs/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_key_pairs(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "key_pairs", "search_item", request)

    def get_key_pair(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "key_pairs", "get_item", uuid)

    def add_key_pair(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "key_pairs", "add_item", data)

    def set_key_pair(self, uuid: str | None, data: dict[str, Any]) -> ApiResponse:
        path = f"{_M}/key_pairs/set_item"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json=data)
        return ApiResponse.model_validate(raw)

    def del_key_pair(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "key_pairs", "del_item", uuid)

    def gen_key_pair(self, key_type: str, size: str | None = None) -> dict[str, Any]:
        path = f"{_M}/key_pairs/gen_key_pair/{key_type}"
        if size:
            path = f"{path}/{size}"
        return self._client._get(path)

    # -- Pre-Shared Keys ---------------------------------------------------

    def get_psk_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/pre_shared_keys/get")

    def set_psk_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/pre_shared_keys/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_psks(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "pre_shared_keys", "search_item", request)

    def get_psk(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "pre_shared_keys", "get_item", uuid)

    def add_psk(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "pre_shared_keys", "add_item", data)

    def set_psk(self, uuid: str | None, data: dict[str, Any]) -> ApiResponse:
        path = f"{_M}/pre_shared_keys/set_item"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json=data)
        return ApiResponse.model_validate(raw)

    def del_psk(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "pre_shared_keys", "del_item", uuid)

    # -- Manual SPD --------------------------------------------------------

    def search_manual_spds(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "manual_spd", "search", request)

    def get_manual_spd(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "manual_spd", "get", uuid)

    def add_manual_spd(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "manual_spd", "add", data)

    def set_manual_spd(self, uuid: str | None, data: dict[str, Any]) -> ApiResponse:
        path = f"{_M}/manual_spd/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json=data)
        return ApiResponse.model_validate(raw)

    def del_manual_spd(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "manual_spd", "del", uuid)

    def toggle_manual_spd(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "manual_spd", "toggle", uuid, enabled)

    # -- Pools -------------------------------------------------------------

    def search_pools(self, request: SearchRequest | None = None) -> SearchResponse[IPsecPool]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/pools/search", json=req.model_dump())
        return SearchResponse[IPsecPool].model_validate(raw)

    def get_pool(self, uuid: str | None = None) -> IPsecPool:
        raw = self._get_item(_M, "pools", "get", uuid)
        return IPsecPool.model_validate(raw.get("Pool", raw.get("pool", raw)))

    def add_pool(self, pool: IPsecPool) -> ApiResponse:
        return self._add_item(_M, "pools", "add", {"Pool": pool.model_dump(exclude_none=True)})

    def set_pool(self, uuid: str | None, pool: IPsecPool) -> ApiResponse:
        path = f"{_M}/pools/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"Pool": pool.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_pool(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "pools", "del", uuid)

    def toggle_pool(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "pools", "toggle", uuid, enabled)

    # -- VTI ---------------------------------------------------------------

    def search_vtis(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "vti", "search", request)

    def get_vti(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "vti", "get", uuid)

    def add_vti(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "vti", "add", data)

    def set_vti(self, uuid: str | None, data: dict[str, Any]) -> ApiResponse:
        path = f"{_M}/vti/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json=data)
        return ApiResponse.model_validate(raw)

    def del_vti(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "vti", "del", uuid)

    def toggle_vti(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "vti", "toggle", uuid, enabled)

    # -- Settings ----------------------------------------------------------

    def get_settings(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set_settings(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    # -- Leases ------------------------------------------------------------

    def get_lease_pools(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/leases/pools")

    def search_leases(self) -> SearchResponse[IPsecLease]:
        raw = self._client._get(f"{_M}/leases/search")
        return SearchResponse[IPsecLease].model_validate(raw)

    # -- SAD & SPD ---------------------------------------------------------

    def search_sad(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/sad/search")

    def del_sad(self, entry_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/sad/delete/{entry_id}")
        return ApiResponse.model_validate(raw)

    def search_spd(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/spd/search")

    def del_spd(self, entry_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/spd/delete/{entry_id}")
        return ApiResponse.model_validate(raw)

    # -- Tunnel (legacy) ---------------------------------------------------

    def search_phase1(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/tunnel/search_phase1")

    def search_phase2(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/tunnel/search_phase2")

    def del_phase1(self, ikeid: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/tunnel/del_phase1/{ikeid}")
        return ApiResponse.model_validate(raw)

    def del_phase2(self, seqid: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/tunnel/del_phase2/{seqid}")
        return ApiResponse.model_validate(raw)

    def toggle_tunnel(self, enabled: bool | None = None) -> ApiResponse:
        path = f"{_M}/tunnel/toggle"
        if enabled is not None:
            path = f"{path}/{int(enabled)}"
        return ApiResponse.model_validate(self._client._post(path))

    def toggle_phase1(self, ikeid: str, enabled: bool | None = None) -> ApiResponse:
        path = f"{_M}/tunnel/toggle_phase1/{ikeid}"
        if enabled is not None:
            path = f"{path}/{int(enabled)}"
        return ApiResponse.model_validate(self._client._post(path))

    def toggle_phase2(self, seqid: str, enabled: bool | None = None) -> ApiResponse:
        path = f"{_M}/tunnel/toggle_phase2/{seqid}"
        if enabled is not None:
            path = f"{path}/{int(enabled)}"
        return ApiResponse.model_validate(self._client._post(path))

    # -- Sessions ----------------------------------------------------------

    def search_sessions_phase1(self) -> SearchResponse[IPsecSession]:
        raw = self._client._get(f"{_M}/sessions/search_phase1")
        return SearchResponse[IPsecSession].model_validate(raw)

    def search_sessions_phase2(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/sessions/search_phase2")

    def connect_session(self, session_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/sessions/connect/{session_id}")
        return ApiResponse.model_validate(raw)

    def disconnect_session(self, session_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/sessions/disconnect/{session_id}")
        return ApiResponse.model_validate(raw)

    # -- Legacy subsystem --------------------------------------------------

    def apply_config(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/legacy_subsystem/apply_config")
        return ApiResponse.model_validate(raw)

    def legacy_status(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/legacy_subsystem/status")

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
