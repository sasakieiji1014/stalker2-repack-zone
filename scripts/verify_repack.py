from __future__ import annotations

import sys
from pathlib import Path

from zone_ext.repack_verifier import PLUGIN as verifier
from zone_host.host import ZoneContext


def main(root: Path) -> int:
    verifier.on_load(ZoneContext(repack_root=root, game_version="1.3.1"))
    manifest = verifier.load_manifest()
    missing = [rel for rel in manifest if not (root / rel).is_file()]
    for m in missing:
        print(f"missing: {m}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else ".")))