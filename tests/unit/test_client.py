import httpx
import pytest
import respx

from opnsense_py import (
    OPNsenseAuthError,
    OPNsenseClient,
    OPNsenseError,
    OPNsenseHTTPError,
    OPNsenseNotFoundError,
    OPNsenseValidationError,
)


def test_client_context_manager(mock_api: respx.MockRouter) -> None:
    with OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    ) as c:
        assert c._http is not None
    # After exit, the underlying httpx client should be closed
    assert c._http.is_closed


def test_raises_auth_error_on_401(mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/core/system/status").mock(
        return_value=httpx.Response(401, text="Unauthorized")
    )
    client = OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    )
    with pytest.raises(OPNsenseAuthError) as exc_info:
        client._get("core/system/status")
    assert exc_info.value.status_code == 401


def test_raises_auth_error_on_403(mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/core/system/status").mock(
        return_value=httpx.Response(403, text="Forbidden")
    )
    client = OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    )
    with pytest.raises(OPNsenseAuthError) as exc_info:
        client._get("core/system/status")
    assert exc_info.value.status_code == 403


def test_raises_not_found_on_404(mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/firewall/alias/get_item/no-uuid").mock(
        return_value=httpx.Response(404, text="Not Found")
    )
    client = OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    )
    with pytest.raises(OPNsenseNotFoundError) as exc_info:
        client._get("firewall/alias/get_item/no-uuid")
    assert exc_info.value.status_code == 404


def test_raises_http_error_on_500(mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/core/system/status").mock(
        return_value=httpx.Response(500, text="Internal Server Error")
    )
    client = OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    )
    with pytest.raises(OPNsenseHTTPError) as exc_info:
        client._get("core/system/status")
    assert exc_info.value.status_code == 500


def test_raises_validation_error_on_non_empty_validations(
    mock_api: respx.MockRouter,
) -> None:
    mock_api.post("/api/cron/settings/add_job").mock(
        return_value=httpx.Response(
            200,
            json={
                "result": "failed",
                "validations": {"job.description": "This field is required."},
            },
        )
    )
    client = OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    )
    with pytest.raises(OPNsenseValidationError) as exc_info:
        client._post("cron/settings/add_job", json={})
    assert "job.description" in exc_info.value.validations


def test_does_not_raise_on_empty_validations(mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/cron/settings/add_job").mock(
        return_value=httpx.Response(
            200,
            json={"result": "saved", "uuid": "abc-123", "validations": {}},
        )
    )
    client = OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    )
    result = client._post("cron/settings/add_job", json={})
    assert result["result"] == "saved"


def test_does_not_raise_on_result_failed_without_validations(
    mock_api: respx.MockRouter,
) -> None:
    mock_api.post("/api/cron/settings/reconfigure").mock(
        return_value=httpx.Response(200, json={"result": "failed"})
    )
    client = OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    )
    result = client._post("cron/settings/reconfigure")
    assert result["result"] == "failed"


def test_raises_error_on_non_json_response(mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/core/system/status").mock(
        return_value=httpx.Response(200, text="not json")
    )
    client = OPNsenseClient(
        host="opnsense.test", api_key="k", api_secret="s", verify_ssl=False
    )
    with pytest.raises(OPNsenseError, match="Non-JSON"):
        client._get("core/system/status")
