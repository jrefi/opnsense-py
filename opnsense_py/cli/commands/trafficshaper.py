from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.trafficshaper import ShaperPipe, ShaperQueue, ShaperRule


@click.group()
def trafficshaper() -> None:
    """Manage traffic shaper pipes, queues, and rules."""


# ===========================================================================
# Pipes
# ===========================================================================


@trafficshaper.group("pipe")
def pipe() -> None:
    """Manage traffic shaper pipes."""


@pipe.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def pipe_list(ctx: click.Context, search: str) -> None:
    """List shaper pipes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.search_pipes(SearchRequest(searchPhrase=search)), lctx.output_format))


@pipe.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def pipe_get(ctx: click.Context, uuid: str) -> None:
    """Get a pipe by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.get_pipe(uuid), lctx.output_format))


@pipe.command("add")
@click.option("--bandwidth", default=None, type=int, help="Bandwidth in Kbit/s.")
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def pipe_add(
    ctx: click.Context, bandwidth: int | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Add a shaper pipe."""
    lctx = get_ctx(ctx)
    obj = build_model(ShaperPipe, from_json, bandwidth=bandwidth,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.trafficshaper.add_pipe(obj), lctx.output_format))


@pipe.command("set")
@click.argument("uuid")
@click.option("--bandwidth", default=None, type=int)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def pipe_set(
    ctx: click.Context, uuid: str, bandwidth: int | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Update a shaper pipe."""
    lctx = get_ctx(ctx)
    obj = build_model(ShaperPipe, from_json, bandwidth=bandwidth,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.trafficshaper.set_pipe(uuid, obj), lctx.output_format))


@pipe.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def pipe_del(ctx: click.Context, uuid: str) -> None:
    """Delete a shaper pipe."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.del_pipe(uuid), lctx.output_format))


@pipe.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def pipe_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a shaper pipe."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.toggle_pipe(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Queues
# ===========================================================================


@trafficshaper.group("queue")
def queue() -> None:
    """Manage traffic shaper queues."""


@queue.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def queue_list(ctx: click.Context, search: str) -> None:
    """List shaper queues."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.search_queues(SearchRequest(searchPhrase=search)), lctx.output_format))


@queue.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def queue_get(ctx: click.Context, uuid: str) -> None:
    """Get a queue by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.get_queue(uuid), lctx.output_format))


@queue.command("add")
@click.option("--pipe", default=None, help="Parent pipe UUID.")
@click.option("--weight", default=None, type=int)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def queue_add(
    ctx: click.Context, pipe: str | None, weight: int | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add a shaper queue."""
    lctx = get_ctx(ctx)
    obj = build_model(ShaperQueue, from_json, pipe=pipe, weight=weight,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.trafficshaper.add_queue(obj), lctx.output_format))


@queue.command("set")
@click.argument("uuid")
@click.option("--pipe", default=None)
@click.option("--weight", default=None, type=int)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def queue_set(
    ctx: click.Context, uuid: str, pipe: str | None, weight: int | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Update a shaper queue."""
    lctx = get_ctx(ctx)
    obj = build_model(ShaperQueue, from_json, pipe=pipe, weight=weight,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.trafficshaper.set_queue(uuid, obj), lctx.output_format))


@queue.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def queue_del(ctx: click.Context, uuid: str) -> None:
    """Delete a shaper queue."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.del_queue(uuid), lctx.output_format))


@queue.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def queue_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a shaper queue."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.toggle_queue(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Rules
# ===========================================================================


@trafficshaper.group("rule")
def rule() -> None:
    """Manage traffic shaper rules."""


@rule.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def rule_list(ctx: click.Context, search: str) -> None:
    """List shaper rules."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.search_rules(SearchRequest(searchPhrase=search)), lctx.output_format))


@rule.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def rule_get(ctx: click.Context, uuid: str) -> None:
    """Get a shaper rule by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.get_rule(uuid), lctx.output_format))


@rule.command("add")
@click.option("--interface", default=None)
@click.option("--proto", default=None, help="Protocol (tcp, udp, etc.)")
@click.option("--source", default=None)
@click.option("--destination", default=None)
@click.option("--target", default=None, help="Target pipe or queue UUID.")
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def rule_add(
    ctx: click.Context, interface: str | None, proto: str | None, source: str | None,
    destination: str | None, target: str | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Add a shaper rule."""
    lctx = get_ctx(ctx)
    obj = build_model(ShaperRule, from_json, interface=interface, proto=proto,
                      source=source, destination=destination, target=target,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.trafficshaper.add_rule(obj), lctx.output_format))


@rule.command("set")
@click.argument("uuid")
@click.option("--interface", default=None)
@click.option("--proto", default=None)
@click.option("--source", default=None)
@click.option("--destination", default=None)
@click.option("--target", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def rule_set(
    ctx: click.Context, uuid: str, interface: str | None, proto: str | None, source: str | None,
    destination: str | None, target: str | None, description: str | None,
    enabled: str | None, from_json: str | None,
) -> None:
    """Update a shaper rule."""
    lctx = get_ctx(ctx)
    obj = build_model(ShaperRule, from_json, interface=interface, proto=proto,
                      source=source, destination=destination, target=target,
                      description=description, enabled=enabled)
    click.echo(render(lctx.client.trafficshaper.set_rule(uuid, obj), lctx.output_format))


@rule.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def rule_del(ctx: click.Context, uuid: str) -> None:
    """Delete a shaper rule."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.del_rule(uuid), lctx.output_format))


@rule.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def rule_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a shaper rule."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.toggle_rule(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@trafficshaper.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply traffic shaper configuration."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.reconfigure(), lctx.output_format))


@trafficshaper.command("statistics")
@click.pass_context
@handle_api_errors
def statistics(ctx: click.Context) -> None:
    """Show traffic shaper statistics."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trafficshaper.statistics(), lctx.output_format))
