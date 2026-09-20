from typing import Any, Dict, List, Optional, Union

def deep_get(dictionary: Dict[str, Any], keys: str, default: Any = None) -> Any:
    """Retrieve nested values from dictionary using dot notation."""
    parts = keys.split('.')
    current = dictionary
    try:
        for part in parts:
            current = current[part]
        return current
    except (KeyError, TypeError):
        return default

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Convert list of lists into a single flat list."""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def sanitize_dict(data: Dict[str, Any], keys_to_remove: List[str]) -> Dict[str, Any]:
    """Remove sensitive or unwanted keys from dictionary."""
    return {k: v for k, v in data.items() if k not in keys_to_remove}

def chunk_data(data: List[Any], size: int) -> List[List[Any]]:
    """Split large list into smaller equal chunks."""
    if size <= 0:
        raise ValueError("Chunk size must be positive integer")
    return [data[i:i + size] for i in range(0, len(data), size)]