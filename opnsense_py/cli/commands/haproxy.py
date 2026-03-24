from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.models.base import SearchRequest


@click.group()
def haproxy() -> None:
    """Manage HAProxy frontends, backends, servers, and service."""


# ===========================================================================
# Frontends
# ===========================================================================


@haproxy.group("frontend")
def frontend() -> None:
    """Manage HAProxy frontends."""


@frontend.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def frontend_list(ctx: click.Context, search: str) -> None:
    """List frontends."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.search_frontends(SearchRequest(searchPhrase=search)), lctx.output_format))


@frontend.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def frontend_get(ctx: click.Context, uuid: str) -> None:
    """Get a frontend by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.get_frontend(uuid), lctx.output_format))


@frontend.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def frontend_del(ctx: click.Context, uuid: str) -> None:
    """Delete a frontend."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.del_frontend(uuid), lctx.output_format))


@frontend.command("toggle")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def frontend_toggle(ctx: click.Context, uuid: str) -> None:
    """Toggle a frontend on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.toggle_frontend(uuid), lctx.output_format))


# ===========================================================================
# Backends
# ===========================================================================


@haproxy.group("backend")
def backend() -> None:
    """Manage HAProxy backends."""


@backend.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def backend_list(ctx: click.Context, search: str) -> None:
    """List backends."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.search_backends(SearchRequest(searchPhrase=search)), lctx.output_format))


@backend.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def backend_get(ctx: click.Context, uuid: str) -> None:
    """Get a backend by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.get_backend(uuid), lctx.output_format))


@backend.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def backend_del(ctx: click.Context, uuid: str) -> None:
    """Delete a backend."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.del_backend(uuid), lctx.output_format))


@backend.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def backend_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a backend on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.toggle_backend(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Servers
# ===========================================================================


@haproxy.group("server")
def server() -> None:
    """Manage HAProxy servers."""


@server.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def server_list(ctx: click.Context, search: str) -> None:
    """List servers."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.search_servers(SearchRequest(searchPhrase=search)), lctx.output_format))


@server.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def server_get(ctx: click.Context, uuid: str) -> None:
    """Get a server by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.get_server(uuid), lctx.output_format))


@server.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def server_del(ctx: click.Context, uuid: str) -> None:
    """Delete a server."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.del_server(uuid), lctx.output_format))


@server.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def server_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a server on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.toggle_server(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Statistics
# ===========================================================================


@haproxy.command("stats")
@click.pass_context
@handle_api_errors
def stats(ctx: click.Context) -> None:
    """Show HAProxy statistics counters."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.stat_counters(), lctx.output_format))


@haproxy.command("info")
@click.pass_context
@handle_api_errors
def info(ctx: click.Context) -> None:
    """Show HAProxy process info."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.stat_info(), lctx.output_format))


@haproxy.command("configtest")
@click.pass_context
@handle_api_errors
def configtest(ctx: click.Context) -> None:
    """Test HAProxy configuration."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.configtest(), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@haproxy.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show HAProxy service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.status(), lctx.output_format))


@haproxy.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply HAProxy configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.reconfigure(), lctx.output_format))


@haproxy.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the HAProxy service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.start(), lctx.output_format))


@haproxy.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the HAProxy service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.stop(), lctx.output_format))


@haproxy.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the HAProxy service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.haproxy.restart(), lctx.output_format))
