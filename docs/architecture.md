# Architecture

`stalker2-repack-zone` is a plugin host for S.T.A.L.K.E.R. 2: Heart of Chornobyl
repacks.

- **zone_host** — host loop, registry, context, plugin protocol
- **zone_ext** — extension modules that run inside the host
- **core** — install service, patch pipeline, manifest models
- **infrastructure** — pak reader, path guards
- **installer** — CLI (`python -m installer.zone_installer`)
- **scripts** — manifest builder and repack verifier

Plugin API version is `3` (`zone_host.__zone_api__`); mismatches log a warning
but are not fatal, matching prior community tooling behaviour.