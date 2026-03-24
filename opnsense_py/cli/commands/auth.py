from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.models.base import SearchRequest


@click.group()
def auth() -> None:
    """Manage users, groups, and API keys."""


# ===========================================================================
# Users
# ===========================================================================


@auth.group("user")
def user() -> None:
    """Manage local user accounts."""


@user.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def user_list(ctx: click.Context, search: str) -> None:
    """List users."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.search_users(SearchRequest(searchPhrase=search)), lctx.output_format))


@user.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def user_get(ctx: click.Context, uuid: str) -> None:
    """Get a user by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.get_user(uuid), lctx.output_format))


@user.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def user_del(ctx: click.Context, uuid: str) -> None:
    """Delete a user."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.del_user(uuid), lctx.output_format))


@user.command("api-keys")
@click.pass_context
@handle_api_errors
def api_keys(ctx: click.Context) -> None:
    """List all API keys."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.search_api_keys(), lctx.output_format))


@user.command("add-api-key")
@click.argument("username")
@click.pass_context
@handle_api_errors
def add_api_key(ctx: click.Context, username: str) -> None:
    """Generate a new API key for a user."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.add_api_key(username), lctx.output_format))


@user.command("del-api-key")
@click.argument("key_id")
@click.pass_context
@handle_api_errors
def del_api_key(ctx: click.Context, key_id: str) -> None:
    """Delete an API key by ID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.del_api_key(key_id), lctx.output_format))


# ===========================================================================
# Groups
# ===========================================================================


@auth.group("group")
def group() -> None:
    """Manage local user groups."""


@group.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def group_list(ctx: click.Context, search: str) -> None:
    """List groups."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.search_groups(SearchRequest(searchPhrase=search)), lctx.output_format))


@group.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def group_get(ctx: click.Context, uuid: str) -> None:
    """Get a group by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.get_group(uuid), lctx.output_format))


@group.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def group_del(ctx: click.Context, uuid: str) -> None:
    """Delete a group."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.auth.del_group(uuid), lctx.output_format))
