from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.openvpn import OpenVPNInstance, OpenVPNOverwrite, OpenVPNStaticKey
from opnsense_py.modules.base import BaseModule

_M = "openvpn"


class OpenVpnModule(BaseModule):
    """Wrapper for the OPNsense OpenVPN API."""

    # -- Instances ---------------------------------------------------------

    def search_instances(self, request: SearchRequest | None = None) -> SearchResponse[OpenVPNInstance]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/instances/search", json=req.model_dump())
        return SearchResponse[OpenVPNInstance].model_validate(raw)

    def get_instance(self, uuid: str | None = None) -> OpenVPNInstance:
        raw = self._get_item(_M, "instances", "get", uuid)
        return OpenVPNInstance.model_validate(raw.get("instance", raw))

    def add_instance(self, instance: OpenVPNInstance) -> ApiResponse:
        return self._add_item(_M, "instances", "add", {"instance": instance.model_dump(exclude_none=True)})

    def set_instance(self, uuid: str | None, instance: OpenVPNInstance) -> ApiResponse:
        path = f"{_M}/instances/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"instance": instance.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_instance(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "instances", "del", uuid)

    def toggle_instance(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "instances", "toggle", uuid, enabled)

    # -- Static keys -------------------------------------------------------

    def search_static_keys(self, request: SearchRequest | None = None) -> SearchResponse[OpenVPNStaticKey]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/instances/search_static_key", json=req.model_dump())
        return SearchResponse[OpenVPNStaticKey].model_validate(raw)

    def get_static_key(self, uuid: str | None = None) -> OpenVPNStaticKey:
        raw = self._get_item(_M, "instances", "get_static_key", uuid)
        return OpenVPNStaticKey.model_validate(raw.get("statickey", raw))

    def add_static_key(self, statickey: OpenVPNStaticKey) -> ApiResponse:
        return self._add_item(_M, "instances", "add_static_key", {"statickey": statickey.model_dump(exclude_none=True)})

    def set_static_key(self, uuid: str | None, statickey: OpenVPNStaticKey) -> ApiResponse:
        path = f"{_M}/instances/set_static_key"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"statickey": statickey.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_static_key(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "instances", "del_static_key", uuid)

    def gen_key(self, key_type: str = "secret") -> dict[str, Any]:
        return self._client._get(f"{_M}/instances/gen_key/{key_type}")

    # -- Client overwrites -------------------------------------------------

    def search_client_overwrites(self, request: SearchRequest | None = None) -> SearchResponse[OpenVPNOverwrite]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/client_overwrites/search", json=req.model_dump())
        return SearchResponse[OpenVPNOverwrite].model_validate(raw)

    def get_client_overwrite(self, uuid: str | None = None) -> OpenVPNOverwrite:
        raw = self._get_item(_M, "client_overwrites", "get", uuid)
        return OpenVPNOverwrite.model_validate(raw.get("Overwrite", raw.get("overwrite", raw)))

    def add_client_overwrite(self, overwrite: OpenVPNOverwrite) -> ApiResponse:
        return self._add_item(_M, "client_overwrites", "add", {"Overwrite": overwrite.model_dump(exclude_none=True)})

    def set_client_overwrite(self, uuid: str | None, overwrite: OpenVPNOverwrite) -> ApiResponse:
        path = f"{_M}/client_overwrites/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json={"Overwrite": overwrite.model_dump(exclude_none=True)})
        return ApiResponse.model_validate(raw)

    def del_client_overwrite(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "client_overwrites", "del", uuid)

    def toggle_client_overwrite(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "client_overwrites", "toggle", uuid, enabled)

    # -- Export ------------------------------------------------------------

    def export_accounts(self, vpn_id: str | None = None) -> dict[str, Any]:
        path = f"{_M}/export/accounts"
        if vpn_id:
            path = f"{path}/{vpn_id}"
        return self._client._get(path)

    def export_download(self, vpn_id: str, cert_ref: str | None = None, data: dict[str, Any] | None = None) -> dict[str, Any]:
        path = f"{_M}/export/download/{vpn_id}"
        if cert_ref:
            path = f"{path}/{cert_ref}"
        return self._client._post(path, json=data or {})

    def export_providers(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/export/providers")

    def export_templates(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/export/templates")

    def store_export_presets(self, vpn_id: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/export/store_presets/{vpn_id}", json=data)
        return ApiResponse.model_validate(raw)

    def validate_export_presets(self, vpn_id: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/export/validate_presets/{vpn_id}", json=data)
        return ApiResponse.model_validate(raw)

    # -- Service -----------------------------------------------------------
    # Note: OpenVPN uses start_service/stop_service/restart_service with optional $id,
    # not the standard start/stop/restart names.

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def start_service(self, service_id: str | None = None) -> ApiResponse:
        path = f"{_M}/service/start_service"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    def stop_service(self, service_id: str | None = None) -> ApiResponse:
        path = f"{_M}/service/stop_service"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    def restart_service(self, service_id: str | None = None) -> ApiResponse:
        path = f"{_M}/service/restart_service"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    def kill_session(self, data: dict[str, Any] | None = None) -> ApiResponse:
        raw = self._client._post(f"{_M}/service/kill_session", json=data or {})
        return ApiResponse.model_validate(raw)

    def search_routes(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/search_routes")

    def search_sessions(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/search_sessions")
