"""Applies community patches to a staged S.T.A.L.K.E.R. 2 repack."""
from __future__ import annotations

from pathlib import Path


class PatchStep:
    def __init__(self, name: str, kind: str, payload: bytes) -> None:
        self.name = name
        self.kind = kind  # "pak" | "ini" | "script"
        self.payload = payload


class PatchPipeline:
    def __init__(self, root: Path) -> None:
        self.root = root
        self._steps: list[PatchStep] = []

    def add(self, step: PatchStep) -> None:
        self._steps.append(step)

    def run(self) -> list[str]:
        applied: list[str] = []
        for step in self._steps:
            out = self.root / "~mods" / f"{step.name}.{step.kind}"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(step.payload)
            applied.append(step.name)
        return applied