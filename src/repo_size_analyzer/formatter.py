def format_size(size_bytes: int) -> str:
    """Convert bytes into a human-readable format."""

    size = float(size_bytes)

    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024