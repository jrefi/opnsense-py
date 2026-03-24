from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse
from opnsense_py.modules.base import BaseModule

_M = "hostdiscovery"


class HostdiscoveryModule(BaseModule):
    """Wrapper for the OPNsense Host Discovery API."""

    # -- Settings ----------------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    # -- Service -----------------------------------------------------------

    def start(self) -> ApiResponse:
        return self._service_start(_M)

    def stop(self) -> ApiResponse:
        return self._service_stop(_M)

    def restart(self) -> ApiResponse:
        return self._service_restart(_M)

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def search(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/search")

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)
