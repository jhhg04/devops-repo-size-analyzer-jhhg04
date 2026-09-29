from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileInfo:
    path: Path
    size: int

@dataclass
    