import os
import shutil
from typing import List, Optional

def remove_temporary_files(directory: str, extensions: List[str]) -> int:
    """Removes files with specific extensions from the given directory."""
    count = 0
    if not os.path.exists(directory):
        return count

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    count += 1
                except OSError:
                    continue
    return count

def clear_directory_contents(directory: str) -> None:
    """Deletes all contents of a directory without removing the root."""
    if not os.path.exists(directory):
        return

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        except OSError:
            continue

def ensure_directory_exists(path: str) -> None:
    """Creates a directory path if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)