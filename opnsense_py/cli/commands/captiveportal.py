from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.models.base import SearchRequest


@click.group()
def captiveportal() -> None:
    """Manage captive portal zones, sessions, and vouchers."""


# ===========================================================================
# Zones
# ===========================================================================


@captiveportal.group("zone")
def zone() -> None:
    """Manage captive portal zones."""


@zone.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def zone_list(ctx: click.Context, search: str) -> None:
    """List captive portal zones."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.search_zones(SearchRequest(searchPhrase=search)), lctx.output_format))


@zone.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def zone_get(ctx: click.Context, uuid: str) -> None:
    """Get a zone by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.get_zone(uuid), lctx.output_format))


@zone.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def zone_del(ctx: click.Context, uuid: str) -> None:
    """Delete a zone."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.del_zone(uuid), lctx.output_format))


@zone.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def zone_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a zone on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.toggle_zone(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Sessions
# ===========================================================================


@captiveportal.command("sessions")
@click.pass_context
@handle_api_errors
def sessions(ctx: click.Context) -> None:
    """List active captive portal sessions."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.search_sessions(), lctx.output_format))


@captiveportal.command("disconnect")
@click.argument("zone_id")
@click.pass_context
@handle_api_errors
def disconnect(ctx: click.Context, zone_id: str) -> None:
    """Disconnect all sessions in a zone."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.disconnect_session(zone_id=zone_id), lctx.output_format))


# ===========================================================================
# Vouchers
# ===========================================================================


@captiveportal.group("voucher")
def voucher() -> None:
    """Manage captive portal vouchers."""


@voucher.command("providers")
@click.pass_context
@handle_api_errors
def voucher_providers(ctx: click.Context) -> None:
    """List voucher providers."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.list_voucher_providers(), lctx.output_format))


@voucher.command("groups")
@click.argument("provider")
@click.pass_context
@handle_api_errors
def voucher_groups(ctx: click.Context, provider: str) -> None:
    """List voucher groups for a provider."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.list_voucher_groups(provider), lctx.output_format))


@voucher.command("list")
@click.argument("provider")
@click.argument("group")
@click.pass_context
@handle_api_errors
def voucher_list(ctx: click.Context, provider: str, group: str) -> None:
    """List vouchers in a group."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.list_vouchers(provider, group), lctx.output_format))


@voucher.command("drop-group")
@click.argument("provider")
@click.argument("group")
@click.pass_context
@handle_api_errors
def voucher_drop_group(ctx: click.Context, provider: str, group: str) -> None:
    """Drop an entire voucher group."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.drop_voucher_group(provider, group), lctx.output_format))


@voucher.command("drop-expired")
@click.argument("provider")
@click.argument("group")
@click.pass_context
@handle_api_errors
def voucher_drop_expired(ctx: click.Context, provider: str, group: str) -> None:
    """Drop expired vouchers from a group."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.drop_expired_vouchers(provider, group), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@captiveportal.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show captive portal service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.status(), lctx.output_format))


@captiveportal.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply captive portal configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.reconfigure(), lctx.output_format))


@captiveportal.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the captive portal service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.start(), lctx.output_format))


@captiveportal.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the captive portal service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.stop(), lctx.output_format))


@captiveportal.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the captive portal service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.captiveportal.restart(), lctx.output_format))
