from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse
from opnsense_py.modules.base import BaseModule

# Firmware module uses "core" as the API module name, not "firmware"
_API = "core"
_CTL = "firmware"


class FirmwareModule(BaseModule):
    """
    Wrapper for the OPNsense Firmware API.

    Note: All API paths use ``core/firmware/...`` not ``firmware/firmware/...``.

    Long-running operations (update, upgrade, health, audit) are fire-and-observe.
    Poll ``running()`` or ``upgradestatus()`` after triggering them.
    """

    # -- Configuration -----------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._client._get(f"{_API}/{_CTL}/get")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_API}/{_CTL}/set", json=data)
        return ApiResponse.model_validate(raw)

    def get_options(self) -> dict[str, Any]:
        return self._client._get(f"{_API}/{_CTL}/get_options")

    # -- Status & info -----------------------------------------------------

    def info(self) -> dict[str, Any]:
        return self._client._get(f"{_API}/{_CTL}/info")

    def running(self) -> dict[str, Any]:
        """Check if a firmware operation is currently running."""
        return self._client._get(f"{_API}/{_CTL}/running")

    def upgradestatus(self) -> dict[str, Any]:
        """Poll upgrade progress/log after calling upgrade()."""
        return self._client._get(f"{_API}/{_CTL}/upgradestatus")

    # -- Operations (fire-and-observe) ------------------------------------

    def status(self) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/status")

    def check(self) -> dict[str, Any]:
        """Check for available updates."""
        return self._client._post(f"{_API}/{_CTL}/check")

    def update(self) -> dict[str, Any]:
        """Trigger firmware update. Poll running() for completion."""
        return self._client._post(f"{_API}/{_CTL}/update")

    def upgrade(self) -> dict[str, Any]:
        """Trigger major firmware upgrade. Poll upgradestatus() for progress."""
        return self._client._post(f"{_API}/{_CTL}/upgrade")

    def health(self) -> dict[str, Any]:
        """Run firmware health check."""
        return self._client._post(f"{_API}/{_CTL}/health")

    def audit(self) -> dict[str, Any]:
        """Run security audit."""
        return self._client._post(f"{_API}/{_CTL}/audit")

    def connection(self) -> dict[str, Any]:
        """Test firmware mirror connectivity."""
        return self._client._post(f"{_API}/{_CTL}/connection")

    def changelog(self, version: str) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/changelog/{version}")

    def log(self, clear: bool = False) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/log/{int(clear)}")

    def resync_plugins(self) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/resync_plugins")

    def sync_plugins(self) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/sync_plugins")

    # -- System power ------------------------------------------------------

    def reboot(self) -> ApiResponse:
        raw = self._client._post(f"{_API}/{_CTL}/reboot")
        return ApiResponse.model_validate(raw)

    def poweroff(self) -> ApiResponse:
        raw = self._client._post(f"{_API}/{_CTL}/poweroff")
        return ApiResponse.model_validate(raw)

    # -- Packages ----------------------------------------------------------

    def package_details(self, pkg_name: str) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/details/{pkg_name}")

    def install_package(self, pkg_name: str) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/install/{pkg_name}")

    def remove_package(self, pkg_name: str) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/remove/{pkg_name}")

    def reinstall_package(self, pkg_name: str) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/reinstall/{pkg_name}")

    def lock_package(self, pkg_name: str) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/lock/{pkg_name}")

    def unlock_package(self, pkg_name: str) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/unlock/{pkg_name}")

    def package_license(self, pkg_name: str) -> dict[str, Any]:
        return self._client._post(f"{_API}/{_CTL}/license/{pkg_name}")
