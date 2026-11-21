from pathlib import Path

from zone_host.host import PluginRecord, ZoneContext, ZoneHost


def test_host_loads_and_unloads(tmp_path: Path) -> None:
    ctx = ZoneContext(repack_root=tmp_path, game_version="1.3.1")
    host = ZoneHost(ctx)
    host.register(PluginRecord(name="repack_verifier", api=3, module="zone_ext.repack_verifier"))
    assert host.load_all() == 1
    host.unload_all()