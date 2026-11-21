"""Core plugin host: loads extension modules from the zone plugin registry."""
from __future__ import annotations

import importlib
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

log = logging.getLogger("zone.host")


class ZonePlugin(Protocol):
    name: str
    api: int

    def on_load(self, ctx: "ZoneContext") -> None: ...
    def on_unload(self) -> None: ...


@dataclass
class ZoneContext:
    repack_root: Path
    game_version: str
    flags: dict[str, bool] = field(default_factory=dict)


@dataclass
class PluginRecord:
    name: str
    api: int
    module: str
    enabled: bool = True


class ZoneHost:
    def __init__(self, context: ZoneContext) -> None:
        self._ctx = context
        self._loaded: dict[str, ZonePlugin] = {}
        self._records: list[PluginRecord] = []

    def register(self, record: PluginRecord) -> None:
        if record.api != __import__("zone_host").__zone_api__:
            log.warning("plugin %s targets api %s, host is %s", record.name, record.api, 3)
        self._records.append(record)

    def load_all(self) -> int:
        count = 0
        for rec in self._records:
            if not rec.enabled:
                continue
            try:
                mod = importlib.import_module(rec.module)
                plugin = getattr(mod, "PLUGIN")
                plugin.on_load(self._ctx)
                self._loaded[rec.name] = plugin
                count += 1
            except Exception as exc:  # noqa: BLE001
                log.error("failed loading %s: %s", rec.name, exc)
        return count

    def unload_all(self) -> None:
        for name, plugin in list(self._loaded.items()):
            try:
                plugin.on_unload()
            finally:
                del self._loaded[name]