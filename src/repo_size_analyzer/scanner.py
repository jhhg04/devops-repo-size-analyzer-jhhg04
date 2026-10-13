from pathlib import Path
from time import perf_counter

from config import IGNORED_FOLDERS
from models import FileInfo

def scan_repository(repo_path: Path) -> RepositoryStats: