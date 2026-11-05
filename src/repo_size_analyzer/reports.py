from models import RepositoryStats
from formatter import format_size

def print_summary(stats: RepositoryStats) -> None:

    average_size = (
        stats.total_size / stats.file_count
        if stats.file_count
        else 0
    )

    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)

    print(f"Files analyzed      : {stats.file_count:,}")
    print(f"Directories analyzed: {len(stats.folder_sizes):,}")
    print(f"Repository size     : {format_size(stats.total_size)}")
    print(f"Average file size   : {format_size(int(average_size))}")
    print(f"Elapsed time        : {stats.elapsed_seconds:.2f} seconds")

def print_largest_files(
    stats: RepositoryStats,
    limit: int,
) -> None:        

    largest_files = sorted(
        stats.files,
        key=lambda file: file.size,
        reverse=True,
    )

    print()
    print("=" * 100)
    print(f"TOP {limit} LARGEST FILES")
    print("=" * 100)

    for file_info in largest_files[:limit]:
        print(