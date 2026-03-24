import httpx
import respx

from opnsense_py import OPNsenseClient
from opnsense_py.models.unbound import HostOverride


def test_search_host_overrides(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    mock_api.post("/api/unbound/settings/search_host_override").mock(
        return_value=httpx.Response(
            200,
            json={
                "total": 1,
                "rowCount": 1,
                "current": 1,
                "rows": [{"uuid": "h1", "hostname": "myhost"}],
            },
        )
    )
    result = client.unbound.search_host_overrides()
    assert result.rows[0].hostname == "myhost"


def test_search_all_host_overrides_paginates(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    mock_api.post("/api/unbound/settings/search_host_override").mock(
        side_effect=[
            httpx.Response(
                200,
                json={
                    "total": 3,
                    "rowCount": 2,
                    "current": 1,
                    "rows": [{"uuid": "h1"}, {"uuid": "h2"}],
                },
            ),
            httpx.Response(
                200,
                json={
                    "total": 3,
                    "rowCount": 1,
                    "current": 2,
                    "rows": [{"uuid": "h3"}],
                },
            ),
        ]
    )
    rows = client.unbound._search_all("unbound", "settings", "search_host_override")
    assert len(rows) == 3
    assert rows[2]["uuid"] == "h3"


def test_add_host_override(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    route = mock_api.post("/api/unbound/settings/add_host_override").mock(
        return_value=httpx.Response(200, json={"result": "saved", "uuid": "new-h"})
    )
    result = client.unbound.add_host_override(
        HostOverride(hostname="newhost", domain="example.com", rr="A", server="1.2.3.4")
    )
    assert route.called
    assert result.uuid == "new-h"


def test_reconfigure_general_uses_get(
    client: OPNsenseClient, mock_api: respx.MockRouter
) -> None:
    route = mock_api.get("/api/unbound/service/reconfigure_general").mock(
        return_value=httpx.Response(200, json={"status": "ok"})
    )
    client.unbound.reconfigure_general()
    assert route.called
