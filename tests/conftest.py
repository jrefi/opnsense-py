import pytest
import respx

from opnsense_py import OPNsenseClient


@pytest.fixture
def mock_api():
    with respx.mock(base_url="https://opnsense.test:443", assert_all_called=False) as mock:
        yield mock


@pytest.fixture
def client(mock_api: respx.MockRouter) -> OPNsenseClient:
    return OPNsenseClient(
        host="opnsense.test",
        api_key="testkey",
        api_secret="testsecret",
        verify_ssl=False,
    )
