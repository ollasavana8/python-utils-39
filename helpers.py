"""General helper utilities for data manipulation and string processing."""

import re
from typing import Any, Iterable, List, TypeVar

T = TypeVar("T")


def chunk_list(items: List[T], chunk_size: int) -> List[List[T]]:
    """Split a list into smaller chunks of a specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def flatten(container: Iterable[Any]) -> List[Any]:
    """Flatten nested lists or tuples into a single flat list."""
    flat_list = []
    for item in container:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def deep_get(data: dict, key_path: str, default: Any = None) -> Any:
    """Retrieve nested dictionary values using dot-separated keys."""
    keys = key_path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def slugify(text: str) -> str:
    """Convert string into a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)
