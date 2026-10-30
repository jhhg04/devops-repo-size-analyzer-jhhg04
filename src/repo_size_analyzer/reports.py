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