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
        return

    stats = scan_repository(REPO_PATH)

    print_summary(stats)

    print_largest_files(
        stats,
        TOP_FILES,
    )

    print_largest_folders(
        stats,
        TOP_FOLDERS,
    )

if __name__ == "__main__":
    main()
