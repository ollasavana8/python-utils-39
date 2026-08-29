import os
import json
from typing import Any, Dict, List, Optional, Union

def read_json_file(filepath: str) -> Optional[Dict[str, Any]]:
    """Read JSON from file, return None on error."""
    if not os.path.isfile(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return None

def write_json_file(filepath: str, data: Dict[str, Any]) -> bool:
    """Write data to JSON file, return success status."""
    try:
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception:
        return False

def flatten_nested_list(nested: List[Any]) -> List[Any]:
    """Flatten a list containing nested lists."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result

def get_value_from_dict(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Get nested value using dot notation path like 'a.b.c'."""
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def chunk_iterable(iterable: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split list into chunks of given size."""
    if chunk_size < 1:
        return [iterable]
    return [iterable[i:i + chunk_size] for i in range(0, len(iterable), chunk_size)]


def find_files_by_ext(directory: str, extension: str = '.txt') -> List[str]:
    """Recursively find files with specific extension."""
    matches = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                matches.append(os.path.join(root, filename))
    return matches