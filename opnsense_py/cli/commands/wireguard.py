from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.wireguard import WireguardPeer, WireguardServer


@click.group()
def wireguard() -> None:
    """Manage WireGuard VPN servers and peers."""


# ===========================================================================
# Servers
# ===========================================================================


@wireguard.group("server")
def server() -> None:
    """Manage WireGuard server instances."""


@server.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def server_list(ctx: click.Context, search: str) -> None:
    """List WireGuard servers."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.search_servers(SearchRequest(searchPhrase=search)), lctx.output_format))


@server.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def server_get(ctx: click.Context, uuid: str) -> None:
    """Get a WireGuard server by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.get_server(uuid), lctx.output_format))


@server.command("add")
@click.option("--name", default=None)
@click.option("--port", default=None)
@click.option("--tunneladdress", default=None, help="Tunnel IP address(es), e.g. 10.0.0.1/24.")
@click.option("--dns", default=None)
@click.option("--mtu", default=None, type=int)
@click.option("--enabled", default=None)
@click.option("--peers", default=None, help="Comma-separated peer UUIDs.")
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def server_add(
    ctx: click.Context, name: str | None, port: str | None, tunneladdress: str | None,
    dns: str | None, mtu: int | None, enabled: str | None, peers: str | None,
    from_json: str | None,
) -> None:
    """Add a WireGuard server."""
    lctx = get_ctx(ctx)
    obj = build_model(WireguardServer, from_json, name=name, port=port,
                      tunneladdress=tunneladdress, dns=dns, mtu=mtu,
                      enabled=enabled, peers=peers)
    click.echo(render(lctx.client.wireguard.add_server(obj), lctx.output_format))


@server.command("set")
@click.argument("uuid")
@click.option("--name", default=None)
@click.option("--port", default=None)
@click.option("--tunneladdress", default=None)
@click.option("--dns", default=None)
@click.option("--mtu", default=None, type=int)
@click.option("--enabled", default=None)
@click.option("--peers", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def server_set(
    ctx: click.Context, uuid: str, name: str | None, port: str | None,
    tunneladdress: str | None, dns: str | None, mtu: int | None,
    enabled: str | None, peers: str | None, from_json: str | None,
) -> None:
    """Update a WireGuard server."""
    lctx = get_ctx(ctx)
    obj = build_model(WireguardServer, from_json, name=name, port=port,
                      tunneladdress=tunneladdress, dns=dns, mtu=mtu,
                      enabled=enabled, peers=peers)
    click.echo(render(lctx.client.wireguard.set_server(uuid, obj), lctx.output_format))


@server.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def server_del(ctx: click.Context, uuid: str) -> None:
    """Delete a WireGuard server."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.del_server(uuid), lctx.output_format))


@server.command("toggle")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def server_toggle(ctx: click.Context, uuid: str) -> None:
    """Toggle a WireGuard server on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.toggle_server(uuid), lctx.output_format))


@server.command("keygen")
@click.pass_context
@handle_api_errors
def server_keygen(ctx: click.Context) -> None:
    """Generate a new WireGuard public/private key pair."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.key_pair(), lctx.output_format))


# ===========================================================================
# Peers
# ===========================================================================


@wireguard.group("peer")
def peer() -> None:
    """Manage WireGuard peers (clients)."""


@peer.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def peer_list(ctx: click.Context, search: str) -> None:
    """List WireGuard peers."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.search_clients(SearchRequest(searchPhrase=search)), lctx.output_format))


@peer.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def peer_get(ctx: click.Context, uuid: str) -> None:
    """Get a WireGuard peer by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.get_client(uuid), lctx.output_format))


@peer.command("add")
@click.option("--name", default=None)
@click.option("--pubkey", default=None, help="Peer public key.")
@click.option("--tunneladdress", default=None, help="Allowed IPs / tunnel address.")
@click.option("--serveraddress", default=None)
@click.option("--serverport", default=None)
@click.option("--keepalive", default=None, type=int)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def peer_add(
    ctx: click.Context, name: str | None, pubkey: str | None, tunneladdress: str | None,
    serveraddress: str | None, serverport: str | None, keepalive: int | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Add a WireGuard peer."""
    lctx = get_ctx(ctx)
    obj = build_model(WireguardPeer, from_json, name=name, pubkey=pubkey,
                      tunneladdress=tunneladdress, serveraddress=serveraddress,
                      serverport=serverport, keepalive=keepalive, enabled=enabled)
    click.echo(render(lctx.client.wireguard.add_client_builder(obj), lctx.output_format))


@peer.command("set")
@click.argument("uuid")
@click.option("--name", default=None)
@click.option("--pubkey", default=None)
@click.option("--tunneladdress", default=None)
@click.option("--serveraddress", default=None)
@click.option("--serverport", default=None)
@click.option("--keepalive", default=None, type=int)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def peer_set(
    ctx: click.Context, uuid: str, name: str | None, pubkey: str | None,
    tunneladdress: str | None, serveraddress: str | None, serverport: str | None,
    keepalive: int | None, enabled: str | None, from_json: str | None,
) -> None:
    """Update a WireGuard peer."""
    lctx = get_ctx(ctx)
    obj = build_model(WireguardPeer, from_json, name=name, pubkey=pubkey,
                      tunneladdress=tunneladdress, serveraddress=serveraddress,
                      serverport=serverport, keepalive=keepalive, enabled=enabled)
    click.echo(render(lctx.client.wireguard.set_client(uuid, obj), lctx.output_format))


@peer.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def peer_del(ctx: click.Context, uuid: str) -> None:
    """Delete a WireGuard peer."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.del_client(uuid), lctx.output_format))


@peer.command("toggle")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def peer_toggle(ctx: click.Context, uuid: str) -> None:
    """Toggle a WireGuard peer on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.toggle_client(uuid), lctx.output_format))


@peer.command("psk")
@click.pass_context
@handle_api_errors
def peer_psk(ctx: click.Context) -> None:
    """Generate a new pre-shared key."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.psk(), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@wireguard.command("show")
@click.pass_context
@handle_api_errors
def show(ctx: click.Context) -> None:
    """Show live WireGuard interface status (wg show)."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.show(), lctx.output_format))


@wireguard.command("status")
@click.pass_context
@handle_api_errors
def wg_status(ctx: click.Context) -> None:
    """Show WireGuard service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.status(), lctx.output_format))


@wireguard.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply WireGuard configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.reconfigure(), lctx.output_format))


@wireguard.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the WireGuard service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.start(), lctx.output_format))


@wireguard.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the WireGuard service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.stop(), lctx.output_format))


@wireguard.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the WireGuard service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.wireguard.restart(), lctx.output_format))
