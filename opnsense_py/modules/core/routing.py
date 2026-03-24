from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.routing import Gateway
from opnsense_py.modules.base import BaseModule

_M = "routing"


class RoutingModule(BaseModule):
    """Wrapper for the OPNsense Routing (gateway) API."""

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def search_gateways(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[Gateway]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_gateway", json=req.model_dump())
        return SearchResponse[Gateway].model_validate(raw)

    def get_gateway(self, uuid: str | None = None) -> Gateway:
        raw = self._get_item(_M, "settings", "get_gateway", uuid)
        return Gateway.model_validate(raw.get("gateway", raw))

    def add_gateway(self, gateway: Gateway) -> ApiResponse:
        return self._add_item(_M, "settings", "add_gateway", {"gateway": gateway.model_dump(exclude_none=True)})

    def set_gateway(self, uuid: str, gateway: Gateway) -> ApiResponse:
        return self._set_item(_M, "settings", "set_gateway", uuid, {"gateway": gateway.model_dump(exclude_none=True)})

    def del_gateway(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_gateway", uuid)

    def toggle_gateway(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_gateway", uuid, enabled)

    def reconfigure(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/reconfigure")
        return ApiResponse.model_validate(raw)
