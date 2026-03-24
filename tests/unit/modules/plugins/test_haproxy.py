import httpx
import respx

from opnsense_py import OPNsenseClient


def test_search_frontends(client: OPNsenseClient, mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/haproxy/settings/search_frontends").mock(
        return_value=httpx.Response(
            200,
            json={
                "total": 1,
                "rowCount": 1,
                "current": 1,
                "rows": [{"uuid": "fe-uuid", "name": "my-frontend"}],
            },
        )
    )
    result = client.haproxy.search_frontends()
    assert result.rows[0]["name"] == "my-frontend"


def test_add_backend(client: OPNsenseClient, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/haproxy/settings/add_backend").mock(
        return_value=httpx.Response(200, json={"result": "saved", "uuid": "be-uuid"})
    )
    result = client.haproxy.add_backend({"backend": {"name": "my-backend"}})
    assert route.called
    assert result.uuid == "be-uuid"


def test_configtest_uses_get(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    route = mock_api.get("/api/haproxy/service/configtest").mock(
        return_value=httpx.Response(200, json={"result": "OK"})
    )
    client.haproxy.configtest()
    assert route.called


def test_search_mailers_non_standard_name(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    mock_api.post("/api/haproxy/settings/searchmailers").mock(
        return_value=httpx.Response(
            200,
            json={"total": 0, "rowCount": 0, "current": 1, "rows": []},
        )
    )
    result = client.haproxy.search_mailers()
    assert result.total == 0


def test_add_mailer_non_standard_name(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    route = mock_api.post("/api/haproxy/settings/addmailer").mock(
        return_value=httpx.Response(200, json={"result": "saved", "uuid": "m-uuid"})
    )
    result = client.haproxy.add_mailer({"mailer": {"name": "smtp"}})
    assert route.called
    assert result.uuid == "m-uuid"


def test_reconfigure(client: OPNsenseClient, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/haproxy/service/reconfigure").mock(
        return_value=httpx.Response(200, json={"result": "ok"})
    )
    client.haproxy.reconfigure()
    assert route.called
