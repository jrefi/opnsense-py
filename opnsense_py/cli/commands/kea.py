from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.kea import KeaHaPeer, KeaReservation4, KeaSubnet4


@click.group()
def kea() -> None:
    """Manage Kea DHCP subnets, reservations, and service."""


# ===========================================================================
# DHCPv4 Subnets
# ===========================================================================


@kea.group("subnet4")
def subnet4() -> None:
    """Manage Kea DHCPv4 subnets."""


@subnet4.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def subnet4_list(ctx: click.Context, search: str) -> None:
    """List DHCPv4 subnets."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.search_v4_subnets(SearchRequest(searchPhrase=search)), lctx.output_format))


@subnet4.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def subnet4_get(ctx: click.Context, uuid: str) -> None:
    """Get a DHCPv4 subnet by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.get_v4_subnet(uuid), lctx.output_format))


@subnet4.command("add")
@click.option("--subnet", default=None, help="Subnet CIDR, e.g. 192.168.1.0/24.")
@click.option("--pools", default=None, help="Address pool ranges.")
@click.option("--next-server", "next_server", default=None)
@click.option("--description", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def subnet4_add(
    ctx: click.Context, subnet: str | None, pools: str | None,
    next_server: str | None, description: str | None, from_json: str | None,
) -> None:
    """Add a DHCPv4 subnet."""
    lctx = get_ctx(ctx)
    obj = build_model(KeaSubnet4, from_json, subnet=subnet, pools=pools,
                      next_server=next_server, description=description)
    click.echo(render(lctx.client.kea.add_v4_subnet(obj), lctx.output_format))


@subnet4.command("set")
@click.argument("uuid")
@click.option("--subnet", default=None)
@click.option("--pools", default=None)
@click.option("--next-server", "next_server", default=None)
@click.option("--description", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def subnet4_set(
    ctx: click.Context, uuid: str, subnet: str | None, pools: str | None,
    next_server: str | None, description: str | None, from_json: str | None,
) -> None:
    """Update a DHCPv4 subnet."""
    lctx = get_ctx(ctx)
    obj = build_model(KeaSubnet4, from_json, subnet=subnet, pools=pools,
                      next_server=next_server, description=description)
    click.echo(render(lctx.client.kea.set_v4_subnet(uuid, obj), lctx.output_format))


@subnet4.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def subnet4_del(ctx: click.Context, uuid: str) -> None:
    """Delete a DHCPv4 subnet."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.del_v4_subnet(uuid), lctx.output_format))


# ===========================================================================
# DHCPv4 Reservations
# ===========================================================================


@kea.group("reservation4")
def reservation4() -> None:
    """Manage Kea DHCPv4 host reservations."""


@reservation4.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def reservation4_list(ctx: click.Context, search: str) -> None:
    """List DHCPv4 reservations."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.search_v4_reservations(SearchRequest(searchPhrase=search)), lctx.output_format))


@reservation4.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def reservation4_get(ctx: click.Context, uuid: str) -> None:
    """Get a DHCPv4 reservation by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.get_v4_reservation(uuid), lctx.output_format))


@reservation4.command("add")
@click.option("--subnet", default=None, help="Parent subnet UUID.")
@click.option("--ip-address", "ip_address", default=None)
@click.option("--hw-address", "hw_address", default=None, help="MAC address.")
@click.option("--hostname", default=None)
@click.option("--description", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def reservation4_add(
    ctx: click.Context, subnet: str | None, ip_address: str | None,
    hw_address: str | None, hostname: str | None, description: str | None,
    from_json: str | None,
) -> None:
    """Add a DHCPv4 reservation."""
    lctx = get_ctx(ctx)
    obj = build_model(KeaReservation4, from_json, subnet=subnet, ip_address=ip_address,
                      hw_address=hw_address, hostname=hostname, description=description)
    click.echo(render(lctx.client.kea.add_v4_reservation(obj), lctx.output_format))


@reservation4.command("set")
@click.argument("uuid")
@click.option("--subnet", default=None)
@click.option("--ip-address", "ip_address", default=None)
@click.option("--hw-address", "hw_address", default=None)
@click.option("--hostname", default=None)
@click.option("--description", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def reservation4_set(
    ctx: click.Context, uuid: str, subnet: str | None, ip_address: str | None,
    hw_address: str | None, hostname: str | None, description: str | None,
    from_json: str | None,
) -> None:
    """Update a DHCPv4 reservation."""
    lctx = get_ctx(ctx)
    obj = build_model(KeaReservation4, from_json, subnet=subnet, ip_address=ip_address,
                      hw_address=hw_address, hostname=hostname, description=description)
    click.echo(render(lctx.client.kea.set_v4_reservation(uuid, obj), lctx.output_format))


@reservation4.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def reservation4_del(ctx: click.Context, uuid: str) -> None:
    """Delete a DHCPv4 reservation."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.del_v4_reservation(uuid), lctx.output_format))


# ===========================================================================
# DHCPv4 HA Peers
# ===========================================================================


@kea.group("peer4")
def peer4() -> None:
    """Manage Kea DHCPv4 high-availability peers."""


@peer4.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def peer4_list(ctx: click.Context, search: str) -> None:
    """List DHCPv4 HA peers."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.search_v4_peers(SearchRequest(searchPhrase=search)), lctx.output_format))


@peer4.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def peer4_get(ctx: click.Context, uuid: str) -> None:
    """Get a DHCPv4 HA peer by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.get_v4_peer(uuid), lctx.output_format))


@peer4.command("add")
@click.option("--name", default=None)
@click.option("--role", default=None, help="primary, secondary, or standby")
@click.option("--url", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def peer4_add(
    ctx: click.Context, name: str | None, role: str | None,
    url: str | None, from_json: str | None,
) -> None:
    """Add a DHCPv4 HA peer."""
    lctx = get_ctx(ctx)
    obj = build_model(KeaHaPeer, from_json, name=name, role=role, url=url)
    click.echo(render(lctx.client.kea.add_v4_peer(obj), lctx.output_format))


@peer4.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def peer4_del(ctx: click.Context, uuid: str) -> None:
    """Delete a DHCPv4 HA peer."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.del_v4_peer(uuid), lctx.output_format))


# ===========================================================================
# Leases
# ===========================================================================


@kea.command("leases")
@click.pass_context
@handle_api_errors
def leases(ctx: click.Context) -> None:
    """Show active DHCP leases."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.search_leases(), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@kea.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show Kea service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.status(), lctx.output_format))


@kea.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply Kea configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.reconfigure(), lctx.output_format))


@kea.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the Kea service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.start(), lctx.output_format))


@kea.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the Kea service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.stop(), lctx.output_format))


@kea.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the Kea service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.kea.restart(), lctx.output_format))
