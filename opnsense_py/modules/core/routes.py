from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.routes import Route
from opnsense_py.modules.base import BaseModule

_M = "routes"


class RoutesModule(BaseModule):
    """Wrapper for the OPNsense Routes API (routes/routes, routes/gateway)."""

    # -- Routes ------------------------------------------------------------

    def search_routes(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[Route]:
        req = request or SearchRequest()
        raw = self._client._post(
            f"{_M}/routes/searchroute", json=req.model_dump()
        )
        return SearchResponse[Route].model_validate(raw)

    def get_route(self, uuid: str | None = None) -> Route:
        raw = self._get_item(_M, "routes", "getroute", uuid)
        return Route.model_validate(raw.get("route", raw))

    def add_route(self, route: Route) -> ApiResponse:
        return self._add_item(_M, "routes", "addroute", {"route": route.model_dump(exclude_none=True)})

    def set_route(self, uuid: str, route: Route) -> ApiResponse:
        return self._set_item(_M, "routes", "setroute", uuid, {"route": route.model_dump(exclude_none=True)})

    def del_route(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "routes", "delroute", uuid)

    def toggle_route(self, uuid: str, disabled: bool | None = None) -> ApiResponse:
        path = f"{_M}/routes/toggleroute/{uuid}"
        if disabled is not None:
            path = f"{path}/{int(disabled)}"
        return ApiResponse.model_validate(self._client._post(path))

    def reconfigure(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/routes/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- Gateway -----------------------------------------------------------

    def gateway_status(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/gateway/status")
