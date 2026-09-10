from repo_size_analyzer.formatter import format_size

def test_format_size_bytes() -> None:
    """Test formatting values smaller than one kilobyte."""
    assert format_size(512) == "512.00 B"