import os
from typing import Any, List, Optional
from pathlib import Path

def ensure_directory(path: str) -> None:
    """Creates a directory if it does not exist."""
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)

def sanitize_filename(filename: str) -> str:
    """Removes problematic characters from strings for filenames."""
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).strip()

def get_environment_variable(key: str, default: Any = None) -> Optional[str]:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default)

def list_files_by_extension(directory: str, extension: str) -> List[str]:
    """Filters directory contents by file extension."""
    path = Path(directory)
    if not path.is_dir():
        return []
    return [f.name for f in path.iterdir() if f.suffix == extension]

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller chunks of defined size."""
    return [data[i:i + size] for i in range(0, len(data), size)]