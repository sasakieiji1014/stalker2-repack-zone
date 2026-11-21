# Contributing to stalker2-repack-zone

Thanks for helping maintain the S.T.A.L.K.E.R. 2: Heart of Chornobyl repack tooling
and its plugin ecosystem.

## Layout
- `src/zone_host/` — core plugin host, registry, contracts
- `src/zone_ext/` — extension modules (anomaly detector, artifact tracker, …)
- `src/core/` — services and models for install/patch pipeline
- `src/infrastructure/` — pak reader and filesystem guards
- `installer/` — CLI entry point
- `scripts/` — dev helpers (manifest generation, verification)

## Adding a plugin
1. Drop a module in `src/zone_ext/` exposing `name`, `api`, and a `PLUGIN` object.
2. Implement `on_load(ctx)` / `on_unload()`.
3. Register it in `src/zone_host/registry.py`.
4. Add a test under `tests/`.

## Style
- Python 3.11+, `from __future__ import annotations`, black + ruff.
- No hidden network calls in plugins.