from config import REPO_PATH, TOP_FILES, TOP_FOLDERS
from scanner import scan_repository
from reports import (
    print_largest_files,
    print_largest_folders,
    print_summary,
)

def main() -> None:

    if not REPO_PATH.exists():
        print(f"Repository not found: {REPO_PATH}")


if __name__ == "__main__":
    main()