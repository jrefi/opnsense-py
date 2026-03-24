from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render


@click.group()
def ntpd() -> None:
    """Show NTP daemon status and peer information."""


@ntpd.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show NTP service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ntpd.status(), lctx.output_format))


@ntpd.command("peers")
@click.pass_context
@handle_api_errors
def peers(ctx: click.Context) -> None:
    """Show NTP peer metadata."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ntpd.meta(), lctx.output_format))


@ntpd.command("gps")
@click.pass_context
@handle_api_errors
def gps(ctx: click.Context) -> None:
    """Show GPS source status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ntpd.gps(), lctx.output_format))
