from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.syslog import SyslogDestination


@click.group()
def syslog() -> None:
    """Manage remote syslog destinations."""


# ===========================================================================
# Destinations
# ===========================================================================


@syslog.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def dest_list(ctx: click.Context, search: str) -> None:
    """List syslog destinations."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.search_destinations(SearchRequest(searchPhrase=search)), lctx.output_format))


@syslog.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def dest_get(ctx: click.Context, uuid: str) -> None:
    """Get a syslog destination by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.get_destination(uuid), lctx.output_format))


@syslog.command("add")
@click.option("--hostname", default=None, help="Remote syslog server hostname.")
@click.option("--port", default=None)
@click.option("--transport", default=None, help="udp4, tcp4, tls4, etc.")
@click.option("--level", default=None)
@click.option("--facility", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def dest_add(
    ctx: click.Context, hostname: str | None, port: str | None, transport: str | None,
    level: str | None, facility: str | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Add a syslog destination."""
    lctx = get_ctx(ctx)
    obj = build_model(SyslogDestination, from_json, hostname=hostname, port=port,
                      transport=transport, level=level, facility=facility,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.syslog.add_destination(obj), lctx.output_format))


@syslog.command("set")
@click.argument("uuid")
@click.option("--hostname", default=None)
@click.option("--port", default=None)
@click.option("--transport", default=None)
@click.option("--level", default=None)
@click.option("--facility", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def dest_set(
    ctx: click.Context, uuid: str, hostname: str | None, port: str | None, transport: str | None,
    level: str | None, facility: str | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Update a syslog destination."""
    lctx = get_ctx(ctx)
    obj = build_model(SyslogDestination, from_json, hostname=hostname, port=port,
                      transport=transport, level=level, facility=facility,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.syslog.set_destination(uuid, obj), lctx.output_format))


@syslog.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def dest_del(ctx: click.Context, uuid: str) -> None:
    """Delete a syslog destination."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.del_destination(uuid), lctx.output_format))


@syslog.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def dest_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a syslog destination."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.toggle_destination(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@syslog.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show syslog service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.status(), lctx.output_format))


@syslog.command("stats")
@click.pass_context
@handle_api_errors
def stats(ctx: click.Context) -> None:
    """Show syslog statistics."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.stats(), lctx.output_format))


@syslog.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply syslog configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.reconfigure(), lctx.output_format))


@syslog.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the syslog service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.start(), lctx.output_format))


@syslog.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the syslog service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.stop(), lctx.output_format))


@syslog.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the syslog service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.syslog.restart(), lctx.output_format))
