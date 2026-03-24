from __future__ import annotations

import click

from opnsense_py.cli.main import get_ctx, handle_api_errors
from opnsense_py.cli.output import render
from opnsense_py.models.base import SearchRequest


@click.group()
def trust() -> None:
    """Manage certificate authorities, certificates, and CRLs."""


# ===========================================================================
# Certificate Authorities
# ===========================================================================


@trust.group("ca")
def ca() -> None:
    """Manage certificate authorities."""


@ca.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def ca_list(ctx: click.Context, search: str) -> None:
    """List certificate authorities."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.search_cas(SearchRequest(searchPhrase=search)), lctx.output_format))


@ca.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def ca_get(ctx: click.Context, uuid: str) -> None:
    """Get a CA by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.get_ca(uuid), lctx.output_format))


@ca.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def ca_del(ctx: click.Context, uuid: str) -> None:
    """Delete a CA."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.del_ca(uuid), lctx.output_format))


@ca.command("dump")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def ca_dump(ctx: click.Context, uuid: str) -> None:
    """Dump the raw PEM of a CA."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.raw_dump_ca(uuid), lctx.output_format))


# ===========================================================================
# Certificates
# ===========================================================================


@trust.group("cert")
def cert() -> None:
    """Manage certificates."""


@cert.command("list")
@click.option("--search", default="", help="Filter by search phrase.")
@click.pass_context
@handle_api_errors
def cert_list(ctx: click.Context, search: str) -> None:
    """List certificates."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.search_certs(SearchRequest(searchPhrase=search)), lctx.output_format))


@cert.command("get")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def cert_get(ctx: click.Context, uuid: str) -> None:
    """Get a certificate by UUID."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.get_cert(uuid), lctx.output_format))


@cert.command("del")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def cert_del(ctx: click.Context, uuid: str) -> None:
    """Delete a certificate."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.del_cert(uuid), lctx.output_format))


@cert.command("dump")
@click.argument("uuid")
@click.pass_context
@handle_api_errors
def cert_dump(ctx: click.Context, uuid: str) -> None:
    """Dump the raw PEM of a certificate."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.raw_dump_cert(uuid), lctx.output_format))


# ===========================================================================
# CRLs
# ===========================================================================


@trust.group("crl")
def crl() -> None:
    """Manage certificate revocation lists."""


@crl.command("list")
@click.pass_context
@handle_api_errors
def crl_list(ctx: click.Context) -> None:
    """List CRLs."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.search_crls(), lctx.output_format))


@crl.command("get")
@click.argument("caref")
@click.pass_context
@handle_api_errors
def crl_get(ctx: click.Context, caref: str) -> None:
    """Get CRL for a CA (by CA ref)."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.get_crl(caref), lctx.output_format))


@crl.command("del")
@click.argument("caref")
@click.pass_context
@handle_api_errors
def crl_del(ctx: click.Context, caref: str) -> None:
    """Delete the CRL for a CA."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.del_crl(caref), lctx.output_format))


@crl.command("dump")
@click.argument("caref")
@click.pass_context
@handle_api_errors
def crl_dump(ctx: click.Context, caref: str) -> None:
    """Dump the raw PEM of a CRL."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.raw_dump_crl(caref), lctx.output_format))


# ===========================================================================
# Reconfigure
# ===========================================================================


@trust.command("reconfigure")
@click.pass_context
@handle_api_errors
def reconfigure(ctx: click.Context) -> None:
    """Apply trust store configuration."""
    lctx = get_ctx(ctx)
    click.echo(render(lctx.client.trust.reconfigure(), lctx.output_format))
