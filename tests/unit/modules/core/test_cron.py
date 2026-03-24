import httpx
import pytest
import respx

from opnsense_py import OPNsenseClient, OPNsenseValidationError
from opnsense_py.models.cron import CronJob


def test_search_jobs(client: OPNsenseClient, mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/cron/settings/search_jobs").mock(
        return_value=httpx.Response(
            200,
            json={
                "total": 1,
                "rowCount": 1,
                "current": 1,
                "rows": [{"uuid": "abc-123", "description": "test job"}],
            },
        )
    )
    result = client.cron.search_jobs()
    assert result.total == 1
    assert result.rows[0].uuid == "abc-123"


def test_get_job(client: OPNsenseClient, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/cron/settings/get_job/abc-123").mock(
        return_value=httpx.Response(200, json={"job": {"description": "test job"}})
    )
    result = client.cron.get_job("abc-123")
    assert result.description == "test job"


def test_add_job_success(client: OPNsenseClient, mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/cron/settings/add_job").mock(
        return_value=httpx.Response(200, json={"result": "saved", "uuid": "new-uuid"})
    )
    result = client.cron.add_job(CronJob(description="new"))
    assert result.result == "saved"
    assert result.uuid == "new-uuid"


def test_add_job_validation_error(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    mock_api.post("/api/cron/settings/add_job").mock(
        return_value=httpx.Response(
            200,
            json={
                "result": "failed",
                "validations": {"job.command": "This field is required."},
            },
        )
    )
    with pytest.raises(OPNsenseValidationError) as exc_info:
        client.cron.add_job(CronJob())
    assert "job.command" in exc_info.value.validations


def test_del_job(client: OPNsenseClient, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/cron/settings/del_job/abc-123").mock(
        return_value=httpx.Response(200, json={"result": "deleted"})
    )
    result = client.cron.del_job("abc-123")
    assert route.called
    assert result.result == "deleted"


def test_toggle_job_with_enabled_false(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    route = mock_api.post("/api/cron/settings/toggle_job/abc-123/0").mock(
        return_value=httpx.Response(200, json={"result": "saved"})
    )
    client.cron.toggle_job("abc-123", enabled=False)
    assert route.called


def test_toggle_job_without_enabled(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    route = mock_api.post("/api/cron/settings/toggle_job/abc-123").mock(
        return_value=httpx.Response(200, json={"result": "saved"})
    )
    client.cron.toggle_job("abc-123")
    assert route.called


def test_reconfigure(client: OPNsenseClient, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/cron/service/reconfigure").mock(
        return_value=httpx.Response(200, json={"result": "ok"})
    )
    client.cron.reconfigure()
    assert route.called
