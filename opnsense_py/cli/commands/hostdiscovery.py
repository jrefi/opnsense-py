from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render


@click.group()
def hostdiscovery() -> None:
    """Discover hosts on the network via ARP/NDP scanning."""


@hostdiscovery.command("scan")
@click.pass_context
@handle_api_errors
def scan(ctx: click.Context) -> None:
    """Show discovered hosts."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.hostdiscovery.search(), lctx.output_format))


@hostdiscovery.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show host discovery service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.hostdiscovery.status(), lctx.output_format))


@hostdiscovery.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply host discovery configuration."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.hostdiscovery.reconfigure(), lctx.output_format))


@hostdiscovery.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the host discovery service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.hostdiscovery.start(), lctx.output_format))


@hostdiscovery.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the host discovery service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.hostdiscovery.stop(), lctx.output_format))


@hostdiscovery.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the host discovery service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.hostdiscovery.restart(), lctx.output_format))
