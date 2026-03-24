from __future__ import annotations

from typing import Any


class OPNsenseError(Exception):
    """Base exception for all OPNsense API errors."""


class OPNsenseHTTPError(OPNsenseError):
    """Raised when the server returns an HTTP error status."""

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        super().__init__(f"HTTP {status_code}: {message}")


class OPNsenseAuthError(OPNsenseHTTPError):
    """Raised on 401 or 403 responses."""


class OPNsenseNotFoundError(OPNsenseHTTPError):
    """Raised on 404 responses."""


class OPNsenseValidationError(OPNsenseError):
    """Raised when the API returns HTTP 200 but includes validation errors in the body."""

    def __init__(self, validations: dict[str, Any]) -> None:
        self.validations = validations
        super().__init__(f"Validation failed: {validations}")
