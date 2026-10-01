from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileInfo:
    path: Path
    size: int

@dataclass
class RepositoryStats:
    files: list[FileInfo]
    folder_sizes: dict[Path, int]
    total_size: int
    file_count: int