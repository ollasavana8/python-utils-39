import json
import os
from typing import Any, Dict, Optional

def read_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Loads a JSON file and returns a dictionary."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(file_path: str, data: Dict[str, Any]) -> bool:
    """Writes a dictionary to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def chunk_list(data: list, size: int):
    """Splits a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def flatten_list(nested_list: list) -> list:
    """Flattens a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]

def get_env_variable(key: str, default: Any = None) -> Any:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default)