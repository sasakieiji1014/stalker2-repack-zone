"""Scans installed repack for anomaly (corrupted/mismatched) asset bundles."""
from __future__ import annotations

import hashlib
from pathlib import Path

from zone_host.host import ZoneContext

name = "anomaly_detector"
api = 3


class _AnomalyPlugin:
    name = "anomaly_detector"
    api = 3

    def on_load(self, ctx: ZoneContext) -> None:
        self.ctx = ctx

    def on_unload(self) -> None:
        self.ctx = None

    def scan(self, manifest: dict[str, str]) -> list[str]:
        bad: list[str] = []
        for rel, expect in manifest.items():
            full = self.ctx.repack_root / rel
            if not full.is_file():
                bad.append(rel)
                continue
            digest = hashlib.sha256(full.read_bytes()).hexdigest()
            if digest != expect:
                bad.append(rel)
        return bad


PLUGIN = _AnomalyPlugin()