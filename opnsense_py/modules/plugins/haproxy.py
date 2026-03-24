from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.modules.base import BaseModule

_M = "haproxy"


class HaproxyModule(BaseModule):
    """
    Wrapper for the OPNsense HAProxy API.

    Covers: settings (15 resource types), export, maintenance, service,
    statistics.

    Note: ``mailer`` and ``resolver`` resources use non-standard method names
    in the API (``addmailer``, ``delmailer``, etc.) which are reflected here.
    """

    # ------------------------------------------------------------------ #
    # Settings — global config                                            #
    # ------------------------------------------------------------------ #

    def get(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/get")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/set", json=data)
        return ApiResponse.model_validate(raw)

    # ------------------------------------------------------------------ #
    # Frontends                                                           #
    # ------------------------------------------------------------------ #

    def search_frontends(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_frontends", request)

    def get_frontend(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_frontend", uuid)

    def add_frontend(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_frontend", data)

    def set_frontend(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_frontend", uuid, data)

    def del_frontend(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_frontend", uuid)

    def toggle_frontend(self, uuid: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/toggle_frontend/{uuid}")
        return ApiResponse.model_validate(raw)

    # ------------------------------------------------------------------ #
    # Backends                                                            #
    # ------------------------------------------------------------------ #

    def search_backends(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_backends", request)

    def get_backend(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_backend", uuid)

    def add_backend(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_backend", data)

    def set_backend(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_backend", uuid, data)

    def del_backend(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_backend", uuid)

    def toggle_backend(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_backend", uuid, enabled)

    # ------------------------------------------------------------------ #
    # Servers                                                             #
    # ------------------------------------------------------------------ #

    def search_servers(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_servers", request)

    def get_server(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_server", uuid)

    def add_server(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_server", data)

    def set_server(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_server", uuid, data)

    def del_server(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_server", uuid)

    def toggle_server(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_server", uuid, enabled)

    # ------------------------------------------------------------------ #
    # ACLs                                                                #
    # ------------------------------------------------------------------ #

    def search_acls(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_acls", request)

    def get_acl(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_acl", uuid)

    def add_acl(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_acl", data)

    def set_acl(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_acl", uuid, data)

    def del_acl(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_acl", uuid)

    # ------------------------------------------------------------------ #
    # Actions                                                             #
    # ------------------------------------------------------------------ #

    def search_actions(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_actions", request)

    def get_action(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_action", uuid)

    def add_action(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_action", data)

    def set_action(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_action", uuid, data)

    def del_action(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_action", uuid)

    # ------------------------------------------------------------------ #
    # CPU affinity                                                        #
    # ------------------------------------------------------------------ #

    def search_cpus(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_cpus", request)

    def get_cpu(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_cpu", uuid)

    def add_cpu(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_cpu", data)

    def set_cpu(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_cpu", uuid, data)

    def del_cpu(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_cpu", uuid)

    def toggle_cpu(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_cpu", uuid, enabled)

    # ------------------------------------------------------------------ #
    # Error files                                                         #
    # ------------------------------------------------------------------ #

    def search_errorfiles(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_errorfiles", request)

    def get_errorfile(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_errorfile", uuid)

    def add_errorfile(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_errorfile", data)

    def set_errorfile(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_errorfile", uuid, data)

    def del_errorfile(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_errorfile", uuid)

    # ------------------------------------------------------------------ #
    # FastCGI                                                             #
    # ------------------------------------------------------------------ #

    def search_fcgis(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_fcgis", request)

    def get_fcgi(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_fcgi", uuid)

    def add_fcgi(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_fcgi", data)

    def set_fcgi(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_fcgi", uuid, data)

    def del_fcgi(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_fcgi", uuid)

    # ------------------------------------------------------------------ #
    # Groups                                                              #
    # ------------------------------------------------------------------ #

    def search_groups(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_groups", request)

    def get_group(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_group", uuid)

    def add_group(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_group", data)

    def set_group(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_group", uuid, data)

    def del_group(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_group", uuid)

    def toggle_group(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_group", uuid, enabled)

    # ------------------------------------------------------------------ #
    # Health checks                                                       #
    # ------------------------------------------------------------------ #

    def search_healthchecks(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_healthchecks", request)

    def get_healthcheck(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_healthcheck", uuid)

    def add_healthcheck(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_healthcheck", data)

    def set_healthcheck(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_healthcheck", uuid, data)

    def del_healthcheck(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_healthcheck", uuid)

    # ------------------------------------------------------------------ #
    # Lua scripts                                                         #
    # ------------------------------------------------------------------ #

    def search_luas(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_luas", request)

    def get_lua(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_lua", uuid)

    def add_lua(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_lua", data)

    def set_lua(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_lua", uuid, data)

    def del_lua(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_lua", uuid)

    def toggle_lua(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_lua", uuid, enabled)

    # ------------------------------------------------------------------ #
    # Map files                                                           #
    # ------------------------------------------------------------------ #

    def search_mapfiles(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_mapfiles", request)

    def get_mapfile(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_mapfile", uuid)

    def add_mapfile(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_mapfile", data)

    def set_mapfile(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_mapfile", uuid, data)

    def del_mapfile(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_mapfile", uuid)

    # ------------------------------------------------------------------ #
    # Users                                                               #
    # ------------------------------------------------------------------ #

    def search_users(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_users", request)

    def get_user(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_user", uuid)

    def add_user(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_user", data)

    def set_user(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_user", uuid, data)

    def del_user(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_user", uuid)

    def toggle_user(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_user", uuid, enabled)

    # ------------------------------------------------------------------ #
    # Mailers (non-standard API method names)                             #
    # ------------------------------------------------------------------ #

    def search_mailers(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "searchmailers", request)

    def get_mailer(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "getmailer", uuid)

    def add_mailer(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "addmailer", data)

    def set_mailer(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "setmailer", uuid, data)

    def del_mailer(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "delmailer", uuid)

    def toggle_mailer(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "togglemailer", uuid, enabled)

    # ------------------------------------------------------------------ #
    # Resolvers (non-standard API method names)                           #
    # ------------------------------------------------------------------ #

    def search_resolvers(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "searchresolvers", request)

    def get_resolver(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "getresolver", uuid)

    def add_resolver(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "addresolver", data)

    def set_resolver(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "setresolver", uuid, data)

    def del_resolver(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "delresolver", uuid)

    def toggle_resolver(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggleresolver", uuid, enabled)

    # ------------------------------------------------------------------ #
    # Export                                                              #
    # ------------------------------------------------------------------ #

    def export_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/export/config")

    def export_diff(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/export/diff")

    def export_download(self, download_type: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/export/download/{download_type}")

    # ------------------------------------------------------------------ #
    # Maintenance                                                         #
    # ------------------------------------------------------------------ #

    def get_maintenance(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/get")

    def set_maintenance(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/maintenance/set", json=data)
        return ApiResponse.model_validate(raw)

    def cert_actions(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/cert_actions")

    def cert_diff(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/cert_diff")

    def cert_sync(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/cert_sync")

    def cert_sync_bulk(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/cert_sync_bulk")

    def fetch_cron_integration(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/maintenance/fetch_cron_integration")
        return ApiResponse.model_validate(raw)

    def search_certificate_diff(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/search_certificate_diff")

    def maintenance_search_servers(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/search_server")

    def server_state(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/server_state")

    def server_state_bulk(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/server_state_bulk")

    def server_weight(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/server_weight")

    def server_weight_bulk(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/maintenance/server_weight_bulk")

    # ------------------------------------------------------------------ #
    # Statistics                                                          #
    # ------------------------------------------------------------------ #

    def stat_counters(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/statistics/counters")

    def stat_info(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/statistics/info")

    def stat_tables(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/statistics/tables")

    # ------------------------------------------------------------------ #
    # Service                                                             #
    # ------------------------------------------------------------------ #

    def start(self) -> ApiResponse:
        return self._service_start(_M)

    def stop(self) -> ApiResponse:
        return self._service_stop(_M)

    def restart(self) -> ApiResponse:
        return self._service_restart(_M)

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def configtest(self) -> dict[str, Any]:
        """Note: configtest uses GET, not POST."""
        return self._client._get(f"{_M}/service/configtest")

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)
