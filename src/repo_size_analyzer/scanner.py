import os
import time
from pathlib import Path

from config import IGNORED_FOLDERS
from models import FileInfo, RepositoryStats

def should_ignore(directory: Path) -> bool:
    """Check whether a directory should be ignored."""
    return directory.name in IGNORED_FOLDERS

def scan_repository(repo_path: Path) -> RepositoryStats:
    """Scan repository and collect file and directory statistics."""

    repo_path = repo_path.resolve()

    if not repo_path.exists():
        raise FileNotFoundError(
            f"Repository path does not exist: {repo_path}"
        )

    if not repo_path.is_dir():
        raise NotADirectoryError(
            f"Repository path is not a directory: {repo_path}"
        )

    start_time = time.perf_counter()

    files: list[FileInfo] = []
    folder_sizes: dict[Path, int] = {}
    total_size = 0

    for current_dir, dir_names, file_names in os.walk(
        repo_path,
        followlinks=False,
    ):
        current_path = Path(current_dir)

        # Exclude ignored directories before traversal.
        dir_names[:] = [
            name
            for name in dir_names
            if not should_ignore(current_path / name)
        ]    

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
        total_size=total_size,
        file_count=file_count,
        elapsed_seconds=elapsed,
    )    