"""Data processing utilities for batching, dictionary manipulation, and sequence formatting."""

from typing import Any, Dict, Generator, List, Sequence, TypeVar

T = TypeVar("T")


def chunk_sequence(data: Sequence[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of a specified size from a sequence."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    for i in range(0, len(data), chunk_size):
        yield list(data[i : i + chunk_size])


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary with delimited keys."""
    items: List[tuple[str, Any]] = []
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def safe_get(data: Dict[str, Any], key_path: str, default: Any = None, sep: str = ".") -> Any:
    """Retrieve a value from a nested dictionary using a dot-separated key path safely."""
    keys = key_path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def filter_empty_values(data: Dict[str, Any], recursive: bool = False) -> Dict[str, Any]:
    """Remove keys with None or empty string values from a dictionary."""
    result = {}
    for k, v in data.items():
        if recursive and isinstance(v, dict):
            v = filter_empty_values(v, recursive=True)
        if v is not None and v != "":
            result[k] = v
    return result
