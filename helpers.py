"""General utility helper functions for data manipulation and execution control."""

import time
from typing import Any, Callable, Dict, Generator, List, TypeVar, Optional

T = TypeVar("T")


def chunk_iterable(iterable: List[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of specified size from a list.

    Args:
        iterable: The list to be split into chunks.
        chunk_size: Maximum size of each yielded chunk.

    Yields:
        Lists of elements up to chunk_size long.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i : i + chunk_size]


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary using separator key join.

    Args:
        d: The nested dictionary to flatten.
        parent_key: Prefix key used during recursive traversal.
        sep: Separator character between joined nested keys.

    Returns:
        A flat dictionary with combined keys.
    """
    items: Dict[str, Any] = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


def retry_operation(
    func: Callable[[], T],
    retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
) -> Optional[T]:
    """Execute a callable with exponential backoff retry logic on failure.

    Args:
        func: Zero-argument function to attempt.
        retries: Maximum number of failed retries allowed.
        delay: Initial pause in seconds before the first retry.
        backoff_factor: Multiplier applied to delay after every failed attempt.

    Returns:
        The result of func if successful, or None if retries exhaust.
    """
    current_delay = delay
    for attempt in range(retries + 1):
        try:
            return func()
        except Exception:
            if attempt == retries:
                raise
            time.sleep(current_delay)
            current_delay *= backoff_factor
    return None
