from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.base import SearchRequest
from opnsense_py.models.firewall import DNatRule, FilterRule, FirewallAlias, SNatRule


@click.group()
def firewall() -> None:
    """Manage firewall rules, aliases, and NAT."""


# ===========================================================================
# Aliases
# ===========================================================================


@firewall.group()
def alias() -> None:
    """Manage firewall aliases."""


@alias.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def alias_list(ctx: click.Context, search: str) -> None:
    """List firewall aliases."""
    lctx = get_ctx(ctx)
    result = lctx.client.firewall.search_aliases(SearchRequest(searchPhrase=search))
    click.echo(render(result, lctx.output_format))


@alias.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def alias_get(ctx: click.Context, uuid: str) -> None:
    """Get a firewall alias by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.get_alias(uuid), lctx.output_format))


@alias.command("add")
@click.option("--name", default=None)
@click.option("--type", "type_", default=None, metavar="TYPE", help="host, network, port, url, ...")
@click.option("--content", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None, help='"1" or "0".')
@click.option("--proto", default=None)
@click.option("--interface", default=None)
@click.option("--updatefreq", default=None)
@click.option("--categories", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def alias_add(
    ctx: click.Context,
    name: str | None, type_: str | None, content: str | None, description: str | None,
    enabled: str | None, proto: str | None, interface: str | None,
    updatefreq: str | None, categories: str | None, from_json: str | None,
) -> None:
    """Add a firewall alias."""
    lctx = get_ctx(ctx)
    obj = build_model(FirewallAlias, from_json, name=name, type=type_, content=content,
                      description=description, enabled=enabled, proto=proto,
                      interface=interface, updatefreq=updatefreq, categories=categories)
    click.echo(render(lctx.client.firewall.add_alias(obj), lctx.output_format))


@alias.command("set")
@click.argument("uuid")
@click.option("--name", default=None)
@click.option("--type", "type_", default=None, metavar="TYPE")
@click.option("--content", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None)
@click.option("--proto", default=None)
@click.option("--interface", default=None)
@click.option("--updatefreq", default=None)
@click.option("--categories", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def alias_set(
    ctx: click.Context, uuid: str,
    name: str | None, type_: str | None, content: str | None, description: str | None,
    enabled: str | None, proto: str | None, interface: str | None,
    updatefreq: str | None, categories: str | None, from_json: str | None,
) -> None:
    """Update a firewall alias."""
    lctx = get_ctx(ctx)
    obj = build_model(FirewallAlias, from_json, name=name, type=type_, content=content,
                      description=description, enabled=enabled, proto=proto,
                      interface=interface, updatefreq=updatefreq, categories=categories)
    click.echo(render(lctx.client.firewall.set_alias(uuid, obj), lctx.output_format))


@alias.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def alias_del(ctx: click.Context, uuid: str) -> None:
    """Delete a firewall alias."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.del_alias(uuid), lctx.output_format))


@alias.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def alias_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a firewall alias on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.toggle_alias(uuid, enabled=enable), lctx.output_format))


@alias.command("reconfigure")
@click.pass_context
@handle_api_errors
def alias_reconfigure(ctx: click.Context) -> None:
    """Apply alias configuration changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.reconfigure_aliases(), lctx.output_format))


# ===========================================================================
# Filter rules
# ===========================================================================


@firewall.group()
def rule() -> None:
    """Manage firewall filter rules."""


def _rule_opts(f):  # type: ignore[no-untyped-def]
    """Apply all filter rule options to a command."""
    for opt in [
        click.option("--enabled", default=None),
        click.option("--action", default=None, help="pass, block, reject"),
        click.option("--interface", default=None),
        click.option("--direction", default=None, help="in, out"),
        click.option("--protocol", default=None),
        click.option("--source-net", "source_net", default=None),
        click.option("--source-port", "source_port", default=None),
        click.option("--destination-net", "destination_net", default=None),
        click.option("--destination-port", "destination_port", default=None),
        click.option("--gateway", default=None),
        click.option("--description", default=None),
        click.option("--log", default=None),
        click.option("--sequence", default=None),
        click.option("--ipprotocol", default=None, help="inet, inet6"),
        click.option("--quick", default=None),
        click.option("--categories", default=None),
        click.option("--from-json", "from_json", default=None, metavar="FILE|-"),
    ]:
        f = opt(f)
    return f


@rule.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def rule_list(ctx: click.Context, search: str) -> None:
    """List firewall filter rules."""
    lctx = get_ctx(ctx)
    result = lctx.client.firewall.search_filter_rules(SearchRequest(searchPhrase=search))
    click.echo(render(result, lctx.output_format))


@rule.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def rule_get(ctx: click.Context, uuid: str) -> None:
    """Get a firewall rule by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.get_filter_rule(uuid), lctx.output_format))


@rule.command("add")
@_rule_opts
@click.pass_context
@handle_api_errors
def rule_add(ctx: click.Context, from_json: str | None, **fields: str | None) -> None:
    """Add a firewall filter rule."""
    lctx = get_ctx(ctx)
    obj = build_model(FilterRule, from_json, **fields)
    click.echo(render(lctx.client.firewall.add_filter_rule(obj), lctx.output_format))


@rule.command("set")
@click.argument("uuid")
@_rule_opts
@click.pass_context
@handle_api_errors
def rule_set(ctx: click.Context, uuid: str, from_json: str | None, **fields: str | None) -> None:
    """Update a firewall filter rule."""
    lctx = get_ctx(ctx)
    obj = build_model(FilterRule, from_json, **fields)
    click.echo(render(lctx.client.firewall.set_filter_rule(uuid, obj), lctx.output_format))


@rule.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def rule_del(ctx: click.Context, uuid: str) -> None:
    """Delete a firewall filter rule."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.del_filter_rule(uuid), lctx.output_format))


@rule.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def rule_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a firewall filter rule on or off."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.toggle_filter_rule(uuid, enabled=enable), lctx.output_format))


# ===========================================================================
# Destination NAT (port forwards)
# ===========================================================================


@firewall.group()
def dnat() -> None:
    """Manage destination NAT (port forward) rules."""


@dnat.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def dnat_list(ctx: click.Context, search: str) -> None:
    """List DNAT rules."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.search_dnat_rules(SearchRequest(searchPhrase=search)), lctx.output_format))


@dnat.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def dnat_get(ctx: click.Context, uuid: str) -> None:
    """Get a DNAT rule by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.get_dnat_rule(uuid), lctx.output_format))


@dnat.command("add")
@click.option("--interface", default=None)
@click.option("--protocol", default=None)
@click.option("--target", default=None)
@click.option("--local-port", "local_port", default=None)
@click.option("--description", "descr", default=None)
@click.option("--log", default=None)
@click.option("--sequence", default=None)
@click.option("--disabled", default=None)
@click.option("--ipprotocol", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def dnat_add(
    ctx: click.Context, interface: str | None, protocol: str | None, target: str | None,
    local_port: str | None, descr: str | None, log: str | None, sequence: str | None,
    disabled: str | None, ipprotocol: str | None, from_json: str | None,
) -> None:
    """Add a DNAT rule."""
    lctx = get_ctx(ctx)
    obj = build_model(DNatRule, from_json, interface=interface, protocol=protocol,
                      target=target, local_port=local_port, descr=descr, log=log,
                      sequence=sequence, disabled=disabled, ipprotocol=ipprotocol)
    click.echo(render(lctx.client.firewall.add_dnat_rule(obj), lctx.output_format))


@dnat.command("set")
@click.argument("uuid")
@click.option("--interface", default=None)
@click.option("--protocol", default=None)
@click.option("--target", default=None)
@click.option("--local-port", "local_port", default=None)
@click.option("--description", "descr", default=None)
@click.option("--log", default=None)
@click.option("--sequence", default=None)
@click.option("--disabled", default=None)
@click.option("--ipprotocol", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def dnat_set(
    ctx: click.Context, uuid: str, interface: str | None, protocol: str | None, target: str | None,
    local_port: str | None, descr: str | None, log: str | None, sequence: str | None,
    disabled: str | None, ipprotocol: str | None, from_json: str | None,
) -> None:
    """Update a DNAT rule."""
    lctx = get_ctx(ctx)
    obj = build_model(DNatRule, from_json, interface=interface, protocol=protocol,
                      target=target, local_port=local_port, descr=descr, log=log,
                      sequence=sequence, disabled=disabled, ipprotocol=ipprotocol)
    click.echo(render(lctx.client.firewall.set_dnat_rule(uuid, obj), lctx.output_format))


@dnat.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def dnat_del(ctx: click.Context, uuid: str) -> None:
    """Delete a DNAT rule."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.del_dnat_rule(uuid), lctx.output_format))


@dnat.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def dnat_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a DNAT rule. Note: the API uses a 'disabled' flag, so --disable enables it."""
    lctx = get_ctx(ctx)
    # API takes disabled=True to disable, disabled=False to enable
    disabled = (not enable) if enable is not None else None
    click.echo(render(lctx.client.firewall.toggle_dnat_rule(uuid, disabled=disabled), lctx.output_format))


# ===========================================================================
# Source NAT (outbound)
# ===========================================================================


@firewall.group()
def snat() -> None:
    """Manage source NAT (outbound) rules."""


@snat.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def snat_list(ctx: click.Context, search: str) -> None:
    """List SNAT rules."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.search_snat_rules(SearchRequest(searchPhrase=search)), lctx.output_format))


@snat.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def snat_get(ctx: click.Context, uuid: str) -> None:
    """Get a SNAT rule by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.get_snat_rule(uuid), lctx.output_format))


@snat.command("add")
@click.option("--interface", default=None)
@click.option("--protocol", default=None)
@click.option("--source-net", "source_net", default=None)
@click.option("--source-port", "source_port", default=None)
@click.option("--destination-net", "destination_net", default=None)
@click.option("--destination-port", "destination_port", default=None)
@click.option("--target", default=None)
@click.option("--target-port", "target_port", default=None)
@click.option("--description", default=None)
@click.option("--log", default=None)
@click.option("--sequence", default=None)
@click.option("--disabled", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def snat_add(
    ctx: click.Context, interface: str | None, protocol: str | None, source_net: str | None,
    source_port: str | None, destination_net: str | None, destination_port: str | None,
    target: str | None, target_port: str | None, description: str | None, log: str | None,
    sequence: str | None, disabled: str | None, from_json: str | None,
) -> None:
    """Add a SNAT rule."""
    lctx = get_ctx(ctx)
    obj = build_model(SNatRule, from_json, interface=interface, protocol=protocol,
                      source_net=source_net, source_port=source_port,
                      destination_net=destination_net, destination_port=destination_port,
                      target=target, target_port=target_port, description=description,
                      log=log, sequence=sequence, enabled="0" if disabled == "1" else None)
    click.echo(render(lctx.client.firewall.add_snat_rule(obj), lctx.output_format))


@snat.command("set")
@click.argument("uuid")
@click.option("--interface", default=None)
@click.option("--protocol", default=None)
@click.option("--source-net", "source_net", default=None)
@click.option("--source-port", "source_port", default=None)
@click.option("--destination-net", "destination_net", default=None)
@click.option("--destination-port", "destination_port", default=None)
@click.option("--target", default=None)
@click.option("--target-port", "target_port", default=None)
@click.option("--description", default=None)
@click.option("--log", default=None)
@click.option("--sequence", default=None)
@click.option("--from-json", "from_json", default=None, metavar="FILE|-")
@click.pass_context
@handle_api_errors
def snat_set(
    ctx: click.Context, uuid: str, interface: str | None, protocol: str | None,
    source_net: str | None, source_port: str | None, destination_net: str | None,
    destination_port: str | None, target: str | None, target_port: str | None,
    description: str | None, log: str | None, sequence: str | None, from_json: str | None,
) -> None:
    """Update a SNAT rule."""
    lctx = get_ctx(ctx)
    obj = build_model(SNatRule, from_json, interface=interface, protocol=protocol,
                      source_net=source_net, source_port=source_port,
                      destination_net=destination_net, destination_port=destination_port,
                      target=target, target_port=target_port, description=description,
                      log=log, sequence=sequence)
    click.echo(render(lctx.client.firewall.set_snat_rule(uuid, obj), lctx.output_format))


@snat.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def snat_del(ctx: click.Context, uuid: str) -> None:
    """Delete a SNAT rule."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.del_snat_rule(uuid), lctx.output_format))


@snat.command("toggle")
@click.argument("uuid")
@click.option("--enable/--disable", default=None)
@click.pass_context
@handle_api_errors
def snat_toggle(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a SNAT rule on or off."""
    lctx = get_ctx(ctx)
    disabled = (not enable) if enable is not None else None
    click.echo(render(lctx.client.firewall.toggle_snat_rule(uuid, disabled=disabled), lctx.output_format))


# ===========================================================================
# Top-level apply
# ===========================================================================


@firewall.command("apply")
@click.pass_context
@handle_api_errors
def apply(ctx: click.Context) -> None:
    """Apply pending firewall changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firewall.apply(), lctx.output_format))
