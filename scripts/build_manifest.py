"""Generate manifest.json for a staged repack directory."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(root: Path) -> None:
    files = []
    for f in sorted(root.rglob("*")):
        if f.is_file() and f.name != "manifest.json":
            files.append({"rel_path": str(f.relative_to(root)), "sha256": digest(f), "size": f.stat().st_size})
    out = root / "manifest.json"
    out.write_text(json.dumps({"version": "0.9.4", "game_build": "1.3.1", "files": files}, indent=2))
    print(f"wrote {out} ({len(files)} entries)")


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "."))