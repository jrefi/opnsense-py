from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.routes import Route


@click.group()
def routes() -> None:
    """Manage static routes and gateway status."""


@routes.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def routes_list(ctx: click.Context, search: str) -> None:
    """List static routes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routes.search_routes(SearchRequest(searchPhrase=search)), lctx.output_format))


@routes.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def routes_get(ctx: click.Context, uuid: str) -> None:
    """Get a static route by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routes.get_route(uuid), lctx.output_format))


@routes.command("add")
@click.option("--network", required=True, help="Destination network, e.g. 192.168.10.0/24.")
@click.option("--gateway", required=True, help="Gateway name or IP.")
@click.option("--descr", default=None, help="Description.")
@click.option("--disabled", default=None, help='"1" to disable the route.')
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def routes_add(
    ctx: click.Context, network: str, gateway: str, descr: str | None,
    disabled: str | None, from_json: str | None,
) -> None:
    """Add a static route."""
    lctx = get_ctx(ctx)
    obj = build_model(Route, from_json, network=network, gateway=gateway,
                      descr=descr, disabled=disabled)
    click.echo(render(lctx.client.routes.add_route(obj), lctx.output_format))


@routes.command("set")
@click.argument("uuid")
@click.option("--network", default=None)
@click.option("--gateway", default=None)
@click.option("--descr", default=None)
@click.option("--disabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def routes_set(
    ctx: click.Context, uuid: str, network: str | None, gateway: str | None,
    descr: str | None, disabled: str | None, from_json: str | None,
) -> None:
    """Update a static route."""
    lctx = get_ctx(ctx)
    obj = build_model(Route, from_json, network=network, gateway=gateway,
                      descr=descr, disabled=disabled)
    click.echo(render(lctx.client.routes.set_route(uuid, obj), lctx.output_format))


@routes.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def routes_del(ctx: click.Context, uuid: str) -> None:
    """Delete a static route."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routes.del_route(uuid), lctx.output_format))


@routes.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def routes_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a static route on or off."""
    lctx = get_ctx(ctx)
    # API uses disabled=True to disable, disabled=False to enable
    disabled = (not enable) if enable is not None else None
    click.echo(render(lctx.client.routes.toggle_route(uuid, disabled=disabled), lctx.output_format))


@routes.command("gateways")
@click.pass_context
@handle_api_errors
def gateways(ctx: click.Context) -> None:
    """Show gateway status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routes.gateway_status(), lctx.output_format))


@routes.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply route configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.routes.reconfigure(), lctx.output_format))
