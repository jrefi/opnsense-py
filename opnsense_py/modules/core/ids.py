from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.ids import IDSPolicy, IDSUserRule
from opnsense_py.modules.base import BaseModule

_M = "ids"


class IdsModule(BaseModule):
    """Wrapper for the OPNsense IDS/IPS API."""

    # -- Settings (global) -------------------------------------------------

    def get(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    # -- Policies ----------------------------------------------------------

    def search_policies(self, request: SearchRequest | None = None) -> SearchResponse[IDSPolicy]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_policy", json=req.model_dump())
        return SearchResponse[IDSPolicy].model_validate(raw)

    def get_policy(self, uuid: str | None = None) -> IDSPolicy:
        raw = self._get_item(_M, "settings", "get_policy", uuid)
        return IDSPolicy.model_validate(raw.get("policy", raw))

    def add_policy(self, policy: IDSPolicy) -> ApiResponse:
        return self._add_item(_M, "settings", "add_policy", {"policy": policy.model_dump(exclude_none=True)})

    def set_policy(self, uuid: str, policy: IDSPolicy) -> ApiResponse:
        return self._set_item(_M, "settings", "set_policy", uuid, {"policy": policy.model_dump(exclude_none=True)})

    def del_policy(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_policy", uuid)

    def toggle_policy(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_policy", uuid, enabled)

    # -- Policy rules ------------------------------------------------------

    def search_policy_rules(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "settings", "search_policy_rule", request)

    def get_policy_rule(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "settings", "get_policy_rule", uuid)

    def add_policy_rule(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "settings", "add_policy_rule", data)

    def set_policy_rule(self, uuid: str, data: dict[str, Any]) -> ApiResponse:
        return self._set_item(_M, "settings", "set_policy_rule", uuid, data)

    def del_policy_rule(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_policy_rule", uuid)

    def toggle_policy_rule(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_policy_rule", uuid, enabled)

    def check_policy_rule(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/check_policy_rule")

    # -- User rules --------------------------------------------------------

    def search_user_rules(self, request: SearchRequest | None = None) -> SearchResponse[IDSUserRule]:
        req = request or SearchRequest()
        raw = self._client._post(f"{_M}/settings/search_user_rule", json=req.model_dump())
        return SearchResponse[IDSUserRule].model_validate(raw)

    def get_user_rule(self, uuid: str | None = None) -> IDSUserRule:
        raw = self._get_item(_M, "settings", "get_user_rule", uuid)
        return IDSUserRule.model_validate(raw.get("rule", raw))

    def add_user_rule(self, rule: IDSUserRule) -> ApiResponse:
        return self._add_item(_M, "settings", "add_user_rule", {"rule": rule.model_dump(exclude_none=True)})

    def set_user_rule(self, uuid: str, rule: IDSUserRule) -> ApiResponse:
        return self._set_item(_M, "settings", "set_user_rule", uuid, {"rule": rule.model_dump(exclude_none=True)})

    def del_user_rule(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_user_rule", uuid)

    def toggle_user_rule(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_user_rule", uuid, enabled)

    # -- Rulesets ----------------------------------------------------------

    def list_rulesets(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/list_rulesets")

    def get_ruleset(self, ruleset_id: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/get_ruleset/{ruleset_id}")

    def set_ruleset(self, filename: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/set_ruleset/{filename}", json=data)
        return ApiResponse.model_validate(raw)

    def get_ruleset_properties(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/get_rulesetproperties")

    def set_ruleset_properties(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/set_rulesetproperties", json=data)
        return ApiResponse.model_validate(raw)

    def toggle_ruleset(self, filenames: str, enabled: bool | None = None) -> ApiResponse:
        path = f"{_M}/settings/toggle_ruleset/{filenames}"
        if enabled is not None:
            path = f"{path}/{int(enabled)}"
        raw = self._client._post(path)
        return ApiResponse.model_validate(raw)

    def search_installed_rules(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._client._post(f"{_M}/settings/search_installed_rules", json=data or {})

    def get_rule_info(self, sid: str | None = None) -> dict[str, Any]:
        path = f"{_M}/settings/get_rule_info"
        if sid:
            path = f"{path}/{sid}"
        return self._client._get(path)

    def list_rule_metadata(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/settings/list_rule_metadata")

    def set_rule(self, sid: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/set_rule/{sid}", json=data)
        return ApiResponse.model_validate(raw)

    def toggle_rule(self, sids: str, enabled: bool | None = None) -> ApiResponse:
        path = f"{_M}/settings/toggle_rule/{sids}"
        if enabled is not None:
            path = f"{path}/{int(enabled)}"
        raw = self._client._post(path)
        return ApiResponse.model_validate(raw)

    # -- Service -----------------------------------------------------------

    def start(self) -> ApiResponse:
        return self._service_start(_M)

    def stop(self) -> ApiResponse:
        return self._service_stop(_M)

    def restart(self) -> ApiResponse:
        return self._service_restart(_M)

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)

    def reload_rules(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/service/reload_rules"))

    def update_rules(self, wait: bool | None = None) -> ApiResponse:
        path = f"{_M}/service/update_rules"
        if wait is not None:
            path = f"{path}/{int(wait)}"
        return ApiResponse.model_validate(self._client._post(path))

    def status(self) -> dict[str, Any]:
        return self._service_status(_M)

    def get_alert_logs(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/service/get_alert_logs")

    def get_alert_info(self, alert_id: str, file_id: str = "") -> dict[str, Any]:
        path = f"{_M}/service/get_alert_info/{alert_id}"
        if file_id:
            path = f"{path}/{file_id}"
        return self._client._get(path)

    def query_alerts(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._client._post(f"{_M}/service/query_alerts", json=data or {})

    def drop_alert_log(self) -> ApiResponse:
        return ApiResponse.model_validate(self._client._post(f"{_M}/service/drop_alert_log"))
