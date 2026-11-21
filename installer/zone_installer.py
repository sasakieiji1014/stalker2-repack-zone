"""CLI entry for installing stalker2-repack-zone."""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from core.services.install_service import InstallService
from zone_host.host import ZoneContext, ZoneHost
from zone_host.registry import DEFAULT_REGISTRY

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="zone-installer")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--target", type=Path, required=True)
    p.add_argument("--no-plugins", action="store_true")
    args = p.parse_args(argv)

    svc = InstallService(args.source, args.target)
    svc.stage()

    if not args.no_plugins:
        ctx = ZoneContext(repack_root=args.target, game_version="1.3.1")
        host = ZoneHost(ctx)
        for rec in DEFAULT_REGISTRY:
            host.register(rec)
        loaded = host.load_all()
        logging.info("loaded %d zone plugins", loaded)
        host.unload_all()
    return 0


if __name__ == "__main__":
    sys.exit(main())