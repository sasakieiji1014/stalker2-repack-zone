# Zone Plugin API (v3)

A plugin module exposes:

```python
name = "my_plugin"
api = 3
PLUGIN = MyPlugin()
```

`on_load(ctx)` receives a `ZoneContext` with `repack_root`, `game_version`,
and `flags`. `on_unload()` must release handles.

Plugins must stay offline and confined to `ctx.repack_root`.