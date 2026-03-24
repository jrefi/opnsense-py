from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render


@click.group()
def diagnostics() -> None:
    """System diagnostics: ARP, routes, states, interfaces, traffic."""


# ===========================================================================
# System info
# ===========================================================================


@diagnostics.command("info")
@click.pass_context
@handle_api_errors
def system_info(ctx: click.Context) -> None:
    """Show system information (uptime, version, CPU, etc.)."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.system_information(), lctx.output_format))


@diagnostics.command("resources")
@click.pass_context
@handle_api_errors
def resources(ctx: click.Context) -> None:
    """Show CPU, memory, and disk resource usage."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.system_resources(), lctx.output_format))


@diagnostics.command("memory")
@click.pass_context
@handle_api_errors
def memory(ctx: click.Context) -> None:
    """Show detailed memory statistics."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.system_memory(), lctx.output_format))


@diagnostics.command("disk")
@click.pass_context
@handle_api_errors
def disk(ctx: click.Context) -> None:
    """Show disk usage."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.system_disk(), lctx.output_format))


@diagnostics.command("temperature")
@click.pass_context
@handle_api_errors
def temperature(ctx: click.Context) -> None:
    """Show hardware temperature sensors."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.system_temperature(), lctx.output_format))


@diagnostics.command("time")
@click.pass_context
@handle_api_errors
def time(ctx: click.Context) -> None:
    """Show system time."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.system_time(), lctx.output_format))


# ===========================================================================
# ARP / NDP
# ===========================================================================


@diagnostics.command("arp")
@click.pass_context
@handle_api_errors
def arp(ctx: click.Context) -> None:
    """Show ARP table."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.search_arp(), lctx.output_format))


@diagnostics.command("ndp")
@click.pass_context
@handle_api_errors
def ndp(ctx: click.Context) -> None:
    """Show IPv6 NDP neighbor table."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.search_ndp(), lctx.output_format))


@diagnostics.command("flush-arp")
@click.pass_context
@handle_api_errors
def flush_arp(ctx: click.Context) -> None:
    """Flush the ARP table."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.flush_arp(), lctx.output_format))


# ===========================================================================
# Routes
# ===========================================================================


@diagnostics.command("routes")
@click.pass_context
@handle_api_errors
def routes(ctx: click.Context) -> None:
    """Show the kernel routing table."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.get_routes(), lctx.output_format))


# ===========================================================================
# Interfaces
# ===========================================================================


@diagnostics.command("interfaces")
@click.pass_context
@handle_api_errors
def interfaces(ctx: click.Context) -> None:
    """Show interface statistics."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.get_interface_statistics(), lctx.output_format))


@diagnostics.command("interface-names")
@click.pass_context
@handle_api_errors
def interface_names(ctx: click.Context) -> None:
    """List interface names."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.get_interface_names(), lctx.output_format))


@diagnostics.command("vip-status")
@click.pass_context
@handle_api_errors
def vip_status(ctx: click.Context) -> None:
    """Show CARP/VIP status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.get_vip_status(), lctx.output_format))


# ===========================================================================
# Firewall states
# ===========================================================================


@diagnostics.command("states")
@click.pass_context
@handle_api_errors
def states(ctx: click.Context) -> None:
    """Show firewall state table summary."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.get_pf_states(), lctx.output_format))


@diagnostics.command("flush-states")
@click.pass_context
@handle_api_errors
def flush_states(ctx: click.Context) -> None:
    """Flush all firewall states."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.flush_states(), lctx.output_format))


@diagnostics.command("pf-stats")
@click.option("--section", default=None, help="Specific statistics section.")
@click.pass_context
@handle_api_errors
def pf_stats(ctx: click.Context, section: str | None) -> None:
    """Show pf statistics."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.get_pf_statistics(section), lctx.output_format))


# ===========================================================================
# Traffic
# ===========================================================================


@diagnostics.command("traffic")
@click.pass_context
@handle_api_errors
def traffic(ctx: click.Context) -> None:
    """Show live interface traffic counters."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.traffic_interface(), lctx.output_format))


@diagnostics.command("activity")
@click.pass_context
@handle_api_errors
def activity(ctx: click.Context) -> None:
    """Show system process activity (top)."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.diagnostics.get_activity(), lctx.output_format))
