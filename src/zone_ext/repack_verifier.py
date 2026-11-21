"""Verifies repack integrity against the shipped Chornobyl bundle manifest."""
from __future__ import annotations

import json
from pathlib import Path

from zone_host.host import ZoneContext

name = "repack_verifier"
api = 3


class _RepackVerifier:
    name = "repack_verifier"
    api = 3

    def on_load(self, ctx: ZoneContext) -> None:
        self.ctx = ctx

    def on_unload(self) -> None:
        self.ctx = None

    def load_manifest(self) -> dict[str, str]:
        mf = self.ctx.repack_root / "manifest.json"
        if not mf.is_file():
            return {}
        return json.loads(mf.read_text(encoding="utf-8")).get("files", {})


PLUGIN = _RepackVerifier()