from pathlib import Path
from time import perf_counter

from config import IGNORED_FOLDERS
from models import FileInfo, RepositoryStats

def scan_repository(path: Path) -> bool:
    """Return True if the path contains an ignored folder."""
    return any(part in IGNORED_FOLDERS for part in path.parts)

def scan_repository(repo_path: Path) -> RepositoryStats:
    """Scan repository and collect file and directory statistics."""

    files: list[FileInfo] = []
    folder_sizes: dict[Path, int] = {}

    total_size = 0
    file_count = 0

    start = perf_counter()

    for file_path in repo_path.rglob("*"):

        if should_ignore(file_path):
            continue

        if not file_path.is_file():
            continue

        try:
            file_size = file_path.stat().st_size

        except (PermissionError, FileNotFoundError, OSError):
            continue

        files.append(
            FileInfo(
                path=file_path,
                size=file_size,
            )
        )

        total_size += file_size
        file_count += 1

        current_folder = file_path.parent

        while True:
            folder_sizes[current_folder] = (
                folder_sizes.get(current_folder, 0)
                + file_size
            )

            if current_folder == repo_path:
                break

            current_folder = current_folder.parent

    elapsed = perf_counter() - start

    return RepositoryStats(
        files=files,
        folder_sizes=folder_sizes,


        elapsed_seconds=elapsed,
    )    