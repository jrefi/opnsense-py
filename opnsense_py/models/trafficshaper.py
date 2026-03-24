from __future__ import annotations

from opnsense_py.models.base import OPNsenseModel


class ShaperPipe(OPNsenseModel):
    """A traffic shaper pipe (trafficshaper/pipe)."""

    enabled: str | None = None
    bandwidth: int | None = None
    bandwidthMetric: str | None = None
    queue: int | None = None
    mask: str | None = None
    buckets: int | None = None
    scheduler: str | None = None
    codel_enable: str | None = None
    codel_target: int | None = None
    codel_interval: int | None = None
    codel_ecn_enable: str | None = None
    pie_enable: str | None = None
    delay: int | None = None
    description: str | None = None


class ShaperQueue(OPNsenseModel):
    """A traffic shaper queue (trafficshaper/queue)."""

    enabled: str | None = None
    pipe: str | None = None
    weight: int | None = None
    mask: str | None = None
    buckets: int | None = None
    codel_enable: str | None = None
    codel_target: int | None = None
    codel_interval: int | None = None
    codel_ecn_enable: str | None = None
    pie_enable: str | None = None
    description: str | None = None


class ShaperRule(OPNsenseModel):
    """A traffic shaper rule (trafficshaper/rule)."""

    enabled: str | None = None
    sequence: int | None = None
    interface: str | None = None
    interface2: str | None = None
    proto: str | None = None
    iplen: int | None = None
    source: str | None = None
    source_not: str | None = None
    src_port: str | None = None
    destination: str | None = None
    destination_not: str | None = None
    dst_port: str | None = None
    dscp: str | None = None
    direction: str | None = None
    target: str | None = None
    description: str | None = None
