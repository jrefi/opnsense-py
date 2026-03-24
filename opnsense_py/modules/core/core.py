from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.core import SystemService, Tunable
from opnsense_py.modules.base import BaseModule

_M = "core"


class CoreModule(BaseModule):
    """Wrapper for the OPNsense Core system API."""

    # -- Backup ------------------------------------------------------------

    def list_backups(self, host: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/backup/backups/{host}")

    def download_backup(self, host: str, backup: str | None = None) -> dict[str, Any]:
        path = f"{_M}/backup/download/{host}"
        if backup:
            path = f"{path}/{backup}"
        return self._client._get(path)

    def diff_backups(self, host: str, backup1: str, backup2: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/backup/diff/{host}/{backup1}/{backup2}")

    def delete_backup(self, backup: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/backup/delete_backup/{backup}")
        return ApiResponse.model_validate(raw)

    def revert_backup(self, backup: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/backup/revert_backup/{backup}")
        return ApiResponse.model_validate(raw)

    def backup_providers(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/backup/providers")

    # -- Dashboard ---------------------------------------------------------

    def get_dashboard(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/dashboard/get_dashboard")

    def dashboard_picture(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/dashboard/picture")

    def product_info_feed(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/dashboard/product_info_feed")

    def dashboard_restore_defaults(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/dashboard/restore_defaults")
        return ApiResponse.model_validate(raw)

    def dashboard_save_widgets(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/dashboard/save_widgets", json=data)
        return ApiResponse.model_validate(raw)

    # -- Defaults ----------------------------------------------------------

    def get_defaults(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/defaults/get")

    def get_installed_sections(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/defaults/get_installed_sections")

    def reset_defaults(self, data: dict[str, Any] | None = None) -> ApiResponse:
        raw = self._client._post(f"{_M}/defaults/reset", json=data or {})
        return ApiResponse.model_validate(raw)

    def factory_defaults(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/defaults/factory_defaults")
        return ApiResponse.model_validate(raw)

    # -- HA Sync -----------------------------------------------------------

    def get_hasync(self) -> dict[str, Any]:
        return self._get_config(_M, "hasync")

    def set_hasync(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "hasync", data)

    def reconfigure_hasync(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/hasync/reconfigure")
        return ApiResponse.model_validate(raw)

    # -- HA Sync Status ----------------------------------------------------

    def hasync_services(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/hasync_status/services")

    def hasync_version(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/hasync_status/version")

    def hasync_remote_service(self, action: str, service: str, service_id: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/hasync_status/remote_service/{action}/{service}/{service_id}")

    def hasync_restart(self, service: str | None = None, service_id: str | None = None) -> ApiResponse:
        path = f"{_M}/hasync_status/restart"
        if service:
            path = f"{path}/{service}"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    def hasync_restart_all(self, service: str | None = None, service_id: str | None = None) -> ApiResponse:
        path = f"{_M}/hasync_status/restart_all"
        if service:
            path = f"{path}/{service}"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    def hasync_start(self, service: str | None = None, service_id: str | None = None) -> ApiResponse:
        path = f"{_M}/hasync_status/start"
        if service:
            path = f"{path}/{service}"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    def hasync_stop(self, service: str | None = None, service_id: str | None = None) -> ApiResponse:
        path = f"{_M}/hasync_status/stop"
        if service:
            path = f"{path}/{service}"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    # -- Initial Setup -----------------------------------------------------

    def get_initial_setup(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/initial_setup/get")

    def set_initial_setup(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/initial_setup/set", json=data)
        return ApiResponse.model_validate(raw)

    def configure_initial_setup(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/initial_setup/configure")

    def abort_initial_setup(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/initial_setup/abort")
        return ApiResponse.model_validate(raw)

    # -- Menu --------------------------------------------------------------

    def search_menu(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/menu/search")

    def menu_tree(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/menu/tree")

    # -- Service -----------------------------------------------------------

    def search_services(self) -> SearchResponse[SystemService]:
        raw = self._client._get(f"{_M}/service/search")
        return SearchResponse[SystemService].model_validate(raw)

    def start_service(self, name: str, service_id: str = "") -> ApiResponse:
        path = f"{_M}/service/start/{name}"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    def stop_service(self, name: str, service_id: str = "") -> ApiResponse:
        path = f"{_M}/service/stop/{name}"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    def restart_service(self, name: str, service_id: str = "") -> ApiResponse:
        path = f"{_M}/service/restart/{name}"
        if service_id:
            path = f"{path}/{service_id}"
        return ApiResponse.model_validate(self._client._post(path))

    # -- Snapshots ---------------------------------------------------------

    def is_snapshots_supported(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/snapshots/is_supported")

    def search_snapshots(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/snapshots/search")

    def get_snapshot(self, uuid: str | None = None) -> dict[str, Any]:
        path = f"{_M}/snapshots/get"
        if uuid:
            path = f"{path}/{uuid}"
        return self._client._get(path)

    def add_snapshot(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/snapshots/add", json=data)
        return ApiResponse.model_validate(raw)

    def set_snapshot(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/snapshots/set/{uuid}", json=data)
        return ApiResponse.model_validate(raw)

    def del_snapshot(self, uuid: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/snapshots/del/{uuid}")
        return ApiResponse.model_validate(raw)

    def activate_snapshot(self, uuid: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/snapshots/activate/{uuid}")
        return ApiResponse.model_validate(raw)

    # -- System ------------------------------------------------------------

    def system_status(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/system/status")

    def dismiss_status(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/system/dismiss_status")
        return ApiResponse.model_validate(raw)

    def reboot(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/system/reboot")
        return ApiResponse.model_validate(raw)

    def halt(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/system/halt")
        return ApiResponse.model_validate(raw)

    # -- Tunables ----------------------------------------------------------

    def get_tunables(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/tunables/get")

    def set_tunables(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/tunables/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_tunables(self, request: SearchRequest | None = None) -> SearchResponse[Tunable]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/tunables/search_item", json=req.model_dump())
        return SearchResponse[Tunable].model_validate(raw)

    def get_tunable(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "tunables", "get_item", uuid)

    def add_tunable(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "tunables", "add_item", data)

    def set_tunable(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "tunables", "set_item", uuid, data)

    def del_tunable(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "tunables", "del_item", uuid)

    def reset_tunables(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/tunables/reset")
        return ApiResponse.model_validate(raw)

    def reconfigure_tunables(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/tunables/reconfigure")
        return ApiResponse.model_validate(raw)
