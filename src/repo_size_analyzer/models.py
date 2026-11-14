from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileInfo:
    path: Path
    size: int

@dataclass
class RepositoryStats:
    total_files: int
    total_size: int
    files: list[FileInfo]
    folder_sizes: dict[Path, int]
    elapsed_seconds: float