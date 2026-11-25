import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Если запуск из Canfly/voicer-ci: проект в соседнем каталоге (../voicer)
for _candidate in (Path("voicer"), Path(__file__).resolve().parents[2] / "voicer"):
    if _candidate.is_dir() and (_candidate / "whisper_service.py").exists():
        sys.path.insert(0, str(_candidate))


@pytest.fixture
def db_path(tmp_path):
    return str(tmp_path / "test.db")


@pytest.fixture
def db(db_path):
    from database import Database

    return Database(db_path)
