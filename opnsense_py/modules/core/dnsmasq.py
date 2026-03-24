from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.dnsmasq import DnsmasqDomainOverride, DnsmasqHost
from opnsense_py.modules.base import BaseModule

_M = "dnsmasq"


class DnsmasqModule(BaseModule):
    """Wrapper for the OPNsense Dnsmasq API."""

    # -- Settings (global) -------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def get_tag_list(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/get_tag_list")

    def download_hosts(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/download_hosts")

    def upload_hosts(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/upload_hosts", json=data)
        return ApiResponse.model_validate(raw)

    # -- Hosts -------------------------------------------------------------

    def search_hosts(self, request: SearchRequest | None = None) -> SearchResponse[DnsmasqHost]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_host", json=req.model_dump())
        return SearchResponse[DnsmasqHost].model_validate(raw)

    def get_host(self, uuid: str | None = None) -> DnsmasqHost:
        raw = self._get_item(_M, "settings", "get_host", uuid)
        return DnsmasqHost.model_validate(raw.get("host", raw))

    def add_host(self, host: DnsmasqHost) -> ApiResponse:
        return self._add_item(_M, "settings", "add_host", {"host": host.model_dump(exclude_none=True)})

    def set_host(self, uuid: str, host: DnsmasqHost) -> ApiResponse:
        return self._set_item(_M, "settings", "set_host", uuid, {"host": host.model_dump(exclude_none=True)})

    def del_host(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_host", uuid)

    # -- Domains -----------------------------------------------------------

    def search_domains(self, request: SearchRequest | None = None) -> SearchResponse[DnsmasqDomainOverride]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_domain", json=req.model_dump())
        return SearchResponse[DnsmasqDomainOverride].model_validate(raw)

    def get_domain(self, uuid: str | None = None) -> DnsmasqDomainOverride:
        raw = self._get_item(_M, "settings", "get_domain", uuid)
        return DnsmasqDomainOverride.model_validate(raw.get("domainoverride", raw))

    def add_domain(self, domain: DnsmasqDomainOverride) -> ApiResponse:
        return self._add_item(_M, "settings", "add_domain", {"domainoverride": domain.model_dump(exclude_none=True)})

    def set_domain(self, uuid: str, domain: DnsmasqDomainOverride) -> ApiResponse:
        return self._set_item(_M, "settings", "set_domain", uuid, {"domainoverride": domain.model_dump(exclude_none=True)})

    def del_domain(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_domain", uuid)

    # -- DHCP Ranges -------------------------------------------------------

    def search_ranges(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_range", request)

    def get_range(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_range", uuid)

    def add_range(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_range", data)

    def set_range(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_range", uuid, data)

    def del_range(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_range", uuid)

    # -- Tags --------------------------------------------------------------

    def search_tags(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_tag", request)

    def get_tag(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_tag", uuid)

    def add_tag(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_tag", data)

    def set_tag(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_tag", uuid, data)

    def del_tag(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_tag", uuid)

    # -- Options -----------------------------------------------------------

    def search_options(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_option", request)

    def get_option(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_option", uuid)

    def add_option(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_option", data)

    def set_option(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_option", uuid, data)

    def del_option(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_option", uuid)

    # -- Boot entries ------------------------------------------------------

    def search_boots(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_boot", request)

    def get_boot(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_boot", uuid)

    def add_boot(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_boot", data)

    def set_boot(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_boot", uuid, data)

    def del_boot(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_boot", uuid)

    # -- Leases ------------------------------------------------------------

    def search_leases(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/leases/search")

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
