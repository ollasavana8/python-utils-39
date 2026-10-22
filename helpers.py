import os
import shutil
from typing import List, Optional

def clean_directory(path: str, extensions: Optional[List[str]] = None) -> int:
    """Removes files with specified extensions from a directory."""
    count = 0
    if not os.path.exists(path):
        return count

    for item in os.listdir(path):
        file_path = os.path.join(path, item)
        if os.path.isfile(file_path):
            if extensions is None or any(item.endswith(ext) for ext in extensions):
                os.remove(file_path)
                count += 1
    return count

def reorganize_files(source: str, target: str, extension: str) -> int:
    """Moves files of a specific type to a target directory."""
    if not os.path.exists(target):
        os.makedirs(target)

    moved = 0
    for item in os.listdir(source):
        if item.endswith(extension):
            src_path = os.path.join(source, item)
            dst_path = os.path.join(target, item)
            shutil.move(src_path, dst_path)
            moved += 1
    return moved

def get_disk_usage(path: str) -> int:
    """Calculates total size of directory contents in bytes."""
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size