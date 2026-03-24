from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.models.base import SearchRequest


@click.group()
def radvd() -> None:
    """Manage Router Advertisement daemon (radvd) entries."""


# ===========================================================================
# Entries
# ===========================================================================


@radvd.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def entry_list(ctx: click.Context, search: str) -> None:
    """List radvd entries."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.search_entries(SearchRequest(searchPhrase=search)), lctx.output_format))


@radvd.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def entry_get(ctx: click.Context, uuid: str) -> None:
    """Get an radvd entry by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.get_entry(uuid), lctx.output_format))


@radvd.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def entry_del(ctx: click.Context, uuid: str) -> None:
    """Delete an radvd entry."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.del_entry(uuid), lctx.output_format))


@radvd.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def entry_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle an radvd entry on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.toggle_entry(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@radvd.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show radvd service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.status(), lctx.output_format))


@radvd.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply radvd configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.reconfigure(), lctx.output_format))


@radvd.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the radvd service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.start(), lctx.output_format))


@radvd.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the radvd service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.stop(), lctx.output_format))


@radvd.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the radvd service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.radvd.restart(), lctx.output_format))
