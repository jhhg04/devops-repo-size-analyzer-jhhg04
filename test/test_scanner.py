from pathlib import Path
from repo_size_analyzer.scanner import scan_repository

def test_scan_repository_counts_files(tmp_path: Path) -> None:
    """Test that the scanner detects files and calculates their sizes."""
    file_one = tmp_path / "file1.txt"
    file_two = tmp_path / "file2.txt"

    file_one.write_text("hello", encoding="utf-8")
    file_two.write_text("hello world", encoding="utf-8")

    stats = scan_repository(tmp_path)

    assert stats.total_files == 2
    assert stats.total_size == 16