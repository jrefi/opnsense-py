from __future__ import annotations

from typing import Any

from opnsense_py.modules.base import BaseModule

_M = "ntpd"


class NtpdModule(BaseModule):
    """Wrapper for the OPNsense NTPd API (ntpd/service)."""

    def gps(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/gps")

    def meta(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/meta")

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)
