from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.unbound import HostAlias, HostOverride, UnboundAcl, UnboundDot


@click.group()
def unbound() -> None:
    """Manage the Unbound DNS resolver."""


# ===========================================================================
# Host overrides
# ===========================================================================


@unbound.group("host")
def host() -> None:
    """Manage DNS host overrides."""


@host.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def host_list(ctx: click.Context, search: str) -> None:
    """List host overrides."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.search_host_overrides(SearchRequest(searchPhrase=search)), lctx.output_format))


@host.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def host_get(ctx: click.Context, uuid: str) -> None:
    """Get a host override by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.get_host_override(uuid), lctx.output_format))


@host.command("add")
@click.option("--hostname", default=None)
@click.option("--domain", default=None)
@click.option("--server", default=None, help="IP address the hostname resolves to.")
@click.option("--rr", default=None, help="Record type: A, AAAA, MX, ...")
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--addptr", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def host_add(
    ctx: click.Context, hostname: str | None, domain: str | None, server: str | None,
    rr: str | None, description: str | None, enabled: str | None,
    addptr: str | None, from_json: str | None,
) -> None:
    """Add a DNS host override."""
    lctx = get_ctx(ctx)
    obj = build_model(HostOverride, from_json, hostname=hostname, domain=domain,
                      server=server, rr=rr, description=description, enabled=enabled,
                      addptr=addptr)
    click.echo(render(lctx.client.unbound.add_host_override(obj), lctx.output_format))


@host.command("set")
@click.argument("uuid")
@click.option("--hostname", default=None)
@click.option("--domain", default=None)
@click.option("--server", default=None)
@click.option("--rr", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--addptr", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def host_set(
    ctx: click.Context, uuid: str, hostname: str | None, domain: str | None,
    server: str | None, rr: str | None, description: str | None,
    enabled: str | None, addptr: str | None, from_json: str | None,
) -> None:
    """Update a DNS host override."""
    lctx = get_ctx(ctx)
    obj = build_model(HostOverride, from_json, hostname=hostname, domain=domain,
                      server=server, rr=rr, description=description, enabled=enabled,
                      addptr=addptr)
    click.echo(render(lctx.client.unbound.set_host_override(uuid, obj), lctx.output_format))


@host.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def host_del(ctx: click.Context, uuid: str) -> None:
    """Delete a DNS host override."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.del_host_override(uuid), lctx.output_format))


@host.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def host_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a DNS host override."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.toggle_host_override(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Host aliases
# ===========================================================================


@unbound.group("alias")
def host_alias() -> None:
    """Manage DNS host aliases (CNAMEs)."""


@host_alias.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def alias_list(ctx: click.Context, search: str) -> None:
    """List host aliases."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.search_host_aliases(SearchRequest(searchPhrase=search)), lctx.output_format))


@host_alias.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def alias_get(ctx: click.Context, uuid: str) -> None:
    """Get a host alias by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.get_host_alias(uuid), lctx.output_format))


@host_alias.command("add")
@click.option("--host", "host_uuid", default=None, help="UUID of the host override to alias.")
@click.option("--hostname", default=None)
@click.option("--domain", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def alias_add(
    ctx: click.Context, host_uuid: str | None, hostname: str | None, domain: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add a host alias."""
    lctx = get_ctx(ctx)
    obj = build_model(HostAlias, from_json, host=host_uuid, hostname=hostname,
                      domain=domain, description=description, enabled=enabled)
    click.echo(render(lctx.client.unbound.add_host_alias(obj), lctx.output_format))


@host_alias.command("set")
@click.argument("uuid")
@click.option("--host", "host_uuid", default=None)
@click.option("--hostname", default=None)
@click.option("--domain", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def alias_set(
    ctx: click.Context, uuid: str, host_uuid: str | None, hostname: str | None,
    domain: str | None, description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Update a host alias."""
    lctx = get_ctx(ctx)
    obj = build_model(HostAlias, from_json, host=host_uuid, hostname=hostname,
                      domain=domain, description=description, enabled=enabled)
    click.echo(render(lctx.client.unbound.set_host_alias(uuid, obj), lctx.output_format))


@host_alias.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def alias_del(ctx: click.Context, uuid: str) -> None:
    """Delete a host alias."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.del_host_alias(uuid), lctx.output_format))


@host_alias.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def alias_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a host alias."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.toggle_host_alias(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Forwards (DoT / upstream resolvers)
# ===========================================================================


@unbound.group("forward")
def forward() -> None:
    """Manage DNS forwards and DoT upstreams."""


@forward.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def forward_list(ctx: click.Context, search: str) -> None:
    """List DNS forwards."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.search_forwards(SearchRequest(searchPhrase=search)), lctx.output_format))


@forward.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def forward_get(ctx: click.Context, uuid: str) -> None:
    """Get a DNS forward by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.get_forward(uuid), lctx.output_format))


@forward.command("add")
@click.option("--server", default=None, help="Upstream resolver IP.")
@click.option("--port", default=None)
@click.option("--type", "type_", default=None, help="dot, forward")
@click.option("--domain", default=None, help="Domain to forward (empty = all).")
@click.option("--verify", default=None, help="TLS verify hostname.")
@click.option("--enabled", default=None)
@click.option("--description", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def forward_add(
    ctx: click.Context, server: str | None, port: str | None, type_: str | None,
    domain: str | None, verify: str | None, enabled: str | None,
    description: str | None, from_json: str | None,
) -> None:
    """Add a DNS forward / DoT upstream."""
    lctx = get_ctx(ctx)
    obj = build_model(UnboundDot, from_json, server=server, port=port, type=type_,
                      domain=domain, verify=verify, enabled=enabled, description=description)
    click.echo(render(lctx.client.unbound.add_forward(obj), lctx.output_format))


@forward.command("set")
@click.argument("uuid")
@click.option("--server", default=None)
@click.option("--port", default=None)
@click.option("--type", "type_", default=None)
@click.option("--domain", default=None)
@click.option("--verify", default=None)
@click.option("--enabled", default=None)
@click.option("--description", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def forward_set(
    ctx: click.Context, uuid: str, server: str | None, port: str | None, type_: str | None,
    domain: str | None, verify: str | None, enabled: str | None,
    description: str | None, from_json: str | None,
) -> None:
    """Update a DNS forward."""
    lctx = get_ctx(ctx)
    obj = build_model(UnboundDot, from_json, server=server, port=port, type=type_,
                      domain=domain, verify=verify, enabled=enabled, description=description)
    click.echo(render(lctx.client.unbound.set_forward(uuid, obj), lctx.output_format))


@forward.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def forward_del(ctx: click.Context, uuid: str) -> None:
    """Delete a DNS forward."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.del_forward(uuid), lctx.output_format))


@forward.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def forward_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a DNS forward."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.toggle_forward(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# ACLs
# ===========================================================================


@unbound.group("acl")
def acl() -> None:
    """Manage Unbound access control lists."""


@acl.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def acl_list(ctx: click.Context, search: str) -> None:
    """List ACL entries."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.search_acls(SearchRequest(searchPhrase=search)), lctx.output_format))


@acl.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def acl_get(ctx: click.Context, uuid: str) -> None:
    """Get an ACL entry by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.get_acl(uuid), lctx.output_format))


@acl.command("add")
@click.option("--name", default=None)
@click.option("--action", default=None, help="allow, refuse, deny, allow_snoop")
@click.option("--networks", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def acl_add(
    ctx: click.Context, name: str | None, action: str | None, networks: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add an ACL entry."""
    lctx = get_ctx(ctx)
    obj = build_model(UnboundAcl, from_json, name=name, action=action, networks=networks,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.unbound.add_acl(obj), lctx.output_format))


@acl.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def acl_del(ctx: click.Context, uuid: str) -> None:
    """Delete an ACL entry."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.del_acl(uuid), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@unbound.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply Unbound configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.reconfigure(), lctx.output_format))


@unbound.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show Unbound service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.status(), lctx.output_format))


@unbound.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the Unbound service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.start(), lctx.output_format))


@unbound.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the Unbound service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.stop(), lctx.output_format))


@unbound.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the Unbound service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.unbound.restart(), lctx.output_format))
