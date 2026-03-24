from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.dhcrelay import DHCRelayDestination, DHCRelayRelay
from opnsense_py.modules.base import BaseModule

_M = "dhcrelay"


class DhcrelayModule(BaseModule):
    """Wrapper for the OPNsense DHCP Relay API."""

    # -- Settings ----------------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    # Destinations

    def search_destinations(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[DHCRelayDestination]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_dest", json=req.model_dump())
        return SearchResponse[DHCRelayDestination].model_validate(raw)

    def get_destination(self, uuid: str | None = None) -> DHCRelayDestination:
        raw = self._get_item(_M, "settings", "get_dest", uuid)
        return DHCRelayDestination.model_validate(raw.get("destination", raw))

    def add_destination(self, destination: DHCRelayDestination) -> ApiResponse:
        return self._add_item(_M, "settings", "add_dest", {"destination": destination.model_dump(exclude_none=True)})

    def set_destination(self, uuid: str, destination: DHCRelayDestination) -> ApiResponse:
        return self._set_item(_M, "settings", "set_dest", uuid, {"destination": destination.model_dump(exclude_none=True)})

    def del_destination(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_dest", uuid)

    # Relays

    def search_relays(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[DHCRelayRelay]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_relay", json=req.model_dump())
        return SearchResponse[DHCRelayRelay].model_validate(raw)

    def get_relay(self, uuid: str | None = None) -> DHCRelayRelay:
        raw = self._get_item(_M, "settings", "get_relay", uuid)
        return DHCRelayRelay.model_validate(raw.get("relay", raw))

    def add_relay(self, relay: DHCRelayRelay) -> ApiResponse:
        return self._add_item(_M, "settings", "add_relay", {"relay": relay.model_dump(exclude_none=True)})

    def set_relay(self, uuid: str, relay: DHCRelayRelay) -> ApiResponse:
        return self._set_item(_M, "settings", "set_relay", uuid, {"relay": relay.model_dump(exclude_none=True)})

    def del_relay(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_relay", uuid)

    def toggle_relay(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_relay", uuid, enabled)

    # -- Service -----------------------------------------------------------

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)
