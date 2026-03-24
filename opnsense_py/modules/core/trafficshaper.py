from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.trafficshaper import ShaperPipe, ShaperQueue, ShaperRule
from opnsense_py.modules.base import BaseModule

_M = "trafficshaper"


class TrafficShaperModule(BaseModule):
    """Wrapper for the OPNsense Traffic Shaper API."""

    # -- Settings (global) -------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    # -- Pipes -------------------------------------------------------------

    def search_pipes(self, request: SearchRequest | None = None) -> SearchResponse[ShaperPipe]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_pipes", json=req.model_dump())
        return SearchResponse[ShaperPipe].model_validate(raw)

    def get_pipe(self, uuid: str | None = None) -> ShaperPipe:
        raw = self._get_item(_M, "settings", "get_pipe", uuid)
        return ShaperPipe.model_validate(raw.get("pipe", raw))

    def add_pipe(self, pipe: ShaperPipe) -> ApiResponse:
        return self._add_item(_M, "settings", "add_pipe", {"pipe": pipe.model_dump(exclude_none=True)})

    def set_pipe(self, uuid: str, pipe: ShaperPipe) -> ApiResponse:
        return self._set_item(_M, "settings", "set_pipe", uuid, {"pipe": pipe.model_dump(exclude_none=True)})

    def del_pipe(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_pipe", uuid)

    def toggle_pipe(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_pipe", uuid, enabled)

    def download_pipes(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/download_pipes")

    def upload_pipes(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/upload_pipes", json=data)
        return ApiResponse.model_validate(raw)

    # -- Queues ------------------------------------------------------------

    def search_queues(self, request: SearchRequest | None = None) -> SearchResponse[ShaperQueue]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_queues", json=req.model_dump())
        return SearchResponse[ShaperQueue].model_validate(raw)

    def get_queue(self, uuid: str | None = None) -> ShaperQueue:
        raw = self._get_item(_M, "settings", "get_queue", uuid)
        return ShaperQueue.model_validate(raw.get("queue", raw))

    def add_queue(self, queue: ShaperQueue) -> ApiResponse:
        return self._add_item(_M, "settings", "add_queue", {"queue": queue.model_dump(exclude_none=True)})

    def set_queue(self, uuid: str, queue: ShaperQueue) -> ApiResponse:
        return self._set_item(_M, "settings", "set_queue", uuid, {"queue": queue.model_dump(exclude_none=True)})

    def del_queue(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_queue", uuid)

    def toggle_queue(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_queue", uuid, enabled)

    def download_queues(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/download_queues")

    # -- Rules -------------------------------------------------------------

    def search_rules(self, request: SearchRequest | None = None) -> SearchResponse[ShaperRule]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_rules", json=req.model_dump())
        return SearchResponse[ShaperRule].model_validate(raw)

    def get_rule(self, uuid: str | None = None) -> ShaperRule:
        raw = self._get_item(_M, "settings", "get_rule", uuid)
        return ShaperRule.model_validate(raw.get("rule", raw))

    def add_rule(self, rule: ShaperRule) -> ApiResponse:
        return self._add_item(_M, "settings", "add_rule", {"rule": rule.model_dump(exclude_none=True)})

    def set_rule(self, uuid: str, rule: ShaperRule) -> ApiResponse:
        return self._set_item(_M, "settings", "set_rule", uuid, {"rule": rule.model_dump(exclude_none=True)})

    def del_rule(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_rule", uuid)

    def toggle_rule(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_rule", uuid, enabled)

    # -- Service -----------------------------------------------------------

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def flushreload(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/service/flushreload"))

    def statistics(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/statistics")
