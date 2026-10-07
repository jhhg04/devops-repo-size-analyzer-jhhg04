from pathlib import Path

# Repository to analyze
REPO_PATH = Path(r"C:\Repos\MyRepository")

# Number of results to display
TOP_FILES = 100
TOP_FOLDERS = 50

# Folders that will be skipped
IGNORED_FOLDERS = {
    ".git",
    ".terraform",
    ".idea",
    ".vs",
    ".vscode",



}