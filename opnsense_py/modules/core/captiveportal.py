from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.captiveportal import CaptivePortalZone
from opnsense_py.modules.base import BaseModule

_M = "captiveportal"


class CaptivePortalModule(BaseModule):
    """Wrapper for the OPNsense Captive Portal API."""

    # -- Zones (settings) --------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def search_zones(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[CaptivePortalZone]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_zones", json=req.model_dump())
        return SearchResponse[CaptivePortalZone].model_validate(raw)

    def get_zone(self, uuid: str | None = None) -> CaptivePortalZone:
        raw = self._get_item(_M, "settings", "get_zone", uuid)
        return CaptivePortalZone.model_validate(raw.get("zone", raw))

    def add_zone(self, zone: CaptivePortalZone) -> ApiResponse:
        return self._add_item(_M, "settings", "add_zone", {"zone": zone.model_dump(exclude_none=True)})

    def set_zone(self, uuid: str, zone: CaptivePortalZone) -> ApiResponse:
        return self._set_item(_M, "settings", "set_zone", uuid, {"zone": zone.model_dump(exclude_none=True)})

    def del_zone(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_zone", uuid)

    def toggle_zone(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_zone", uuid, enabled)

    # -- Sessions ----------------------------------------------------------

    def list_sessions(self, zone_id: int = 0) -> dict[str, Any]:
        return self._client._get(f"{_M}/session/list/{zone_id}")

    def search_sessions(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/session/search")

    def list_zones(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/session/zones")

    def connect_session(self, zone_id: int = 0, data: dict[str, Any] | None = None) -> ApiResponse:
        raw = self._client._post(f"{_M}/session/connect/{zone_id}", json=data or {})
        return ApiResponse.model_validate(raw)

    def disconnect_session(self, zone_id: str = "", data: dict[str, Any] | None = None) -> ApiResponse:
        raw = self._client._post(f"{_M}/session/disconnect/{zone_id}", json=data or {})
        return ApiResponse.model_validate(raw)

    # -- Access ------------------------------------------------------------

    def api_info(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/access/api")

    def logon(self, zone_id: int = 0, data: dict[str, Any] | None = None) -> ApiResponse:
        raw = self._client._post(f"{_M}/access/logon/{zone_id}", json=data or {})
        return ApiResponse.model_validate(raw)

    def logoff(self, zone_id: int = 0) -> dict[str, Any]:
        return self._client._get(f"{_M}/access/logoff/{zone_id}")

    def access_status(self, zone_id: int = 0) -> dict[str, Any]:
        return self._client._get(f"{_M}/access/status/{zone_id}")

    # -- Vouchers ----------------------------------------------------------

    def list_voucher_providers(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/voucher/list_providers")

    def list_voucher_groups(self, provider: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/voucher/list_voucher_groups/{provider}")

    def list_vouchers(self, provider: str, group: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/voucher/list_vouchers/{provider}/{group}")

    def generate_vouchers(self, provider: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/voucher/generate_vouchers/{provider}", json=data)
        return ApiResponse.model_validate(raw)

    def expire_voucher(self, provider: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/voucher/expire_voucher/{provider}", json=data)
        return ApiResponse.model_validate(raw)

    def drop_voucher_group(self, provider: str, group: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/voucher/drop_voucher_group/{provider}/{group}")
        return ApiResponse.model_validate(raw)

    def drop_expired_vouchers(self, provider: str, group: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/voucher/drop_expired_vouchers/{provider}/{group}")
        return ApiResponse.model_validate(raw)

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

    def search_templates(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/search_templates")

    def get_template(self, file_id: str | None = None) -> dict[str, Any]:
        path = f"{_M}/service/get_template"
        if file_id is not None:
            path = f"{path}/{file_id}"
        return self._client._get(path)

    def save_template(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/service/save_template", json=data)
        return ApiResponse.model_validate(raw)

    def del_template(self, uuid: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/service/del_template/{uuid}")
        return ApiResponse.model_validate(raw)
