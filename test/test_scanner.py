from pathlib import Path
from repo_size_analyzer.scanner import scan_repository

def test_scan_repository_counts_files(tmp_path: Path) -> None: