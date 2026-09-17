from pathlib import Path
from repo_size_analyzer.scanner import scan_repository

def test_scan_repository_counts_files(tmp_path: Path) -> None:
    """Test that the scanner detects files and calculates their sizes."""