import functools
import time
from typing import Callable, Any, Dict

_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Cache function results based on arguments for performance."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, size: int = 100):
    """Memory-efficient generator for large dataset chunks."""
    for i in range(0, len(items), size):
        yield items[i:i + size]

class PerformanceTracker:
    """Context manager for simple execution timing."""
    def __init__(self, label: str):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"{self.label} took {elapsed:.4f} seconds")