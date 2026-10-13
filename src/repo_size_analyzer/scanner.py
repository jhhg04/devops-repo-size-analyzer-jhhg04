from pathlib import Path
from time import perf_counter

from config import IGNORED_FOLDERS
from models import FileInfo, RepositoryStats

def scan_repository(path: Path) -> bool:
    """Return True if the path contains an ignored folder."""