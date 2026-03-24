from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class SyslogDestination(OPNsenseModel):
    """A syslog remote destination (syslog/destination)."""

    enabled: str | None = None
    transport: str | None = None
    program: str | None = None
    level: str | None = None
    facility: str | None = None
    hostname: str | None = None
    certificate: str | None = None
    port: str | None = None
    rfc5424: str | None = None
    description: str | None = None
