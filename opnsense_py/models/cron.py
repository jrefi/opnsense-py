from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class CronJob(OPNsenseModel):
    """A single cron job entry.

    Boolean fields (``enabled``) use ``"0"``/``"1"`` strings as returned by
    the OPNsense API.
    """

    origin: str | None = None
    enabled: str | None = None
    minutes: str | None = None
    hours: str | None = None
    days: str | None = None
    months: str | None = None
    weekdays: str | None = None
    who: str | None = None
    command: str | None = None
    parameters: str | None = None
    description: str | None = None
