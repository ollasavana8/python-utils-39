"""General utility helper functions for common data manipulation tasks."""

from typing import Any, Dict, Generator, Iterable, List, Optional, Type, TypeVar

T = TypeVar('T')


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Split an iterable into chunks of a specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def safe_cast(val: Any, to_type: Type[T], default: Optional[T] = None) -> Optional[T]:
    """Safely cast a value to a target type, returning default on failure."""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary structure using dot notation keys."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries, giving precedence to the second."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
