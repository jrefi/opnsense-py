from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.modules.base import BaseModule

_M = "auth"


class AuthModule(BaseModule):
    """Wrapper for the OPNsense Auth API (user, group, priv)."""

    # -- Users -------------------------------------------------------------

    def search_users(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "user", "search", request)

    def get_user(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "user", "get", uuid)

    def add_user(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "user", "add", data)

    def set_user(self, uuid: str | None, data: dict[str, Any]) -> ApiResponse:
        path = f"{_M}/user/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json=data)
        return ApiResponse.model_validate(raw)

    def del_user(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "user", "del", uuid)

    def download_users(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/user/download")

    def upload_users(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/user/upload", json=data)
        return ApiResponse.model_validate(raw)

    def new_otp_seed(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/user/new_otp_seed")

    def search_api_keys(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/user/search_api_key")

    def add_api_key(self, username: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/user/add_api_key/{username}")
        return ApiResponse.model_validate(raw)

    def del_api_key(self, key_id: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/user/del_api_key/{key_id}")
        return ApiResponse.model_validate(raw)

    # -- Groups ------------------------------------------------------------

    def search_groups(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "group", "search", request)

    def get_group(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "group", "get", uuid)

    def add_group(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "group", "add", data)

    def set_group(self, uuid: str | None, data: dict[str, Any]) -> ApiResponse:
        path = f"{_M}/group/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json=data)
        return ApiResponse.model_validate(raw)

    def del_group(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "group", "del", uuid)

    # -- Privileges --------------------------------------------------------

    def get_privileges(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/priv/get")

    def search_privileges(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/priv/search")

    def get_privilege(self, priv_id: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/priv/get_item/{priv_id}")

    def set_privileges(self, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/priv/set", json=data)
        return ApiResponse.model_validate(raw)

    def set_privilege(self, priv_id: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/priv/set_item/{priv_id}", json=data)
        return ApiResponse.model_validate(raw)
