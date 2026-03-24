from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.routing import Gateway


@click.group()
def routing() -> None:
    """Manage gateway definitions."""


@routing.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def gateway_list(ctx: click.Context, search: str) -> None:
    """List gateways."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routing.search_gateways(SearchRequest(searchPhrase=search)), lctx.output_format))


@routing.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def gateway_get(ctx: click.Context, uuid: str) -> None:
    """Get a gateway by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routing.get_gateway(uuid), lctx.output_format))


@routing.command("add")
@click.option("--name", default=None, required=True, help="Gateway name.")
@click.option("--interface", default=None, required=True)
@click.option("--gateway", default=None, help="Gateway IP address.")
@click.option("--ipprotocol", default=None, help="inet or inet6")
@click.option("--descr", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def gateway_add(
    ctx: click.Context, name: str | None, interface: str | None, gateway: str | None,
    ipprotocol: str | None, descr: str | None, from_json: str | None,
) -> None:
    """Add a gateway."""
    lctx = get_ctx(ctx)
    obj = build_model(Gateway, from_json, name=name, interface=interface,
                      gateway=gateway, ipprotocol=ipprotocol, descr=descr)
    click.echo(render(lctx.client.routing.add_gateway(obj), lctx.output_format))


@routing.command("set")
@click.argument("uuid")
@click.option("--name", default=None)
@click.option("--interface", default=None)
@click.option("--gateway", default=None)
@click.option("--ipprotocol", default=None)
@click.option("--descr", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def gateway_set(
    ctx: click.Context, uuid: str, name: str | None, interface: str | None, gateway: str | None,
    ipprotocol: str | None, descr: str | None, from_json: str | None,
) -> None:
    """Update a gateway."""
    lctx = get_ctx(ctx)
    obj = build_model(Gateway, from_json, name=name, interface=interface,
                      gateway=gateway, ipprotocol=ipprotocol, descr=descr)
    click.echo(render(lctx.client.routing.set_gateway(uuid, obj), lctx.output_format))


@routing.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def gateway_del(ctx: click.Context, uuid: str) -> None:
    """Delete a gateway."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routing.del_gateway(uuid), lctx.output_format))


@routing.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def gateway_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a gateway on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routing.toggle_gateway(uuid, enabled=enable), lctx.output_format))


@routing.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply routing configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routing.reconfigure(), lctx.output_format))
