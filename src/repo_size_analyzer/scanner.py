from pathlib import Path
from time import perf_counter
from repo_size_analyzer.config import IGNORED_FOLDERS
from repo_size_analyzer.models import DirectoryInfo, FileInfo, RepositoryStats

def scan_repository(repo_path: Path) -> RepositoryStats: