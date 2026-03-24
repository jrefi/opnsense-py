from __future__ import annotations

from typing import Any

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.modules.base import BaseModule

_M = "trust"


class TrustModule(BaseModule):
    """Wrapper for the OPNsense Trust (certificates) API."""

    # -- Certificate Authorities -------------------------------------------

    def search_cas(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "ca", "search", request)

    def get_ca(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "ca", "get", uuid)

    def add_ca(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "ca", "add", data)

    def set_ca(self, uuid: str | None, data: dict[str, Any]) -> ApiResponse:
        path = f"{_M}/ca/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json=data)
        return ApiResponse.model_validate(raw)

    def del_ca(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "ca", "del", uuid)

    def ca_info(self, caref: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/ca/ca_info/{caref}")

    def ca_list(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/ca/ca_list")

    def generate_ca_file(self, uuid: str | None = None, file_type: str = "crt") -> ApiResponse:
        path = f"{_M}/ca/generate_file"
        if uuid is not None:
            path = f"{path}/{uuid}"
        raw = self._client._post(f"{path}/{file_type}")
        return ApiResponse.model_validate(raw)

    def raw_dump_ca(self, uuid: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/ca/raw_dump/{uuid}")

    # -- Certificates ------------------------------------------------------

    def search_certs(self, request: SearchRequest | None = None) -> SearchResponse[dict[str, Any]]:
        return self._search(_M, "cert", "search", request)

    def get_cert(self, uuid: str | None = None) -> dict[str, Any]:
        return self._get_item(_M, "cert", "get", uuid)

    def add_cert(self, data: dict[str, Any]) -> ApiResponse:
        return self._add_item(_M, "cert", "add", data)

    def set_cert(self, uuid: str | None, data: dict[str, Any]) -> ApiResponse:
        path = f"{_M}/cert/set"
        if uuid:
            path = f"{path}/{uuid}"
        raw = self._client._post(path, json=data)
        return ApiResponse.model_validate(raw)

    def del_cert(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "cert", "del", uuid)

    def cert_ca_info(self, caref: str | None = None) -> dict[str, Any]:
        path = f"{_M}/cert/ca_info"
        if caref:
            path = f"{path}/{caref}"
        return self._client._get(path)

    def cert_ca_list(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/cert/ca_list")

    def cert_user_list(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/cert/user_list")

    def generate_cert_file(self, uuid: str | None = None, file_type: str = "crt") -> ApiResponse:
        path = f"{_M}/cert/generate_file"
        if uuid is not None:
            path = f"{path}/{uuid}"
        raw = self._client._post(f"{path}/{file_type}")
        return ApiResponse.model_validate(raw)

    def raw_dump_cert(self, uuid: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/cert/raw_dump/{uuid}")

    # -- CRL ---------------------------------------------------------------

    def search_crls(self) -> dict[str, Any]:
        return self._client._get(f"{_M}/crl/search")

    def get_crl(self, caref: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/crl/get/{caref}")

    def set_crl(self, caref: str, data: dict[str, Any]) -> ApiResponse:
        raw = self._client._post(f"{_M}/crl/set/{caref}", json=data)
        return ApiResponse.model_validate(raw)

    def del_crl(self, caref: str) -> ApiResponse:
        raw = self._client._post(f"{_M}/crl/del/{caref}")
        return ApiResponse.model_validate(raw)

    def get_crl_ocsp_info(self, caref: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/crl/get_ocsp_info_data/{caref}")

    def raw_dump_crl(self, caref: str) -> dict[str, Any]:
        return self._client._get(f"{_M}/crl/raw_dump/{caref}")

    # -- Settings ----------------------------------------------------------

    def get_settings(self) -> dict[str, Any]:
        return self._get_config(_M, "settings")

    def set_settings(self, data: dict[str, Any]) -> ApiResponse:
        return self._set_config(_M, "settings", data)

    def reconfigure(self) -> ApiResponse:
        raw = self._client._post(f"{_M}/settings/reconfigure")
        return ApiResponse.model_validate(raw)
