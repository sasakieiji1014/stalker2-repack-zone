"""Static plugin registry for the Chornobyl repack zone."""
from __future__ import annotations

from zone_host.host import PluginRecord

DEFAULT_REGISTRY: list[PluginRecord] = [
    PluginRecord(name="anomaly_detector", api=3, module="zone_ext.anomaly_detector"),
    PluginRecord(name="artifact_tracker", api=3, module="zone_ext.artifact_tracker"),
    PluginRecord(name="repack_verifier", api=3, module="zone_ext.repack_verifier"),
    PluginRecord(name="save_migrator", api=3, module="zone_ext.save_migrator", enabled=False),
]


def by_name(name: str) -> PluginRecord | None:
    for rec in DEFAULT_REGISTRY:
        if rec.name == name:
            return rec
    return None