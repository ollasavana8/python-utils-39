import json
import os
from typing import Any, Dict, List, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Load and parse JSON file contents."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Any, filepath: str) -> None:
    """Write data to a JSON file with formatting."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, sort_keys=True)

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list of items."""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split list into chunks of specific size."""
    return [data[i:i + size] for i in range(0, len(data), size)]

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default or "")