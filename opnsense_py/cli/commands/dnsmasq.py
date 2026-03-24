from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.dnsmasq import DnsmasqDomainOverride, DnsmasqHost


@click.group()
def dnsmasq() -> None:
    """Manage Dnsmasq DNS/DHCP host entries and domain overrides."""


# ===========================================================================
# Hosts
# ===========================================================================


@dnsmasq.group("host")
def host() -> None:
    """Manage Dnsmasq host entries."""


@host.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def host_list(ctx: click.Context, search: str) -> None:
    """List host entries."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.search_hosts(SearchRequest(searchPhrase=search)), lctx.output_format))


@host.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def host_get(ctx: click.Context, uuid: str) -> None:
    """Get a host entry by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.get_host(uuid), lctx.output_format))


@host.command("add")
@click.option("--hostname", default=None)
@click.option("--domain", default=None)
@click.option("--ip", default=None, help="IP address.")
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def host_add(
    ctx: click.Context, hostname: str | None, domain: str | None,
    ip: str | None, description: str | None, enabled: str | None,
    from_json: str | None,
) -> None:
    """Add a host entry."""
    lctx = get_ctx(ctx)
    obj = build_model(DnsmasqHost, from_json, hostname=hostname, domain=domain,
                      ip=ip, description=description, enabled=enabled)
    click.echo(render(lctx.client.dnsmasq.add_host(obj), lctx.output_format))


@host.command("set")
@click.argument("uuid")
@click.option("--hostname", default=None)
@click.option("--domain", default=None)
@click.option("--ip", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def host_set(
    ctx: click.Context, uuid: str, hostname: str | None, domain: str | None,
    ip: str | None, description: str | None, enabled: str | None,
    from_json: str | None,
) -> None:
    """Update a host entry."""
    lctx = get_ctx(ctx)
    obj = build_model(DnsmasqHost, from_json, hostname=hostname, domain=domain,
                      ip=ip, description=description, enabled=enabled)
    click.echo(render(lctx.client.dnsmasq.set_host(uuid, obj), lctx.output_format))


@host.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def host_del(ctx: click.Context, uuid: str) -> None:
    """Delete a host entry."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.del_host(uuid), lctx.output_format))


# ===========================================================================
# Domain overrides
# ===========================================================================


@dnsmasq.group("domain")
def domain() -> None:
    """Manage Dnsmasq domain overrides."""


@domain.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def domain_list(ctx: click.Context, search: str) -> None:
    """List domain overrides."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.search_domains(SearchRequest(searchPhrase=search)), lctx.output_format))


@domain.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def domain_get(ctx: click.Context, uuid: str) -> None:
    """Get a domain override by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.get_domain(uuid), lctx.output_format))


@domain.command("add")
@click.option("--domain", default=None)
@click.option("--ip", default=None, help="Upstream DNS server IP.")
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def domain_add(
    ctx: click.Context, domain: str | None, ip: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add a domain override."""
    lctx = get_ctx(ctx)
    obj = build_model(DnsmasqDomainOverride, from_json, domain=domain, ip=ip,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.dnsmasq.add_domain(obj), lctx.output_format))


@domain.command("set")
@click.argument("uuid")
@click.option("--domain", default=None)
@click.option("--ip", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def domain_set(
    ctx: click.Context, uuid: str, domain: str | None, ip: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Update a domain override."""
    lctx = get_ctx(ctx)
    obj = build_model(DnsmasqDomainOverride, from_json, domain=domain, ip=ip,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.dnsmasq.set_domain(uuid, obj), lctx.output_format))


@domain.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def domain_del(ctx: click.Context, uuid: str) -> None:
    """Delete a domain override."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.del_domain(uuid), lctx.output_format))


# ===========================================================================
# Leases
# ===========================================================================


@dnsmasq.command("leases")
@click.pass_context
@handle_api_errors
def leases(ctx: click.Context) -> None:
    """Show active DHCP leases."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.search_leases(), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@dnsmasq.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show Dnsmasq service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.status(), lctx.output_format))


@dnsmasq.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply Dnsmasq configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.reconfigure(), lctx.output_format))


@dnsmasq.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the Dnsmasq service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.start(), lctx.output_format))


@dnsmasq.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the Dnsmasq service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.stop(), lctx.output_format))


@dnsmasq.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the Dnsmasq service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.dnsmasq.restart(), lctx.output_format))
