from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.radvd import RadvdEntry
from opnsense_py.modules.base import BaseModule

_M = "radvd"


class RadvdModule(BaseModule):
    """Wrapper for the OPNsense RADVd API."""

    # -- Settings ----------------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def search_entries(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[RadvdEntry]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_entry", json=req.model_dump())
        return SearchResponse[RadvdEntry].model_validate(raw)

    def get_entry(self, uuid: str | None = None) -> RadvdEntry:
        raw = self._get_item(_M, "settings", "get_entry", uuid)
        return RadvdEntry.model_validate(raw.get("entry", raw))

    def add_entry(self, entry: RadvdEntry) -> ApiResponse:
        return self._add_item(_M, "settings", "add_entry", {"entry": entry.model_dump(exclude_none=True)})

    def set_entry(self, uuid: str, entry: RadvdEntry) -> ApiResponse:
        return self._set_item(_M, "settings", "set_entry", uuid, {"entry": entry.model_dump(exclude_none=True)})

    def del_entry(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_entry", uuid)

    def toggle_entry(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_entry", uuid, enabled)

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
