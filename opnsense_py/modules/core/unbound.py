from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.unbound import HostAlias, HostOverride, UnboundAcl, UnboundDnsbl, UnboundDot
from opnsense_py.modules.base import BaseModule

_M = "unbound"


class UnboundModule(BaseModule):
    """Wrapper for the OPNsense Unbound DNS Resolver API."""

    # -- Settings (global) -------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def get_nameservers(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/get_nameservers")

    def update_blocklist(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/update_blocklist")
        return ApiResponse.model_validate(raw)

    # -- ACLs --------------------------------------------------------------

    def search_acls(self, request: SearchRequest | None = None) -> SearchResponse[UnboundAcl]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_acl", json=req.model_dump())
        return SearchResponse[UnboundAcl].model_validate(raw)

    def get_acl(self, uuid: str | None = None) -> UnboundAcl:
        raw = self._get_item(_M, "settings", "get_acl", uuid)
        return UnboundAcl.model_validate(raw.get("acl", raw))

    def add_acl(self, acl: UnboundAcl) -> ApiResponse:
        return self._add_item(_M, "settings", "add_acl", {"acl": acl.model_dump(exclude_none=True)})

    def set_acl(self, uuid: str, acl: UnboundAcl) -> ApiResponse:
        return self._set_item(_M, "settings", "set_acl", uuid, {"acl": acl.model_dump(exclude_none=True)})

    def del_acl(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_acl", uuid)

    def toggle_acl(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_acl", uuid, enabled)

    # -- DNS Blocklist (DNSBL) ---------------------------------------------

    def search_dnsbl(self, request: SearchRequest | None = None) -> SearchResponse[UnboundDnsbl]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_dnsbl", json=req.model_dump())
        return SearchResponse[UnboundDnsbl].model_validate(raw)

    def get_dnsbl(self, uuid: str | None = None) -> UnboundDnsbl:
        raw = self._get_item(_M, "settings", "get_dnsbl", uuid)
        return UnboundDnsbl.model_validate(raw.get("blocklist", raw))

    def add_dnsbl(self, blocklist: UnboundDnsbl) -> ApiResponse:
        return self._add_item(_M, "settings", "add_dnsbl", {"blocklist": blocklist.model_dump(exclude_none=True)})

    def set_dnsbl(self, uuid: str, blocklist: UnboundDnsbl) -> ApiResponse:
        return self._set_item(_M, "settings", "set_dnsbl", uuid, {"blocklist": blocklist.model_dump(exclude_none=True)})

    def del_dnsbl(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_dnsbl", uuid)

    def toggle_dnsbl(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_dnsbl", uuid, enabled)

    # -- Forwards (DoT / upstream) ----------------------------------------

    def search_forwards(self, request: SearchRequest | None = None) -> SearchResponse[UnboundDot]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_forward", json=req.model_dump())
        return SearchResponse[UnboundDot].model_validate(raw)

    def get_forward(self, uuid: str | None = None) -> UnboundDot:
        raw = self._get_item(_M, "settings", "get_forward", uuid)
        return UnboundDot.model_validate(raw.get("dot", raw))

    def add_forward(self, dot: UnboundDot) -> ApiResponse:
        return self._add_item(_M, "settings", "add_forward", {"dot": dot.model_dump(exclude_none=True)})

    def set_forward(self, uuid: str, dot: UnboundDot) -> ApiResponse:
        return self._set_item(_M, "settings", "set_forward", uuid, {"dot": dot.model_dump(exclude_none=True)})

    def del_forward(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_forward", uuid)

    def toggle_forward(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_forward", uuid, enabled)

    # -- Host Overrides ----------------------------------------------------

    def search_host_overrides(self, request: SearchRequest | None = None) -> SearchResponse[HostOverride]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_host_override", json=req.model_dump())
        return SearchResponse[HostOverride].model_validate(raw)

    def get_host_override(self, uuid: str | None = None) -> HostOverride:
        raw = self._get_item(_M, "settings", "get_host_override", uuid)
        return HostOverride.model_validate(raw.get("host", raw))

    def add_host_override(self, host: HostOverride) -> ApiResponse:
        return self._add_item(_M, "settings", "add_host_override", {"host": host.model_dump(exclude_none=True)})

    def set_host_override(self, uuid: str, host: HostOverride) -> ApiResponse:
        return self._set_item(_M, "settings", "set_host_override", uuid, {"host": host.model_dump(exclude_none=True)})

    def del_host_override(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_host_override", uuid)

    def toggle_host_override(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_host_override", uuid, enabled)

    # -- Host Aliases ------------------------------------------------------

    def search_host_aliases(self, request: SearchRequest | None = None) -> SearchResponse[HostAlias]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_host_alias", json=req.model_dump())
        return SearchResponse[HostAlias].model_validate(raw)

    def get_host_alias(self, uuid: str | None = None) -> HostAlias:
        raw = self._get_item(_M, "settings", "get_host_alias", uuid)
        return HostAlias.model_validate(raw.get("alias", raw))

    def add_host_alias(self, alias: HostAlias) -> ApiResponse:
        return self._add_item(_M, "settings", "add_host_alias", {"alias": alias.model_dump(exclude_none=True)})

    def set_host_alias(self, uuid: str, alias: HostAlias) -> ApiResponse:
        return self._set_item(_M, "settings", "set_host_alias", uuid, {"alias": alias.model_dump(exclude_none=True)})

    def del_host_alias(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_host_alias", uuid)

    def toggle_host_alias(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_host_alias", uuid, enabled)

    # -- Diagnostics -------------------------------------------------------

    def dump_cache(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/diagnostics/dumpcache")

    def dump_infra(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/diagnostics/dumpinfra")

    def list_insecure(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/diagnostics/listinsecure")

    def list_local_data(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/diagnostics/listlocaldata")

    def list_local_zones(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/diagnostics/listlocalzones")

    def diag_stats(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/diagnostics/stats")

    def test_blocklist(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._client._post(f"{_M}/diagnostics/test_blocklist", json=data or {})

    # -- Overview ----------------------------------------------------------

    def rolling(self, timeperiod: str, clients: int = 0) -> dict[str, Any]:
        return self._client._get(f"{_M}/overview/_rolling/{timeperiod}/{clients}")

    def get_policies(self, uuid: str | None = None) -> dict[str, Any]:
        path = f"{_M}/overview/get_policies"
        if uuid:
            path = f"{path}/{uuid}"
        return self._client._get(path)

    def is_block_list_enabled(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/overview/is_block_list_enabled")

    def is_enabled(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/overview/is_enabled")

    def search_queries(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/overview/search_queries")

    def totals(self, maximum: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/overview/totals/{maximum}")

    # -- Service -----------------------------------------------------------

    def start(self) -> ApiResponse:
        return self._service_start(_M)

    def stop(self) -> ApiResponse:
        return self._service_stop(_M)

    def restart(self) -> ApiResponse:
        return self._service_restart(_M)

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def reconfigure_general(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/reconfigure_general")

    def dnsbl_status(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/dnsbl")

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)
