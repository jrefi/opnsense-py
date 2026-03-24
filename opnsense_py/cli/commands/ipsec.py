from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.ipsec import IPsecChild, IPsecConnection


@click.group()
def ipsec() -> None:
    """Manage IPsec VPN connections."""


# ===========================================================================
# Connections
# ===========================================================================


@ipsec.group("connection")
def connection() -> None:
    """Manage IPsec IKE connections."""


@connection.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def connection_list(ctx: click.Context, search: str) -> None:
    """List IPsec connections."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.search_connections(SearchRequest(searchPhrase=search)), lctx.output_format))


@connection.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def connection_get(ctx: click.Context, uuid: str) -> None:
    """Get an IPsec connection by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.get_connection(uuid), lctx.output_format))


@connection.command("add")
@click.option("--local-addrs", "local_addrs", default=None)
@click.option("--remote-addrs", "remote_addrs", default=None)
@click.option("--version", default=None, help="IKE version: 1 or 2")
@click.option("--proposals", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def connection_add(
    ctx: click.Context, local_addrs: str | None, remote_addrs: str | None,
    version: str | None, proposals: str | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Add an IPsec connection."""
    lctx = get_ctx(ctx)
    obj = build_model(IPsecConnection, from_json, local_addrs=local_addrs,
                      remote_addrs=remote_addrs, version=version, proposals=proposals,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.ipsec.add_connection(obj), lctx.output_format))


@connection.command("set")
@click.argument("uuid")
@click.option("--local-addrs", "local_addrs", default=None)
@click.option("--remote-addrs", "remote_addrs", default=None)
@click.option("--version", default=None)
@click.option("--proposals", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def connection_set(
    ctx: click.Context, uuid: str, local_addrs: str | None, remote_addrs: str | None,
    version: str | None, proposals: str | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Update an IPsec connection."""
    lctx = get_ctx(ctx)
    obj = build_model(IPsecConnection, from_json, local_addrs=local_addrs,
                      remote_addrs=remote_addrs, version=version, proposals=proposals,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.ipsec.set_connection(uuid, obj), lctx.output_format))


@connection.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def connection_del(ctx: click.Context, uuid: str) -> None:
    """Delete an IPsec connection."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.del_connection(uuid), lctx.output_format))


@connection.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def connection_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle an IPsec connection."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.toggle_connection(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Child SAs
# ===========================================================================


@ipsec.group("child")
def child() -> None:
    """Manage IPsec child SAs (tunnels)."""


@child.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def child_list(ctx: click.Context, search: str) -> None:
    """List IPsec child SAs."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.search_children(SearchRequest(searchPhrase=search)), lctx.output_format))


@child.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def child_get(ctx: click.Context, uuid: str) -> None:
    """Get an IPsec child SA by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.get_child(uuid), lctx.output_format))


@child.command("add")
@click.option("--connection", default=None, help="Parent connection UUID.")
@click.option("--local-ts", "local_ts", default=None, help="Local traffic selectors.")
@click.option("--remote-ts", "remote_ts", default=None, help="Remote traffic selectors.")
@click.option("--mode", default=None, help="tunnel or transport")
@click.option("--esp-proposals", "esp_proposals", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def child_add(
    ctx: click.Context, connection: str | None, local_ts: str | None, remote_ts: str | None,
    mode: str | None, esp_proposals: str | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Add an IPsec child SA."""
    lctx = get_ctx(ctx)
    obj = build_model(IPsecChild, from_json, connection=connection, local_ts=local_ts,
                      remote_ts=remote_ts, mode=mode, esp_proposals=esp_proposals,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.ipsec.add_child(obj), lctx.output_format))


@child.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def child_del(ctx: click.Context, uuid: str) -> None:
    """Delete an IPsec child SA."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.del_child(uuid), lctx.output_format))


@child.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def child_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle an IPsec child SA."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.toggle_child(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Sessions
# ===========================================================================


@ipsec.command("sessions")
@click.pass_context
@handle_api_errors
def sessions(ctx: click.Context) -> None:
    """Show active IPsec IKE sessions."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.search_sessions_phase1(), lctx.output_format))


@ipsec.command("leases")
@click.pass_context
@handle_api_errors
def leases(ctx: click.Context) -> None:
    """Show IPsec address pool leases."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.search_leases(), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@ipsec.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show IPsec service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.status(), lctx.output_format))


@ipsec.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply IPsec configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.reconfigure(), lctx.output_format))


@ipsec.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the IPsec service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.start(), lctx.output_format))


@ipsec.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the IPsec service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.stop(), lctx.output_format))


@ipsec.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the IPsec service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ipsec.restart(), lctx.output_format))
