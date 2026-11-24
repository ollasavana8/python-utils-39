from typing import Any, Dict, List, Union, Optional

def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested dictionary values using dot notation."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split list into smaller sub-lists of fixed size."""
    if size <= 0:
        return [items]
    return [items[i:i + size] for i in range(0, len(items), size)]

def sanitize_dict(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Remove sensitive or unwanted keys from dictionary."""
    return {k: v for k, v in data.items() if k not in keys}

def flatten_list(nested_list: List[Union[Any, List[Any]]]) -> List[Any]:
    """Convert list of lists into flat list."""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat