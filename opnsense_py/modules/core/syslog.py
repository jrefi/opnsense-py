from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.syslog import SyslogDestination
from opnsense_py.modules.base import BaseModule

_M = "syslog"


class SyslogModule(BaseModule):
    """Wrapper for the OPNsense Syslog API."""

    # -- Settings ----------------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def search_destinations(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[SyslogDestination]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_destinations", json=req.model_dump())
        return SearchResponse[SyslogDestination].model_validate(raw)

    def get_destination(self, uuid: str | None = None) -> SyslogDestination:
        raw = self._get_item(_M, "settings", "get_destination", uuid)
        return SyslogDestination.model_validate(raw.get("destination", raw))

    def add_destination(self, destination: SyslogDestination) -> ApiResponse:
        return self._add_item(_M, "settings", "add_destination", {"destination": destination.model_dump(exclude_none=True)})

    def set_destination(self, uuid: str, destination: SyslogDestination) -> ApiResponse:
        return self._set_item(_M, "settings", "set_destination", uuid, {"destination": destination.model_dump(exclude_none=True)})

    def del_destination(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_destination", uuid)

    def toggle_destination(
        self, uuid: str, enabled: bool | None = None
    ) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_destination", uuid, enabled)

    # -- Service -----------------------------------------------------------

    def start(self) -> ApiResponse:
        return self._service_start(_M)

    def stop(self) -> ApiResponse:
        return self._service_stop(_M)

    def restart(self) -> ApiResponse:
        return self._service_restart(_M)

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def reset(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/service/reset"))

    def stats(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/stats")

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)
