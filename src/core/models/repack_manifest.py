from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RepackFile:
    rel_path: str
    sha256: str
    size: int


@dataclass
class RepackManifest:
    version: str
    game_build: str
    files: list[RepackFile] = field(default_factory=list)

    def as_map(self) -> dict[str, str]:
        return {f.rel_path: f.sha256 for f in self.files}