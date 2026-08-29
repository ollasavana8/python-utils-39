"""Utility functions for general data handling."""

import copy

from typing import Any, Dict, List, Union

def deep_merge_dicts(base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries.

    Nested dictionaries are merged, other values overridden.
    """
    result = copy.deepcopy(base)
    for key, value in update.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result

def safe_get(data: Any, path: List[Union[str, int]], default: Any = None) -> Any:
    """Safely retrieve value from nested structure.

    Supports dicts and lists. Returns default on failure.
    """
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, (list, tuple)) and isinstance(key, int):
            if 0 <= key < len(current):
                current = current[key]
            else:
                return default
        else:
            return default
    return current

def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary.

    Keys are joined with separator for nested levels.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """Divide a list into smaller chunks.

    Each chunk has at most chunk_size elements.
    """
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunks.append(data[i:i + chunk_size])
    return chunks

def update_nested(data: Dict[str, Any], path: List[str], value: Any) -> Dict[str, Any]:
    """Update a nested dictionary value.

    Creates intermediate dicts if needed.
    """
    if not path:
        return data
    current = data
    for key in path[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    current[path[-1]] = value
    return data