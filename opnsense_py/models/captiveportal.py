from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class CaptivePortalZone(OPNsenseModel):
    """A captive portal zone (captiveportal/settings/zone)."""

    enabled: str | None = None
    zoneid: str | None = None
    interfaces: str | None = None
    authservers: str | None = None
    idletimeout: str | None = None
    hardtimeout: str | None = None
    concurrentlogins: str | None = None
    bandwidth_up: str | None = None
    bandwidth_down: str | None = None
    description: str | None = None
