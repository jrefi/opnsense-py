from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render


@click.group()
def firmware() -> None:
    """Manage firmware, updates, and packages."""


# ===========================================================================
# Status / info
# ===========================================================================


@firmware.command("status")
@click.pass_context
@handle_api_errors
def status(ctx: click.Context) -> None:
    """Show current firmware status and available updates."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.status(), lctx.output_format))


@firmware.command("info")
@click.pass_context
@handle_api_errors
def info(ctx: click.Context) -> None:
    """Show detailed firmware information."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.info(), lctx.output_format))


@firmware.command("running")
@click.pass_context
@handle_api_errors
def running(ctx: click.Context) -> None:
    """Check if a firmware operation is in progress."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.running(), lctx.output_format))


@firmware.command("connection")
@click.pass_context
@handle_api_errors
def connection(ctx: click.Context) -> None:
    """Test connectivity to the firmware mirror."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.connection(), lctx.output_format))


# ===========================================================================
# Operations (fire-and-observe)
# ===========================================================================


@firmware.command("check")
@click.pass_context
@handle_api_errors
def check(ctx: click.Context) -> None:
    """Check for available firmware updates."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.check(), lctx.output_format))


@firmware.command("update")
@click.pass_context
@handle_api_errors
def update(ctx: click.Context) -> None:
    """Trigger a firmware update. Poll 'running' to track completion."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.update(), lctx.output_format))


@firmware.command("upgrade")
@click.pass_context
@handle_api_errors
def upgrade(ctx: click.Context) -> None:
    """Trigger a major firmware upgrade. Poll 'running' to track completion."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.upgrade(), lctx.output_format))


@firmware.command("health")
@click.pass_context
@handle_api_errors
def health(ctx: click.Context) -> None:
    """Run a firmware health check."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.health(), lctx.output_format))


@firmware.command("audit")
@click.pass_context
@handle_api_errors
def audit(ctx: click.Context) -> None:
    """Run a firmware security audit."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.audit(), lctx.output_format))


@firmware.command("changelog")
@click.argument("version")
@click.pass_context
@handle_api_errors
def changelog(ctx: click.Context, version: str) -> None:
    """Show the changelog for a specific firmware version."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.changelog(version), lctx.output_format))


# ===========================================================================
# System power (requires explicit confirmation)
# ===========================================================================


@firmware.command("reboot")
@click.option("--yes", is_flag=True, required=True, help="Confirm reboot.")
@click.pass_context
@handle_api_errors
def reboot(ctx: click.Context, yes: bool) -> None:
    """Reboot the system. Requires --yes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.reboot(), lctx.output_format))


@firmware.command("poweroff")
@click.option("--yes", is_flag=True, required=True, help="Confirm power off.")
@click.pass_context
@handle_api_errors
def poweroff(ctx: click.Context, yes: bool) -> None:
    """Power off the system. Requires --yes."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.poweroff(), lctx.output_format))


# ===========================================================================
# Package management
# ===========================================================================


@firmware.group("package")
def package() -> None:
    """Manage OPNsense packages and plugins."""


@package.command("details")
@click.argument("name")
@click.pass_context
@handle_api_errors
def package_details(ctx: click.Context, name: str) -> None:
    """Show details for a package."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.package_details(name), lctx.output_format))


@package.command("install")
@click.argument("name")
@click.pass_context
@handle_api_errors
def package_install(ctx: click.Context, name: str) -> None:
    """Install a package. Poll 'firmware running' to track progress."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.install_package(name), lctx.output_format))


@package.command("remove")
@click.argument("name")
@click.pass_context
@handle_api_errors
def package_remove(ctx: click.Context, name: str) -> None:
    """Remove a package."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.remove_package(name), lctx.output_format))


@package.command("reinstall")
@click.argument("name")
@click.pass_context
@handle_api_errors
def package_reinstall(ctx: click.Context, name: str) -> None:
    """Reinstall a package."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.reinstall_package(name), lctx.output_format))


@package.command("lock")
@click.argument("name")
@click.pass_context
@handle_api_errors
def package_lock(ctx: click.Context, name: str) -> None:
    """Lock a package at its current version."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.lock_package(name), lctx.output_format))


@package.command("unlock")
@click.argument("name")
@click.pass_context
@handle_api_errors
def package_unlock(ctx: click.Context, name: str) -> None:
    """Unlock a package so it can be upgraded."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.firmware.unlock_package(name), lctx.output_format))
