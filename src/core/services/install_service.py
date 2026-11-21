"""Install service: unpacks the Chornobyl repack into the target zone dir."""
from __future__ import annotations

import logging
import shutil
from pathlib import Path

log = logging.getLogger("zone.install")


class InstallService:
    def __init__(self, source: Path, target: Path) -> None:
        self.source = source
        self.target = target

    def stage(self) -> int:
        self.target.mkdir(parents=True, exist_ok=True)
        count = 0
        for entry in self.source.rglob("*"):
            if entry.is_file():
                dest = self.target / entry.relative_to(self.source)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(entry, dest)
                count += 1
        log.info("staged %d files into %s", count, self.target)
        return count

    def verify_present(self, manifest: dict[str, str]) -> list[str]:
        return [rel for rel in manifest if not (self.target / rel).is_file()]