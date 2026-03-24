from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.models.base import SearchRequest


@click.group()
def system() -> None:
    """System control: services, tunables, backups, reboot."""


# ===========================================================================
# System status / control
# ===========================================================================


@system.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show system status messages."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.system_status(), lctx.output_format))


@system.command("reboot")
@click.option("--yes", is_flag=True, required=True, help="Confirm reboot.")
@click.pass_context
@handle_api_errors
def reboot(ctx: click.Context, yes: bool) -> None:
    """Reboot the system. Requires --yes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.reboot(), lctx.output_format))


@system.command("halt")
@click.option("--yes", is_flag=True, required=True, help="Confirm halt.")
@click.pass_context
@handle_api_errors
def halt(ctx: click.Context, yes: bool) -> None:
    """Halt the system. Requires --yes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.halt(), lctx.output_format))


# ===========================================================================
# Services
# ===========================================================================


@system.group("service")
def service() -> None:
    """Manage system services."""


@service.command("list")
@click.pass_context
@handle_api_errors
def service_list(ctx: click.Context) -> None:
    """List all services and their status."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.search_services(), lctx.output_format))


@service.command("start")
@click.argument("name")
@click.option("--id", "service_id", default="", help="Optional service instance ID.")
@click.pass_context
@handle_api_errors
def service_start(ctx: click.Context, name: str, service_id: str) -> None:
    """Start a service by name."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.start_service(name, service_id), lctx.output_format))


@service.command("stop")
@click.argument("name")
@click.option("--id", "service_id", default="")
@click.pass_context
@handle_api_errors
def service_stop(ctx: click.Context, name: str, service_id: str) -> None:
    """Stop a service by name."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.stop_service(name, service_id), lctx.output_format))


@service.command("restart")
@click.argument("name")
@click.option("--id", "service_id", default="")
@click.pass_context
@handle_api_errors
def service_restart(ctx: click.Context, name: str, service_id: str) -> None:
    """Restart a service by name."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.restart_service(name, service_id), lctx.output_format))


# ===========================================================================
# Tunables
# ===========================================================================


@system.group("tunable")
def tunable() -> None:
    """Manage sysctl tunables."""


@tunable.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def tunable_list(ctx: click.Context, search: str) -> None:
    """List tunables."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.search_tunables(SearchRequest(searchPhrase=search)), lctx.output_format))


@tunable.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def tunable_get(ctx: click.Context, uuid: str) -> None:
    """Get a tunable by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.get_tunable(uuid), lctx.output_format))


@tunable.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def tunable_del(ctx: click.Context, uuid: str) -> None:
    """Delete a tunable override."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.del_tunable(uuid), lctx.output_format))


@tunable.command("reconfigure")
@click.pass_context
@handle_api_errors
def tunable_reconfigure(ctx: click.Context) -> None:
    """Apply tunable changes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.reconfigure_tunables(), lctx.output_format))


# ===========================================================================
# Backups
# ===========================================================================


@system.group("backup")
def backup() -> None:
    """Manage configuration backups."""


@backup.command("list")
@click.argument("host")
@click.pass_context
@handle_api_errors
def backup_list(ctx: click.Context, host: str) -> None:
    """List backups for a host."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.list_backups(host), lctx.output_format))


@backup.command("revert")
@click.argument("backup")
@click.pass_context
@handle_api_errors
def backup_revert(ctx: click.Context, backup: str) -> None:
    """Revert to a backup."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.revert_backup(backup), lctx.output_format))


@backup.command("delete")
@click.argument("backup")
@click.pass_context
@handle_api_errors
def backup_delete(ctx: click.Context, backup: str) -> None:
    """Delete a backup."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.core.delete_backup(backup), lctx.output_format))
