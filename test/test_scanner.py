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

def test_scan_repository_ignores_configured_directories(tmp_path: Path) -> None:
    """Test that ignored directories are excluded from the scan."""
    included_file = tmp_path / "included.txt"
    included_file.write_text("included", encoding="utf-8")

    git_dir = tmp_path / ".git"
    git_dir.mkdir()

    ignored_file = git_dir / "ignored.txt"
    ignored_file.write_text("ignored", encoding="utf-8")

    stats = scan_repository(tmp_path)

    assert stats.total_files == 1
    assert stats.total_size == len("included")

def test_scan_repository_detects_nested_files(tmp_path: Path) -> None:
    """Test that files inside nested directories are detected."""
    nested_dir = tmp_path / "src" / "app"
    nested_dir.mkdir(parents=True)

    nested_file = nested_dir / "main.py"
    nested_file.write_text("print('hello')", encoding="utf-8")

    stats = scan_repository(tmp_path)
    assert stats.total_files == 1
    assert stats.total_size == len("print('hello')")