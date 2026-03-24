from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class OPNsenseModel(BaseModel):
    """Base for all OPNsense models. Extra fields are silently accepted."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


class SearchRequest(BaseModel):
    """Standard grid search request body."""

    current: int = 1
    rowCount: int = 500
    searchPhrase: str = ""
    sort: dict[str, str] = {}


class SearchResponse(BaseModel, Generic[T]):
    """Standard grid search response envelope."""

    total: int
    rowCount: int
    current: int
    rows: list[T]

    model_config = ConfigDict(extra="allow")


class ApiResponse(BaseModel):
    """Generic envelope for simple POST responses (result/uuid)."""

    result: str | None = None
    uuid: str | None = None
    validations: dict[str, Any] | None = None

    model_config = ConfigDict(extra="allow")
