# Repack Layout

```
<repack_root>/
  manifest.json          # verifier reads this
  Stalker2/Content/Paks/ # UE paks from the repack
  ~mods/                 # patch pipeline output
  Binaries/Win64/
```

The `anomaly_detector` hashes each file against `manifest.json`; the
`repack_verifier` reports missing entries.