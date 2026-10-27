"""General utility helper functions for data manipulation."""

from typing import Any, Dict, Generator, List, Sequence, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Sequence[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Split an iterable into fixed-size chunks.
    
    Args:
        iterable: Sequence of items to chunk.
        chunk_size: Maximum size of each chunk.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    
    for i in range(0, len(iterable), chunk_size):
        yield list(iterable[i:i + chunk_size])


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Recursively flatten a nested dictionary structure.
    
    Args:
        d: Dictionary to flatten.
        parent_key: Prefix for nested keys.
        sep: Separator between key hierarchy levels.
    """
    items: List[tuple[str, Any]] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries recursively, prioritizing values in dict2.
    
    Args:
        dict1: Base dictionary.
        dict2: Dictionary with overriding values.
    """
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result