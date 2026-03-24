from pathlib import Path
from unittest.mock import patch

import pytest

from opnsense_py.cli.context import build_client
import click


def test_missing_credentials_raises_usage_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPNSENSE_HOST", raising=False)
    monkeypatch.delenv("OPNSENSE_API_KEY", raising=False)
    monkeypatch.delenv("OPNSENSE_API_SECRET", raising=False)
    with patch("opnsense_py.cli.context._CONFIG_PATH", Path("/nonexistent/path.toml")):
        with pytest.raises(click.UsageError, match="Missing required"):
            build_client(host=None, api_key=None, api_secret=None, verify_ssl=True, https=True, profile="default")


def test_env_vars_override_config_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    config = tmp_path / "config.toml"
    config.write_text('[default]\nhost = "file-host"\napi_key = "file-key"\napi_secret = "file-secret"\n')

    monkeypatch.setenv("OPNSENSE_HOST", "env-host")
    monkeypatch.setenv("OPNSENSE_API_KEY", "env-key")
    monkeypatch.setenv("OPNSENSE_API_SECRET", "env-secret")

    with patch("opnsense_py.cli.context._CONFIG_PATH", config):
        with patch("opnsense_py.cli.context.OPNsenseClient") as mock_client:
            build_client(host=None, api_key=None, api_secret=None, verify_ssl=True, https=True, profile="default")
            mock_client.assert_called_once_with(
                host="env-host",
                api_key="env-key",
                api_secret="env-secret",
                verify_ssl=True,
                https=True,
            )


def test_cli_flags_override_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPNSENSE_HOST", "env-host")
    monkeypatch.setenv("OPNSENSE_API_KEY", "env-key")
    monkeypatch.setenv("OPNSENSE_API_SECRET", "env-secret")

    with patch("opnsense_py.cli.context._CONFIG_PATH", Path("/nonexistent/path.toml")):
        with patch("opnsense_py.cli.context.OPNsenseClient") as mock_client:
            build_client(
                host="flag-host",
                api_key="flag-key",
                api_secret="flag-secret",
                verify_ssl=False,
                https=True,
                profile="default",
            )
            mock_client.assert_called_once_with(
                host="flag-host",
                api_key="flag-key",
                api_secret="flag-secret",
                verify_ssl=False,
                https=True,
            )


def test_config_file_profile_loaded(tmp_path: Path) -> None:
    config = tmp_path / "config.toml"
    config.write_text(
        '[prod]\nhost = "prod-host"\napi_key = "prod-key"\napi_secret = "prod-secret"\n'
    )
    with patch("opnsense_py.cli.context._CONFIG_PATH", config):
        with patch("opnsense_py.cli.context.OPNsenseClient") as mock_client:
            build_client(host=None, api_key=None, api_secret=None, verify_ssl=True, https=True, profile="prod")
            mock_client.assert_called_once_with(
                host="prod-host",
                api_key="prod-key",
                api_secret="prod-secret",
                verify_ssl=True,
                https=True,
            )


def test_verify_ssl_disabled_via_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPNSENSE_VERIFY_SSL", "false")
    with patch("opnsense_py.cli.context._CONFIG_PATH", Path("/nonexistent/path.toml")):
        with patch("opnsense_py.cli.context.OPNsenseClient") as mock_client:
            build_client(
                host="h", api_key="k", api_secret="s", verify_ssl=True, https=True, profile="default"
            )
            _, kwargs = mock_client.call_args
            assert kwargs["verify_ssl"] is False


def test_no_tls_via_flag(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPNSENSE_HTTPS", raising=False)
    with patch("opnsense_py.cli.context._CONFIG_PATH", Path("/nonexistent/path.toml")):
        with patch("opnsense_py.cli.context.OPNsenseClient") as mock_client:
            build_client(
                host="h", api_key="k", api_secret="s", verify_ssl=True, https=False, profile="default"
            )
            _, kwargs = mock_client.call_args
            assert kwargs["https"] is False
