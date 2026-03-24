import json

from opnsense_py.cli.output import render
from opnsense_py.models.base import ApiResponse, SearchResponse
from opnsense_py.models.cron import CronJob


def _make_search_response() -> SearchResponse[CronJob]:
    return SearchResponse[CronJob].model_validate(
        {
            "total": 2,
            "rowCount": 2,
            "current": 1,
            "rows": [
                {"uuid": "abc-1", "description": "job one", "command": "/usr/bin/true"},
                {"uuid": "abc-2", "description": "job two", "command": "/usr/bin/false"},
            ],
        }
    )


def _make_api_response() -> ApiResponse:
    return ApiResponse(result="saved", uuid="new-uuid")


# ---------------------------------------------------------------------------
# JSON format
# ---------------------------------------------------------------------------


def test_json_search_response() -> None:
    data = _make_search_response()
    out = json.loads(render(data, "json"))
    assert isinstance(out, dict)
    assert out["total"] == 2
    assert out["rows"][0]["uuid"] == "abc-1"


def test_json_api_response() -> None:
    data = _make_api_response()
    out = json.loads(render(data, "json"))
    assert out["result"] == "saved"
    assert out["uuid"] == "new-uuid"


def test_json_opnsense_model() -> None:
    job = CronJob(description="my job", command="/bin/true")
    out = json.loads(render(job, "json"))
    assert out["description"] == "my job"


# ---------------------------------------------------------------------------
# Plain format
# ---------------------------------------------------------------------------


def test_plain_search_response_yields_uuids() -> None:
    data = _make_search_response()
    out = render(data, "plain")
    assert "abc-1" in out
    assert "abc-2" in out


def test_plain_api_response() -> None:
    data = _make_api_response()
    out = render(data, "plain")
    assert "saved" in out
    assert "new-uuid" in out


def test_plain_opnsense_model() -> None:
    job = CronJob(description="my job")
    out = render(job, "plain")
    assert "description" in out
    assert "my job" in out


# ---------------------------------------------------------------------------
# Table format
# ---------------------------------------------------------------------------


def test_table_search_response_contains_columns() -> None:
    data = _make_search_response()
    out = render(data, "table")
    assert "uuid" in out
    assert "abc-1" in out


def test_table_empty_search_response() -> None:
    data = SearchResponse[CronJob].model_validate(
        {"total": 0, "rowCount": 0, "current": 1, "rows": []}
    )
    out = render(data, "table")
    assert "no results" in out


def test_table_api_response() -> None:
    data = _make_api_response()
    out = render(data, "table")
    assert "saved" in out


def test_table_opnsense_model_field_value_layout() -> None:
    job = CronJob(description="check", command="/bin/check")
    out = render(job, "table")
    assert "description" in out
    assert "check" in out
