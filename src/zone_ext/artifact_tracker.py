"""Tracks artifact spawn tables from repack pak files."""
from __future__ import annotations

from zone_host.host import ZoneContext

name = "artifact_tracker"
api = 3


class _ArtifactTracker:
    name = "artifact_tracker"
    api = 3

    def on_load(self, ctx: ZoneContext) -> None:
        self.ctx = ctx
        self.tables: dict[str, list[str]] = {}

    def on_unload(self) -> None:
        self.tables.clear()

    def ingest(self, level: str, artifacts: list[str]) -> None:
        self.tables.setdefault(level, []).extend(artifacts)

    def summary(self) -> dict[str, int]:
        return {lvl: len(items) for lvl, items in self.tables.items()}


PLUGIN = _ArtifactTracker()