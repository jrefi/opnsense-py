from __future__ import annotations

import sys
from functools import wraps
from typing import Any, Callable, TypeVar

import click

from opnsense_py.cli.context import build_client
from opnsense_py.exceptions import (
    OPNsenseAuthError,
    OPNsenseError,
    OPNsenseHTTPError,
    OPNsenseNotFoundError,
    OPNsenseValidationError,
)

F = TypeVar("F", bound=Callable[..., Any])

_OUTPUT_CHOICES = click.Choice(["table", "json", "plain"], case_sensitive=False)


# ---------------------------------------------------------------------------
# Error handler decorator
# ---------------------------------------------------------------------------


def handle_api_errors(f: F) -> F:
    """Decorator that catches OPNsense exceptions and exits with a clean message."""

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return f(*args, **kwargs)
        except OPNsenseValidationError as exc:
            click.echo("Validation errors:", err=True)
            for field, msg in exc.validations.items():
                click.echo(f"  {field}: {msg}", err=True)
            sys.exit(4)
        except OPNsenseAuthError:
            click.echo("Authentication failed. Check your API key and secret.", err=True)
            sys.exit(2)
        except OPNsenseNotFoundError as exc:
            click.echo(f"Not found: {exc}", err=True)
            sys.exit(3)
        except OPNsenseHTTPError as exc:
            click.echo(f"HTTP error: {exc}", err=True)
            sys.exit(1)
        except OPNsenseError as exc:
            click.echo(f"API error: {exc}", err=True)
            sys.exit(1)

    return wrapper  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Root group
# ---------------------------------------------------------------------------


@click.group()
@click.option("--host", envvar="OPNSENSE_HOST", default=None, help="OPNsense hostname or IP.")
@click.option("--api-key", envvar="OPNSENSE_API_KEY", default=None, help="API key.")
@click.option("--api-secret", envvar="OPNSENSE_API_SECRET", default=None, help="API secret.")
@click.option(
    "--no-verify-ssl",
    is_flag=True,
    default=False,
    help="Disable TLS certificate verification.",
)
@click.option(
    "--no-tls",
    is_flag=True,
    default=False,
    envvar="OPNSENSE_NO_TLS",
    help="Use plain HTTP instead of HTTPS (sets default port to 80).",
)
@click.option(
    "--profile",
    envvar="OPNSENSE_PROFILE",
    default="default",
    show_default=True,
    help="Config file profile to use.",
)
@click.option(
    "--output",
    "-o",
    type=_OUTPUT_CHOICES,
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def cli(
    ctx: click.Context,
    host: str | None,
    api_key: str | None,
    api_secret: str | None,
    no_verify_ssl: bool,
    no_tls: bool,
    profile: str,
    output: str,
) -> None:
    """opn — OPNsense command-line interface."""
    # Allow tests to inject a pre-built _LazyContext via obj=
    if isinstance(ctx.obj, _LazyContext):
        return
    ctx.obj = _LazyContext(
        host=host,
        api_key=api_key,
        api_secret=api_secret,
        verify_ssl=not no_verify_ssl,
        https=not no_tls,
        profile=profile,
        output_format=output,
    )
    ctx.call_on_close(_close_client(ctx))


def _close_client(ctx: click.Context) -> Callable[[], None]:
    def _close() -> None:
        lazy = ctx.obj
        if isinstance(lazy, _LazyContext) and lazy._client is not None:
            lazy._client.close()

    return _close


class _LazyContext:
    """Defers client construction until the first command actually needs it."""

    def __init__(
        self,
        host: str | None,
        api_key: str | None,
        api_secret: str | None,
        verify_ssl: bool,
        https: bool,
        profile: str,
        output_format: str,
    ) -> None:
        self._host = host
        self._api_key = api_key
        self._api_secret = api_secret
        self._verify_ssl = verify_ssl
        self._https = https
        self._profile = profile
        self.output_format = output_format
        self._client = None

    @property
    def client(self):  # type: ignore[no-untyped-def]
        if self._client is None:
            self._client = build_client(
                host=self._host,
                api_key=self._api_key,
                api_secret=self._api_secret,
                verify_ssl=self._verify_ssl,
                https=self._https,
                profile=self._profile,
            )
        return self._client


def get_ctx(ctx: click.Context) -> _LazyContext:
    """Retrieve the _LazyContext from the Click context object."""
    return ctx.obj  # type: ignore[no-any-return]


# ---------------------------------------------------------------------------
# Subgroup registration
# ---------------------------------------------------------------------------

from opnsense_py.cli.commands.auth import auth  # noqa: E402
from opnsense_py.cli.commands.captiveportal import captiveportal  # noqa: E402
from opnsense_py.cli.commands.cron import cron  # noqa: E402
from opnsense_py.cli.commands.dhcrelay import dhcrelay  # noqa: E402
from opnsense_py.cli.commands.diagnostics import diagnostics  # noqa: E402
from opnsense_py.cli.commands.dnsmasq import dnsmasq  # noqa: E402
from opnsense_py.cli.commands.firewall import firewall  # noqa: E402
from opnsense_py.cli.commands.firmware import firmware  # noqa: E402
from opnsense_py.cli.commands.haproxy import haproxy  # noqa: E402
from opnsense_py.cli.commands.hostdiscovery import hostdiscovery  # noqa: E402
from opnsense_py.cli.commands.ids import ids  # noqa: E402
from opnsense_py.cli.commands.ipsec import ipsec  # noqa: E402
from opnsense_py.cli.commands.kea import kea  # noqa: E402
from opnsense_py.cli.commands.monit import monit  # noqa: E402
from opnsense_py.cli.commands.ntpd import ntpd  # noqa: E402
from opnsense_py.cli.commands.openvpn import openvpn  # noqa: E402
from opnsense_py.cli.commands.radvd import radvd  # noqa: E402
from opnsense_py.cli.commands.routes import routes  # noqa: E402
from opnsense_py.cli.commands.routing import routing  # noqa: E402
from opnsense_py.cli.commands.syslog import syslog  # noqa: E402
from opnsense_py.cli.commands.system import system  # noqa: E402
from opnsense_py.cli.commands.trafficshaper import trafficshaper  # noqa: E402
from opnsense_py.cli.commands.trust import trust  # noqa: E402
from opnsense_py.cli.commands.unbound import unbound  # noqa: E402
from opnsense_py.cli.commands.wireguard import wireguard  # noqa: E402

cli.add_command(auth)
cli.add_command(captiveportal)
cli.add_command(cron)
cli.add_command(dhcrelay)
cli.add_command(diagnostics)
cli.add_command(dnsmasq)
cli.add_command(firewall)
cli.add_command(firmware)
cli.add_command(haproxy)
cli.add_command(hostdiscovery)
cli.add_command(ids)
cli.add_command(ipsec)
cli.add_command(kea)
cli.add_command(monit)
cli.add_command(ntpd)
cli.add_command(openvpn)
cli.add_command(radvd)
cli.add_command(routes)
cli.add_command(routing)
cli.add_command(syslog)
cli.add_command(system)
cli.add_command(trafficshaper)
cli.add_command(trust)
cli.add_command(unbound)
cli.add_command(wireguard)
