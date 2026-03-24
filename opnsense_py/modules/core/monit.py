from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.monit import MonitAlert, MonitService, MonitTest
from opnsense_py.modules.base import BaseModule

_M = "monit"


class MonitModule(BaseModule):
    """Wrapper for the OPNsense Monit API."""

    # -- Settings (global) -------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def get_general(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/get_general")

    # -- Services ----------------------------------------------------------

    def search_services(self, request: SearchRequest | None = None) -> SearchResponse[MonitService]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_service", json=req.model_dump())
        return SearchResponse[MonitService].model_validate(raw)

    def get_service(self, uuid: str | None = None) -> MonitService:
        raw = self._get_item(_M, "settings", "get_service", uuid)
        return MonitService.model_validate(raw.get("service", raw))

    def add_service(self, service: MonitService) -> ApiResponse:
        return self._add_item(_M, "settings", "add_service", {"service": service.model_dump(exclude_none=True)})

    def set_service(self, uuid: str, service: MonitService) -> ApiResponse:
        return self._set_item(_M, "settings", "set_service", uuid, {"service": service.model_dump(exclude_none=True)})

    def del_service(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_service", uuid)

    def toggle_service(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_service", uuid, enabled)

    # -- Tests -------------------------------------------------------------

    def search_tests(self, request: SearchRequest | None = None) -> SearchResponse[MonitTest]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_test", json=req.model_dump())
        return SearchResponse[MonitTest].model_validate(raw)

    def get_test(self, uuid: str | None = None) -> MonitTest:
        raw = self._get_item(_M, "settings", "get_test", uuid)
        return MonitTest.model_validate(raw.get("test", raw))

    def add_test(self, test: MonitTest) -> ApiResponse:
        return self._add_item(_M, "settings", "add_test", {"test": test.model_dump(exclude_none=True)})

    def set_test(self, uuid: str, test: MonitTest) -> ApiResponse:
        return self._set_item(_M, "settings", "set_test", uuid, {"test": test.model_dump(exclude_none=True)})

    def del_test(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_test", uuid)

    # -- Alerts ------------------------------------------------------------

    def search_alerts(self, request: SearchRequest | None = None) -> SearchResponse[MonitAlert]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_alert", json=req.model_dump())
        return SearchResponse[MonitAlert].model_validate(raw)

    def get_alert(self, uuid: str | None = None) -> MonitAlert:
        raw = self._get_item(_M, "settings", "get_alert", uuid)
        return MonitAlert.model_validate(raw.get("alert", raw))

    def add_alert(self, alert: MonitAlert) -> ApiResponse:
        return self._add_item(_M, "settings", "add_alert", {"alert": alert.model_dump(exclude_none=True)})

    def set_alert(self, uuid: str, alert: MonitAlert) -> ApiResponse:
        return self._set_item(_M, "settings", "set_alert", uuid, {"alert": alert.model_dump(exclude_none=True)})

    def del_alert(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_alert", uuid)

    def toggle_alert(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_alert", uuid, enabled)

    # -- Status ------------------------------------------------------------

    def get_status(self, fmt: str = "xml") -> dict[str, Any]:
        return self._client._get(f"{_M}/status/get/{fmt}")

    # -- Service -----------------------------------------------------------

    def start(self) -> ApiResponse:
        return self._service_start(_M)

    def stop(self) -> ApiResponse:
        return self._service_stop(_M)

    def restart(self) -> ApiResponse:
        return self._service_restart(_M)

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def check(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/service/check"))

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)
