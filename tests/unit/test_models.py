from opnsense_py.models.base import ApiResponse, SearchRequest, SearchResponse


def test_search_request_defaults() -> None:
    req = SearchRequest()
    assert req.current == 1
    assert req.rowCount == 500
    assert req.searchPhrase == ""
    assert req.sort == {}


def test_search_response_parses() -> None:
    raw = {
        "total": 2,
        "rowCount": 2,
        "current": 1,
        "rows": [{"uuid": "a"}, {"uuid": "b"}],
    }
    resp = SearchResponse[dict].model_validate(raw)
    assert resp.total == 2
    assert len(resp.rows) == 2
    assert resp.rows[0]["uuid"] == "a"


def test_api_response_accepts_extra_fields() -> None:
    raw = {"result": "saved", "uuid": "abc", "extra_field": "ignored"}
    resp = ApiResponse.model_validate(raw)
    assert resp.result == "saved"
    assert resp.uuid == "abc"


def test_api_response_no_validations() -> None:
    resp = ApiResponse.model_validate({"result": "ok"})
    assert resp.validations is None
