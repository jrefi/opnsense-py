from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class Gateway(OPNsenseModel):
    """A network gateway definition (routing/gateway)."""

    disabled: str | None = None
    name: str | None = None
    descr: str | None = None
    interface: str | None = None
    ipprotocol: str | None = None
    gateway: str | None = None
    defaultgw: str | None = None
    fargw: str | None = None
    monitor_disable: str | None = None
    monitor_noroute: str | None = None
    monitor: str | None = None
    force_down: str | None = None
    priority: int | None = None
    weight: int | None = None
    latencylow: int | None = None
    latencyhigh: int | None = None
    losslow: int | None = None
    losshigh: int | None = None
    interval: int | None = None
    time_period: int | None = None
    loss_interval: int | None = None
    data_length: int | None = None
