import collections.abc
from typing import Any, Dict, List, Union

def deep_flatten(items: Iterable) -> List[Any]:
    """Flatten nested sequences into a single list."""
    result = []
    for item in items:
        if isinstance(item, (list, tuple, set)) and not isinstance(item, (str, bytes)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    """Recursively merge two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def sanitize_keys(data: Dict[str, Any], prefix: str = "_") -> Dict[str, Any]:
    """Prefix dictionary keys with provided string."""
    return {f"{prefix}{k}": v for k, v in data.items()}

from typing import Iterable