import os
import json
from typing import Any, Optional

def load_json_file(file_path: str) -> dict:
    """Loads and parses a JSON file safely."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data: dict, file_path: str) -> None:
    """Saves dictionary to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default or "")

def ensure_directory(path: str) -> None:
    """Creates directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def chunk_list(items: list, size: int):
    """Yields successive n-sized chunks from list."""
    for i in range(0, len(items), size):
        yield items[i:i + size]

def flatten_list(nested_list: list) -> list:
    """Flattens a list of lists into one."""
    return [item for sublist in nested_list for item in sublist]