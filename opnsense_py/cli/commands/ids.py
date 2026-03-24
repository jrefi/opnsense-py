from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.ids import IDSPolicy, IDSUserRule


@click.group()
def ids() -> None:
    """Manage IDS/IPS (Suricata) policies, rules, and alerts."""


# ===========================================================================
# Policies
# ===========================================================================


@ids.group("policy")
def policy() -> None:
    """Manage IDS policies."""


@policy.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def policy_list(ctx: click.Context, search: str) -> None:
    """List IDS policies."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.search_policies(SearchRequest(searchPhrase=search)), lctx.output_format))


@policy.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def policy_get(ctx: click.Context, uuid: str) -> None:
    """Get an IDS policy by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.get_policy(uuid), lctx.output_format))


@policy.command("add")
@click.option("--description", default=None)
@click.option("--action", default=None, help="alert, drop, or pass")
@click.option("--rulesets", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def policy_add(
    ctx: click.Context, description: str | None, action: str | None,
    rulesets: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add an IDS policy."""
    lctx = get_ctx(ctx)
    obj = build_model(IDSPolicy, from_json, description=description, action=action,
                      rulesets=rulesets, enabled=enabled)
    click.echo(render(lctx.client.ids.add_policy(obj), lctx.output_format))


@policy.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def policy_del(ctx: click.Context, uuid: str) -> None:
    """Delete an IDS policy."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.del_policy(uuid), lctx.output_format))


@policy.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def policy_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle an IDS policy."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.toggle_policy(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# User rules
# ===========================================================================


@ids.group("rule")
def rule() -> None:
    """Manage custom IDS user rules."""


@rule.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def rule_list(ctx: click.Context, search: str) -> None:
    """List user-defined IDS rules."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.search_user_rules(SearchRequest(searchPhrase=search)), lctx.output_format))


@rule.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def rule_get(ctx: click.Context, uuid: str) -> None:
    """Get a user rule by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.get_user_rule(uuid), lctx.output_format))


@rule.command("add")
@click.option("--source", default=None)
@click.option("--destination", default=None)
@click.option("--action", default=None, help="alert, drop, or pass")
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def rule_add(
    ctx: click.Context, source: str | None, destination: str | None, action: str | None,
    description: str | None, enabled: str | None, from_json: str | None,
) -> None:
    """Add a user-defined IDS rule."""
    lctx = get_ctx(ctx)
    obj = build_model(IDSUserRule, from_json, source=source, destination=destination,
                      action=action, description=description, enabled=enabled)
    click.echo(render(lctx.client.ids.add_user_rule(obj), lctx.output_format))


@rule.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def rule_del(ctx: click.Context, uuid: str) -> None:
    """Delete a user rule."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.del_user_rule(uuid), lctx.output_format))


@rule.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def rule_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a user rule."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.toggle_user_rule(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Rulesets
# ===========================================================================


@ids.command("rulesets")
@click.pass_context
@handle_api_errors
def rulesets(ctx: click.Context) -> None:
    """List available IDS rulesets."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.list_rulesets(), lctx.output_format))


@ids.command("update-rules")
@click.pass_context
@handle_api_errors
def update_rules(ctx: click.Context) -> None:
    """Download and update IDS rules from configured sources."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.update_rules(), lctx.output_format))


# ===========================================================================
# Alerts
# ===========================================================================


@ids.command("alerts")
@click.pass_context
@handle_api_errors
def alerts(ctx: click.Context) -> None:
    """Show recent IDS alert log entries."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.get_alert_logs(), lctx.output_format))


# ===========================================================================
# Service control
# ===========================================================================


@ids.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show IDS service status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.status(), lctx.output_format))


@ids.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply IDS configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.reconfigure(), lctx.output_format))


@ids.command("start")
@click.pass_context
@handle_api_errors
def start(ctx: click.Context) -> None:
    """Start the IDS service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.start(), lctx.output_format))


@ids.command("stop")
@click.pass_context
@handle_api_errors
def stop(ctx: click.Context) -> None:
    """Stop the IDS service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.stop(), lctx.output_format))


@ids.command("restart")
@click.pass_context
@handle_api_errors
def restart(ctx: click.Context) -> None:
    """Restart the IDS service."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.ids.restart(), lctx.output_format))
