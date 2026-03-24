from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Generator

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.firewall import (
    DNatRule,
    FilterRule,
    FirewallAlias,
    FirewallCategory,
    NPTRule,
    OneToOneRule,
    SNatRule,
)
from opnsense_py.modules.base import BaseModule

_M = "firewall"


class FirewallModule(BaseModule):
    """
    Wrapper for the OPNsense Firewall API.

    Covers: alias, alias_util, category, filter, d_nat, source_nat, npt,
    one_to_one, group, filter_util, migration.

    Savepoint / rollback
    --------------------
    Use the ``savepoint()`` context manager before making rule changes that
    should be revertible.  The OPNsense server will auto-revert after 60 s
    unless ``cancel_rollback()`` is called explicitly inside the ``with``
    block::

        with client.firewall.savepoint("filter") as revision:
            client.firewall.toggle_filter_rule(uuid, enabled=False)
            client.firewall.apply(revision)
            client.firewall.cancel_rollback(revision)
            # Changes are now permanent.
    """

    # ------------------------------------------------------------------ #
    # Savepoint helpers (FilterBaseController — shared by all rule types)  #
    # ------------------------------------------------------------------ #

    @contextmanager
    def savepoint(self, controller: str = "filter") -> Generator[str, None, None]:
        """
        Context manager that creates a savepoint and yields the revision token.

        On exception (or if cancel_rollback is never called), the server
        auto-reverts after 60 seconds.  Call ``cancel_rollback(revision)``
        inside the block to make changes permanent.
        """
        raw = self._client._post(f"{_M}/{controller}/savepoint")
        revision: str = raw["revision"]
        try:
            yield revision
        except Exception:
            raise

    def apply(
        self,
        rollback_revision: str | None = None,
        controller: str = "filter",
    ) -> ApiResponse:
        path = f"{_M}/{controller}/apply"
        if rollback_revision:
            path = f"{path}/{rollback_revision}"
        return ApiResponse.model_validate(self._client._post(path))

    def cancel_rollback(
        self, rollback_revision: str, controller: str = "filter"
    ) -> ApiResponse:
        raw = self._client._post(
            f"{_M}/{controller}/cancel_rollback/{rollback_revision}"
        )
        return ApiResponse.model_validate(raw)

    def revert(self, revision: str, controller: str = "filter") -> ApiResponse:
        raw = self._client._post(f"{_M}/{controller}/revert/{revision}")
        return ApiResponse.model_validate(raw)

    def get_filter_base(self, controller: str = "filter") -> dict[str, Any]:
        return self._client._get(f"{_M}/{controller}/get")

    def set_filter_base(
        self, data: dict[str, Any], controller: str = "filter"
    ) -> ApiResponse:
        raw = self._client._post(f"{_M}/{controller}/set", json=data)
        return ApiResponse.model_validate(raw)

    def list_filter_categories(self, controller: str = "filter") -> dict[str, Any]:
        return self._client._get(f"{_M}/{controller}/list_categories")

    def list_network_select_options(self, controller: str = "filter") -> dict[str, Any]:
        return self._client._get(f"{_M}/{controller}/list_network_select_options")

    def list_port_select_options(self, controller: str = "filter") -> dict[str, Any]:
        return self._client._get(f"{_M}/{controller}/list_port_select_options")

    # ------------------------------------------------------------------ #
    # Aliases (AliasController)                                           #
    # ------------------------------------------------------------------ #

    def get_alias_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/get")

    def set_alias_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/alias/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_aliases(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[FirewallAlias]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/alias/search_item", json=req.model_dump())
        return SearchResponse[FirewallAlias].model_validate(raw)

    def get_alias(self, uuid: str | None = None) -> FirewallAlias:
        raw = self._get_item(_M, "alias", "get_item", uuid)
        return FirewallAlias.model_validate(raw.get("alias", raw))

    def add_alias(self, alias: FirewallAlias) -> ApiResponse:
        return self._add_item(_M, "alias", "add_item", {"alias": alias.model_dump(exclude_none=True)})

    def set_alias(self, uuid: str, alias: FirewallAlias) -> ApiResponse:
        return self._set_item(_M, "alias", "set_item", uuid, {"alias": alias.model_dump(exclude_none=True)})

    def del_alias(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "alias", "del_item", uuid)

    def toggle_alias(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "alias", "toggle_item", uuid, enabled)

    def get_alias_uuid(self, name: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/get_alias_u_u_i_d/{name}")

    def get_geo_ip(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/get_geo_i_p")

    def get_table_size(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/get_table_size")

    def alias_list_categories(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/list_categories")

    def list_countries(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/list_countries")

    def list_network_aliases(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/list_network_aliases")

    def list_user_groups(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/list_user_groups")

    def export_aliases(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias/export")

    def import_aliases(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/alias/import", json=data)
        return ApiResponse.model_validate(raw)

    def reconfigure_aliases(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/alias/reconfigure")
        return ApiResponse.model_validate(raw)

    # ------------------------------------------------------------------ #
    # Alias utilities (AliasUtilController)                               #
    # ------------------------------------------------------------------ #

    def alias_util_add(self, alias: str, data: dict[str, Any] | None = None) -> ApiResponse:
        raw = self._client._post(f"{_M}/alias_util/add/{alias}", json=data or {})
        return ApiResponse.model_validate(raw)

    def alias_util_delete(self, alias: str, data: dict[str, Any] | None = None) -> ApiResponse:
        raw = self._client._post(f"{_M}/alias_util/delete/{alias}", json=data or {})
        return ApiResponse.model_validate(raw)

    def alias_util_flush(self, alias: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/alias_util/flush/{alias}")
        return ApiResponse.model_validate(raw)

    def alias_util_find_references(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._client._post(f"{_M}/alias_util/find_references", json=data or {})

    def alias_util_list(self, alias: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias_util/list/{alias}")

    def alias_util_aliases(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias_util/aliases")

    def alias_util_update_bogons(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/alias_util/update_bogons")

    # ------------------------------------------------------------------ #
    # Categories (CategoryController)                                     #
    # ------------------------------------------------------------------ #

    def get_category_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/category/get")

    def set_category_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/category/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_categories(
        self, request: SearchRequest | None = None, add_empty: int = 0
    ) -> SearchResponse[FirewallCategory]:
        req = request or SearchRequest()
        raw = self._client._post(
            f"{_M}/category/search_item",
            json={**req.model_dump(), "add_empty": add_empty},
        )
        return SearchResponse[FirewallCategory].model_validate(raw)

    def get_category(self, uuid: str | None = None) -> FirewallCategory:
        raw = self._get_item(_M, "category", "get_item", uuid)
        return FirewallCategory.model_validate(raw.get("category", raw))

    def add_category(self, category: FirewallCategory) -> ApiResponse:
        return self._add_item(_M, "category", "add_item", {"category": category.model_dump(exclude_none=True)})

    def set_category(self, uuid: str, category: FirewallCategory) -> ApiResponse:
        return self._set_item(_M, "category", "set_item", uuid, {"category": category.model_dump(exclude_none=True)})

    def del_category(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "category", "del_item", uuid)

    # ------------------------------------------------------------------ #
    # Filter rules (FilterController)                                     #
    # ------------------------------------------------------------------ #

    def search_filter_rules(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[FilterRule]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/filter/search_rule", json=req.model_dump())
        return SearchResponse[FilterRule].model_validate(raw)

    def get_filter_rule(self, uuid: str | None = None) -> FilterRule:
        raw = self._get_item(_M, "filter", "get_rule", uuid)
        return FilterRule.model_validate(raw.get("rule", raw))

    def add_filter_rule(self, rule: FilterRule) -> ApiResponse:
        return self._add_item(_M, "filter", "add_rule", {"rule": rule.model_dump(exclude_none=True)})

    def set_filter_rule(self, uuid: str, rule: FilterRule) -> ApiResponse:
        return self._set_item(_M, "filter", "set_rule", uuid, {"rule": rule.model_dump(exclude_none=True)})

    def del_filter_rule(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "filter", "del_rule", uuid)

    def toggle_filter_rule(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "filter", "toggle_rule", uuid, enabled)

    def toggle_filter_rule_log(self, uuid: str, log: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/filter/toggle_rule_log/{uuid}/{log}")

    def move_filter_rule_before(
        self, selected_uuid: str, target_uuid: str
    ) -> dict[str, Any]:
        return self._client._get(
            f"{_M}/filter/move_rule_before/{selected_uuid}/{target_uuid}"
        )

    def download_filter_rules(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/filter/download_rules")

    def upload_filter_rules(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/filter/upload_rules", json=data)
        return ApiResponse.model_validate(raw)

    def flush_inspect_cache(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/filter/flush_inspect_cache")
        return ApiResponse.model_validate(raw)

    def get_filter_interface_list(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/filter/get_interface_list")

    def filter_rule_stats(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/filter_util/rule_stats")

    # ------------------------------------------------------------------ #
    # Groups (GroupController)                                            #
    # ------------------------------------------------------------------ #

    def get_group_config(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/group/get")

    def set_group_config(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/group/set", json=data)
        return ApiResponse.model_validate(raw)

    def search_groups(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "group", "search_item", request)

    def get_group(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "group", "get_item", uuid)

    def add_group(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "group", "add_item", data)

    def set_group(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "group", "set_item", uuid, data)

    def del_group(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "group", "del_item", uuid)

    def reconfigure_groups(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/group/reconfigure")
        return ApiResponse.model_validate(raw)

    # ------------------------------------------------------------------ #
    # Destination NAT — DNatController (extends FilterBaseController)     #
    # ------------------------------------------------------------------ #

    def search_dnat_rules(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[DNatRule]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/d_nat/search_rule", json=req.model_dump())
        return SearchResponse[DNatRule].model_validate(raw)

    def get_dnat_rule(self, uuid: str | None = None) -> DNatRule:
        raw = self._get_item(_M, "d_nat", "get_rule", uuid)
        return DNatRule.model_validate(raw.get("rule", raw))

    def add_dnat_rule(self, rule: DNatRule) -> ApiResponse:
        return self._add_item(_M, "d_nat", "add_rule", {"rule": rule.model_dump(exclude_none=True)})

    def set_dnat_rule(self, uuid: str, rule: DNatRule) -> ApiResponse:
        return self._set_item(_M, "d_nat", "set_rule", uuid, {"rule": rule.model_dump(exclude_none=True)})

    def del_dnat_rule(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "d_nat", "del_rule", uuid)

    def toggle_dnat_rule(self, uuid: str, disabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "d_nat", "toggle_rule", uuid, disabled)

    def toggle_dnat_rule_log(self, uuid: str, log: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/d_nat/toggle_rule_log/{uuid}/{log}")

    def move_dnat_rule_before(
        self, selected_uuid: str, target_uuid: str
    ) -> dict[str, Any]:
        return self._client._get(
            f"{_M}/d_nat/move_rule_before/{selected_uuid}/{target_uuid}"
        )

    # ------------------------------------------------------------------ #
    # Source NAT (SourceNatController)                                    #
    # ------------------------------------------------------------------ #

    def search_snat_rules(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[SNatRule]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/source_nat/search_rule", json=req.model_dump())
        return SearchResponse[SNatRule].model_validate(raw)

    def get_snat_rule(self, uuid: str | None = None) -> SNatRule:
        raw = self._get_item(_M, "source_nat", "get_rule", uuid)
        return SNatRule.model_validate(raw.get("rule", raw))

    def add_snat_rule(self, rule: SNatRule) -> ApiResponse:
        return self._add_item(_M, "source_nat", "add_rule", {"rule": rule.model_dump(exclude_none=True)})

    def set_snat_rule(self, uuid: str, rule: SNatRule) -> ApiResponse:
        return self._set_item(_M, "source_nat", "set_rule", uuid, {"rule": rule.model_dump(exclude_none=True)})

    def del_snat_rule(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "source_nat", "del_rule", uuid)

    def toggle_snat_rule(self, uuid: str, disabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "source_nat", "toggle_rule", uuid, disabled)

    def toggle_snat_rule_log(self, uuid: str, log: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/source_nat/toggle_rule_log/{uuid}/{log}")

    def move_snat_rule_before(
        self, selected_uuid: str, target_uuid: str
    ) -> dict[str, Any]:
        return self._client._get(
            f"{_M}/source_nat/move_rule_before/{selected_uuid}/{target_uuid}"
        )

    # ------------------------------------------------------------------ #
    # NPT (NptController)                                                 #
    # ------------------------------------------------------------------ #

    def search_npt_rules(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[NPTRule]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/npt/search_rule", json=req.model_dump())
        return SearchResponse[NPTRule].model_validate(raw)

    def get_npt_rule(self, uuid: str | None = None) -> NPTRule:
        raw = self._get_item(_M, "npt", "get_rule", uuid)
        return NPTRule.model_validate(raw.get("rule", raw))

    def add_npt_rule(self, rule: NPTRule) -> ApiResponse:
        return self._add_item(_M, "npt", "add_rule", {"rule": rule.model_dump(exclude_none=True)})

    def set_npt_rule(self, uuid: str, rule: NPTRule) -> ApiResponse:
        return self._set_item(_M, "npt", "set_rule", uuid, {"rule": rule.model_dump(exclude_none=True)})

    def del_npt_rule(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "npt", "del_rule", uuid)

    def toggle_npt_rule(self, uuid: str, disabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "npt", "toggle_rule", uuid, disabled)

    def toggle_npt_rule_log(self, uuid: str, log: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/npt/toggle_rule_log/{uuid}/{log}")

    def move_npt_rule_before(
        self, selected_uuid: str, target_uuid: str
    ) -> dict[str, Any]:
        return self._client._get(
            f"{_M}/npt/move_rule_before/{selected_uuid}/{target_uuid}"
        )

    # ------------------------------------------------------------------ #
    # One-to-one NAT (OneToOneController)                                 #
    # ------------------------------------------------------------------ #

    def search_one_to_one_rules(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[OneToOneRule]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/one_to_one/search_rule", json=req.model_dump())
        return SearchResponse[OneToOneRule].model_validate(raw)

    def get_one_to_one_rule(self, uuid: str | None = None) -> OneToOneRule:
        raw = self._get_item(_M, "one_to_one", "get_rule", uuid)
        return OneToOneRule.model_validate(raw.get("rule", raw))

    def add_one_to_one_rule(self, rule: OneToOneRule) -> ApiResponse:
        return self._add_item(_M, "one_to_one", "add_rule", {"rule": rule.model_dump(exclude_none=True)})

    def set_one_to_one_rule(self, uuid: str, rule: OneToOneRule) -> ApiResponse:
        return self._set_item(_M, "one_to_one", "set_rule", uuid, {"rule": rule.model_dump(exclude_none=True)})

    def del_one_to_one_rule(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "one_to_one", "del_rule", uuid)

    def toggle_one_to_one_rule(
        self, uuid: str, disabled: bool | None = None
    ) -> ApiResponse:
        return self._toggle_item(_M, "one_to_one", "toggle_rule", uuid, disabled)

    def toggle_one_to_one_rule_log(self, uuid: str, log: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/one_to_one/toggle_rule_log/{uuid}/{log}")

    def move_one_to_one_rule_before(
        self, selected_uuid: str, target_uuid: str
    ) -> dict[str, Any]:
        return self._client._get(
            f"{_M}/one_to_one/move_rule_before/{selected_uuid}/{target_uuid}"
        )

    # ------------------------------------------------------------------ #
    # Migration (MigrationController)                                     #
    # ------------------------------------------------------------------ #

    def migration_download_rules(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/migration/download_rules")

    def migration_flush(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/migration/flush")
        return ApiResponse.model_validate(raw)
