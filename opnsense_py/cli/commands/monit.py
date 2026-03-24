from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.monit import MonitAlert, MonitService, MonitTest


@click.group()
def monit() -> None:
    """Manage Monit service checks, tests, and alerts."""


# ===========================================================================
# Services
# ===========================================================================


@monit.group("service")
def service() -> None:
    """Manage Monit service checks."""


@service.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def service_list(ctx: click.Context, search: str) -> None:
    """List Monit service checks."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.search_services(SearchRequest(searchPhrase=search)), lctx.output_format))


@service.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def service_get(ctx: click.Context, uuid: str) -> None:
    """Get a Monit service check by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.get_service(uuid), lctx.output_format))


@service.command("add")
@click.option("--name", default=None)
@click.option("--type", "type_", default=None, help="Service type (process, host, etc.)")
@click.option("--address", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def service_add(
    ctx: click.Context, name: str | None, type_: str | None, address: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add a Monit service check."""
    lctx = get_ctx(ctx)
    obj = build_model(MonitService, from_json, name=name, type=type_, address=address,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.monit.add_service(obj), lctx.output_format))


@service.command("set")
@click.argument("uuid")
@click.option("--name", default=None)
@click.option("--type", "type_", default=None)
@click.option("--address", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def service_set(
    ctx: click.Context, uuid: str, name: str | None, type_: str | None, address: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Update a Monit service check."""
    lctx = get_ctx(ctx)
    obj = build_model(MonitService, from_json, name=name, type=type_, address=address,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.monit.set_service(uuid, obj), lctx.output_format))


@service.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def service_del(ctx: click.Context, uuid: str) -> None:
    """Delete a Monit service check."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.del_service(uuid), lctx.output_format))


@service.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def service_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a Monit service check."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.toggle_service(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Tests
# ===========================================================================


@monit.group("test")
def test() -> None:
    """Manage Monit test conditions."""


@test.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def test_list(ctx: click.Context, search: str) -> None:
    """List Monit test conditions."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.search_tests(SearchRequest(searchPhrase=search)), lctx.output_format))


@test.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def test_get(ctx: click.Context, uuid: str) -> None:
    """Get a Monit test by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.get_test(uuid), lctx.output_format))


@test.command("add")
@click.option("--name", default=None)
@click.option("--type", "type_", default=None)
@click.option("--condition", default=None)
@click.option("--action", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def test_add(
    ctx: click.Context, name: str | None, type_: str | None,
    condition: str | None, action: str | None, from_json: str | None,
) -> None:
    """Add a Monit test condition."""
    lctx = get_ctx(ctx)
    obj = build_model(MonitTest, from_json, name=name, type=type_,
                      condition=condition, action=action)
    click.echo(render(lctx.client.monit.add_test(obj), lctx.output_format))


@test.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def test_del(ctx: click.Context, uuid: str) -> None:
    """Delete a Monit test condition."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.del_test(uuid), lctx.output_format))


# ===========================================================================
# Alerts
# ===========================================================================


@monit.group("alert")
def alert() -> None:
    """Manage Monit email alerts."""


@alert.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def alert_list(ctx: click.Context, search: str) -> None:
    """List Monit alerts."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.search_alerts(SearchRequest(searchPhrase=search)), lctx.output_format))


@alert.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def alert_get(ctx: click.Context, uuid: str) -> None:
    """Get a Monit alert by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.get_alert(uuid), lctx.output_format))


@alert.command("add")
@click.option("--recipient", default=None, help="Email recipient address.")
@click.option("--events", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def alert_add(
    ctx: click.Context, recipient: str | None, events: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add a Monit alert."""
    lctx = get_ctx(ctx)
    obj = build_model(MonitAlert, from_json, recipient=recipient, events=events,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.monit.add_alert(obj), lctx.output_format))


@alert.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def alert_del(ctx: click.Context, uuid: str) -> None:
    """Delete a Monit alert."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.del_alert(uuid), lctx.output_format))


@alert.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def alert_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a Monit alert."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.toggle_alert(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@monit.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show Monit service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.status(), lctx.output_format))


@monit.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply Monit configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.reconfigure(), lctx.output_format))


@monit.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the Monit service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.start(), lctx.output_format))


@monit.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the Monit service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.stop(), lctx.output_format))


@monit.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the Monit service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.monit.restart(), lctx.output_format))
