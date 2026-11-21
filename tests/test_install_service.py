from pathlib import Path

from core.services.install_service import InstallService


def test_stage_copies_files(tmp_path: Path) -> None:
    src = tmp_path / "src"
    src.mkdir()
    (src / "a.pak").write_bytes(b"PAK")
    dst = tmp_path / "dst"
    svc = InstallService(src, dst)
    assert svc.stage() == 1
    assert (dst / "a.pak").is_file()