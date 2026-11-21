from __future__ import annotations

import os
from pathlib import Path


def assert_inside(root: Path, candidate: Path) -> Path:
    root = root.resolve()
    candidate = candidate.resolve()
    if os.path.commonpath([str(root), str(candidate)]) != str(root):
        raise PermissionError(f"path escapes zone root: {candidate}")
    return candidate