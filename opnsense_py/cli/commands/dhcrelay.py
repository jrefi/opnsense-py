from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.dhcrelay import DHCRelayDestination, DHCRelayRelay


@click.group()
def dhcrelay() -> None:
    """Manage DHCP relay destinations and relays."""


# ===========================================================================
# Destinations
# ===========================================================================


@dhcrelay.group("destination")
def destination() -> None:
    """Manage DHCP relay destination servers."""


@destination.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def destination_list(ctx: click.Context, search: str) -> None:
    """List relay destinations."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dhcrelay.search_destinations(SearchRequest(searchPhrase=search)), lctx.output_format))


@destination.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def destination_get(ctx: click.Context, uuid: str) -> None:
    """Get a relay destination by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dhcrelay.get_destination(uuid), lctx.output_format))


@destination.command("add")
@click.option("--name", default=None)
@click.option("--server", default=None, help="Destination server IP.")
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def destination_add(
    ctx: click.Context, name: str | None, server: str | None, from_json: str | None,
) -> None:
    """Add a relay destination."""
    lctx = get_ctx(ctx)
    obj = build_model(DHCRelayDestination, from_json, name=name, server=server)
    click.echo(render(lctx.client.dhcrelay.add_destination(obj), lctx.output_format))


@destination.command("set")
@click.argument("uuid")
@click.option("--name", default=None)
@click.option("--server", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def destination_set(
    ctx: click.Context, uuid: str, name: str | None, server: str | None, from_json: str | None,
) -> None:
    """Update a relay destination."""
    lctx = get_ctx(ctx)
    obj = build_model(DHCRelayDestination, from_json, name=name, server=server)
    click.echo(render(lctx.client.dhcrelay.set_destination(uuid, obj), lctx.output_format))


@destination.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def destination_del(ctx: click.Context, uuid: str) -> None:
    """Delete a relay destination."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dhcrelay.del_destination(uuid), lctx.output_format))


# ===========================================================================
# Relays
# ===========================================================================


@dhcrelay.group("relay")
def relay() -> None:
    """Manage DHCP relay interface bindings."""


@relay.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def relay_list(ctx: click.Context, search: str) -> None:
    """List relays."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dhcrelay.search_relays(SearchRequest(searchPhrase=search)), lctx.output_format))


@relay.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def relay_get(ctx: click.Context, uuid: str) -> None:
    """Get a relay by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dhcrelay.get_relay(uuid), lctx.output_format))


@relay.command("add")
@click.option("--interface", default=None, help="Listening interface.")
@click.option("--destination", default=None, help="Destination UUID.")
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def relay_add(
    ctx: click.Context, interface: str | None, destination: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Add a relay."""
    lctx = get_ctx(ctx)
    obj = build_model(DHCRelayRelay, from_json, interface=interface,
                      destination=destination, enabled=enabled)
    click.echo(render(lctx.client.dhcrelay.add_relay(obj), lctx.output_format))


@relay.command("set")
@click.argument("uuid")
@click.option("--interface", default=None)
@click.option("--destination", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def relay_set(
    ctx: click.Context, uuid: str, interface: str | None, destination: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Update a relay."""
    lctx = get_ctx(ctx)
    obj = build_model(DHCRelayRelay, from_json, interface=interface,
                      destination=destination, enabled=enabled)
    click.echo(render(lctx.client.dhcrelay.set_relay(uuid, obj), lctx.output_format))


@relay.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def relay_del(ctx: click.Context, uuid: str) -> None:
    """Delete a relay."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dhcrelay.del_relay(uuid), lctx.output_format))


@relay.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def relay_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a relay on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dhcrelay.toggle_relay(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@dhcrelay.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply DHCP relay configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dhcrelay.reconfigure(), lctx.output_format))
