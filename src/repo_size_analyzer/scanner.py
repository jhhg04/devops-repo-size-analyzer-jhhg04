from pathlib import Path
from time import perf_counter

from config import IGNORED_FOLDERS
from models import FileInfo, RepositoryStats

def scan_repository(path: Path) -> bool:
    """Return True if the path contains an ignored folder."""
    return any(part in IGNORED_FOLDERS for part in path.parts)

def scan_repository(repo_path: Path) -> RepositoryStats: