from pathlib import Path
from time import perf_counter

from config import IGNORED_FOLDERS
from models import FileInfo, RepositoryStats

def scan_repository(path: Path) -> bool:
    """Return True if the path contains an ignored folder."""
    return any(part in IGNORED_FOLDERS for part in path.parts)

def scan_repository(repo_path: Path) -> RepositoryStats:
    """Scan repository and collect file and directory statistics."""

    files: list[FileInfo] = []
    folder_sizes: dict[Path, int] = {}

    total_size = 0
    file_count = 0

    start = perf_counter()

    for file_path in repo_path.rglob("*"):