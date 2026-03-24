from __future__ import annotations

from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse
from opnsense_py.models.cron import CronJob
from opnsense_py.modules.base import BaseModule

_M = "cron"


class CronModule(BaseModule):
    """Wrapper for the OPNsense Cron API (cron/settings, cron/service)."""

    # -- Settings ----------------------------------------------------------

    def search_jobs(
        self, request: SearchRequest | None = None
    ) -> SearchResponse[CronJob]:
        req = request or SearchRequest()
        raw = self._client._post(
            f"{_M}/settings/search_jobs", json=req.model_dump()
        )
        return SearchResponse[CronJob].model_validate(raw)

    def get_job(self, uuid: str | None = None) -> CronJob:
        raw = self._get_item(_M, "settings", "get_job", uuid)
        return CronJob.model_validate(raw.get("job", raw))

    def add_job(self, job: CronJob) -> ApiResponse:
        return self._add_item(_M, "settings", "add_job", {"job": job.model_dump(exclude_none=True)})

    def set_job(self, uuid: str, job: CronJob) -> ApiResponse:
        return self._set_item(_M, "settings", "set_job", uuid, {"job": job.model_dump(exclude_none=True)})

    def del_job(self, uuid: str) -> ApiResponse:
        return self._del_item(_M, "settings", "del_job", uuid)

    def toggle_job(self, uuid: str, enabled: bool | None = None) -> ApiResponse:
        return self._toggle_item(_M, "settings", "toggle_job", uuid, enabled)

    # -- Service -----------------------------------------------------------

    def reconfigure(self) -> ApiResponse:
        return self._service_reconfigure(_M)
