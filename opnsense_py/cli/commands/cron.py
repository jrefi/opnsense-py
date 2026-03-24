from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.cli.utils import build_model
from opnsense_py.models.cron import CronJob


@click.group()
def cron() -> None:
    """Manage cron jobs."""


# ---------------------------------------------------------------------------
# list-jobs
# ---------------------------------------------------------------------------


@cron.command("list-jobs")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def list_jobs(ctx: click.Context, search: str) -> None:
    """List all cron jobs."""
    lctx = get_ctx(ctx)
    from opnsense_py.models.base import SearchRequest

    result = lctx.client.cron.search_jobs(SearchRequest(searchPhrase=search))
    click.echo(render(result, lctx.output_format))


# ---------------------------------------------------------------------------
# get-job
# ---------------------------------------------------------------------------


@cron.command("get-job")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def get_job(ctx: click.Context, uuid: str) -> None:
    """Get a cron job by UUID."""
    lctx = get_ctx(ctx)
    result = lctx.client.cron.get_job(uuid)
    click.echo(render(result, lctx.output_format))


# ---------------------------------------------------------------------------
# add-job
# ---------------------------------------------------------------------------


@cron.command("add-job")
@click.option("--minutes", default=None)
@click.option("--hours", default=None)
@click.option("--days", default=None)
@click.option("--months", default=None)
@click.option("--weekdays", default=None)
@click.option("--who", default=None)
@click.option("--command", default=None)
@click.option("--parameters", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None, help='"1" to enable, "0" to disable.')
@click.option(
    "--from-json",
    "from_json",
    default=None,
    metavar="FILE|-",
    help="Read job fields from JSON (use - for stdin).",
)
@click.pass_context
@handle_api_errors
def add_job(
    ctx: click.Context,
    minutes: str | None,
    hours: str | None,
    days: str | None,
    months: str | None,
    weekdays: str | None,
    who: str | None,
    command: str | None,
    parameters: str | None,
    description: str | None,
    enabled: str | None,
    from_json: str | None,
) -> None:
    """Add a new cron job."""
    lctx = get_ctx(ctx)
    job = build_model(CronJob, from_json,
        minutes=minutes,
        hours=hours,
        days=days,
        months=months,
        weekdays=weekdays,
        who=who,
        command=command,
        parameters=parameters,
        description=description,
        enabled=enabled,
    )
    result = lctx.client.cron.add_job(job)
    click.echo(render(result, lctx.output_format))


# ---------------------------------------------------------------------------
# set-job
# ---------------------------------------------------------------------------


@cron.command("set-job")
@click.argument("uuid")
@click.option("--minutes", default=None)
@click.option("--hours", default=None)
@click.option("--days", default=None)
@click.option("--months", default=None)
@click.option("--weekdays", default=None)
@click.option("--who", default=None)
@click.option("--command", default=None)
@click.option("--parameters", default=None)
@click.option("--description", default=None)
@click.option("--enabled", default=None, help='"1" to enable, "0" to disable.')
@click.option(
    "--from-json",
    "from_json",
    default=None,
    metavar="FILE|-",
    help="Read job fields from JSON (use - for stdin).",
)
@click.pass_context
@handle_api_errors
def set_job(
    ctx: click.Context,
    uuid: str,
    minutes: str | None,
    hours: str | None,
    days: str | None,
    months: str | None,
    weekdays: str | None,
    who: str | None,
    command: str | None,
    parameters: str | None,
    description: str | None,
    enabled: str | None,
    from_json: str | None,
) -> None:
    """Update an existing cron job."""
    lctx = get_ctx(ctx)
    job = build_model(CronJob, from_json,
        minutes=minutes,
        hours=hours,
        days=days,
        months=months,
        weekdays=weekdays,
        who=who,
        command=command,
        parameters=parameters,
        description=description,
        enabled=enabled,
    )
    result = lctx.client.cron.set_job(uuid, job)
    click.echo(render(result, lctx.output_format))


# ---------------------------------------------------------------------------
# del-job
# ---------------------------------------------------------------------------


@cron.command("del-job")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def del_job(ctx: click.Context, uuid: str) -> None:
    """Delete a cron job."""
    lctx = get_ctx(ctx)
    result = lctx.client.cron.del_job(uuid)
    click.echo(render(result, lctx.output_format))


# ---------------------------------------------------------------------------
# toggle-job
# ---------------------------------------------------------------------------


@cron.command("toggle-job")
@click.argument("uuid")
@click.option("--enable/--disable", default=None, help="Set enabled state explicitly.")
@click.pass_context
@handle_api_errors
def toggle_job(ctx: click.Context, uuid: str, enable: bool | None) -> None:
    """Toggle a cron job on or off."""
    lctx = get_ctx(ctx)
    result = lctx.client.cron.toggle_job(uuid, enabled=enable)
    click.echo(render(result, lctx.output_format))


# ---------------------------------------------------------------------------
# reconfigure
# ---------------------------------------------------------------------------


@cron.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply cron configuration changes."""
    lctx = get_ctx(ctx)
    result = lctx.client.cron.reconfigure()
    click.echo(render(result, lctx.output_format))


