from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.openvpn import OpenVPNInstance, OpenVPNOverwrite


@click.group()
def openvpn() -> None:
    """Manage OpenVPN instances, overwrites, and sessions."""


# ===========================================================================
# Instances
# ===========================================================================


@openvpn.group("instance")
def instance() -> None:
    """Manage OpenVPN server/client instances."""


@instance.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def instance_list(ctx: click.Context, search: str) -> None:
    """List OpenVPN instances."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.search_instances(SearchRequest(searchPhrase=search)), lctx.output_format))


@instance.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def instance_get(ctx: click.Context, uuid: str) -> None:
    """Get an OpenVPN instance by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.get_instance(uuid), lctx.output_format))


@instance.command("add")
@click.option("--role", default=None, help="server or client")
@click.option("--proto", default=None, help="udp, tcp-server, tcp-client")
@click.option("--port", default=None)
@click.option("--server", default=None, help="Server network, e.g. 10.8.0.0/24")
@click.option("--remote", default=None, help="Remote host (client mode).")
@click.option("--cert", default=None, help="Certificate UUID.")
@click.option("--ca", default=None, help="CA UUID.")
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def instance_add(
    ctx: click.Context, role: str | None, proto: str | None, port: str | None,
    server: str | None, remote: str | None, cert: str | None, ca: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add an OpenVPN instance."""
    lctx = get_ctx(ctx)
    obj = build_model(OpenVPNInstance, from_json, role=role, proto=proto, port=port,
                      server=server, remote=remote, cert=cert, ca=ca,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.openvpn.add_instance(obj), lctx.output_format))


@instance.command("set")
@click.argument("uuid")
@click.option("--role", default=None)
@click.option("--proto", default=None)
@click.option("--port", default=None)
@click.option("--server", default=None)
@click.option("--remote", default=None)
@click.option("--cert", default=None)
@click.option("--ca", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def instance_set(
    ctx: click.Context, uuid: str, role: str | None, proto: str | None, port: str | None,
    server: str | None, remote: str | None, cert: str | None, ca: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Update an OpenVPN instance."""
    lctx = get_ctx(ctx)
    obj = build_model(OpenVPNInstance, from_json, role=role, proto=proto, port=port,
                      server=server, remote=remote, cert=cert, ca=ca,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.openvpn.set_instance(uuid, obj), lctx.output_format))


@instance.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def instance_del(ctx: click.Context, uuid: str) -> None:
    """Delete an OpenVPN instance."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.del_instance(uuid), lctx.output_format))


@instance.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def instance_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle an OpenVPN instance on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.toggle_instance(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Client overwrites
# ===========================================================================


@openvpn.group("overwrite")
def overwrite() -> None:
    """Manage OpenVPN client-specific configuration overwrites."""


@overwrite.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def overwrite_list(ctx: click.Context, search: str) -> None:
    """List client overwrites."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.search_client_overwrites(SearchRequest(searchPhrase=search)), lctx.output_format))


@overwrite.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def overwrite_get(ctx: click.Context, uuid: str) -> None:
    """Get a client overwrite by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.get_client_overwrite(uuid), lctx.output_format))


@overwrite.command("add")
@click.option("--common-name", "common_name", default=None)
@click.option("--servers", default=None, help="Comma-separated server UUIDs.")
@click.option("--tunnel-network", "tunnel_network", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def overwrite_add(
    ctx: click.Context, common_name: str | None, servers: str | None,
    tunnel_network: str | None, description: str | None, enabled: str | None,
    from_json: str | None,
) -> None:
    """Add a client overwrite."""
    lctx = get_ctx(ctx)
    obj = build_model(OpenVPNOverwrite, from_json, common_name=common_name, servers=servers,
                      tunnel_network=tunnel_network, description=description, enabled=enabled)
    click.echo(render(lctx.client.openvpn.add_client_overwrite(obj), lctx.output_format))


@overwrite.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def overwrite_del(ctx: click.Context, uuid: str) -> None:
    """Delete a client overwrite."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.del_client_overwrite(uuid), lctx.output_format))


# ===========================================================================
# Sessions
# ===========================================================================


@openvpn.command("sessions")
@click.pass_context
@handle_api_errors
def sessions(ctx: click.Context) -> None:
    """List active OpenVPN sessions."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.search_sessions(), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@openvpn.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply OpenVPN configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.reconfigure(), lctx.output_format))


@openvpn.command("start")
@click.option("--id", "service_id", default=None, help="Instance UUID (omit for all).")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context, service_id: str | None) -> None:
    """Start OpenVPN service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.start_service(service_id), lctx.output_format))


@openvpn.command("stop")
@click.option("--id", "service_id", default=None, help="Instance UUID (omit for all).")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context, service_id: str | None) -> None:
    """Stop OpenVPN service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.stop_service(service_id), lctx.output_format))


@openvpn.command("restart")
@click.option("--id", "service_id", default=None, help="Instance UUID (omit for all).")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context, service_id: str | None) -> None:
    """Restart OpenVPN service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.openvpn.restart_service(service_id), lctx.output_format))
