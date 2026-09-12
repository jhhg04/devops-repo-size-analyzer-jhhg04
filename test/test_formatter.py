from repo_size_analyzer.formatter import format_size

def test_format_size_bytes() -> None:
    """Test formatting values smaller than one kilobyte."""
    assert format_size(512) == "512.00 B"

def test_format_size_kilobytes() -> None:
    """Test formatting values in kilobytes."""
    assert format_size(1024) == "1.00 KB" 

def test_format_size_megabytes() -> None:
    """Test formatting values in megabytes."""