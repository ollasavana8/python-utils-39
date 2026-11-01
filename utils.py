import math
from typing import Any, Dict, Generator, Iterable, List, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of specified size from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries without mutating originals."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def format_bytes(num_bytes: float) -> str:
    """Convert standard byte count into a human-readable string representation."""
    if num_bytes < 0:
        raise ValueError("Byte count cannot be negative.")
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    unit_index = 0
    value = float(num_bytes)

    while value >= 1024.0 and unit_index < len(units) - 1:
        value /= 1024.0
        unit_index += 1

    return f"{value:.2f} {units[unit_index]}"
