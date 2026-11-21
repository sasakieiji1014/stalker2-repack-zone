"""Minimal UE pak file reader used to inspect repack archives."""
from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path

PAK_MAGIC = 0x5A6F12E1


@dataclass
class PakEntry:
    path: str
    offset: int
    size: int


class PakReader:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._fh = path.open("rb")

    def read_header(self) -> tuple[int, int]:
        self._fh.seek(-44, 2)
        magic, version, _index_off, _index_size = struct.unpack("<IIqq", self._fh.read(24))
        if magic != PAK_MAGIC:
            raise ValueError(f"not a pak file: {self.path}")
        return magic, version

    def close(self) -> None:
        self._fh.close()