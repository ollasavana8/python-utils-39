from typing import Any, Dict, List


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flatten a nested dictionary recursively by joining keys with a separator.
    """
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def safe_get(d: Dict[str, Any], path: str, default: Any = None, sep: str = '.') -> Any:
    """
    Safely retrieve nested values from a dictionary using a delimited path string.
    """
    if not isinstance(d, dict):
        return default

    keys = path.split(sep)
    current: Any = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
