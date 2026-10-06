import functools
import time
from typing import Callable, Any, Dict

# Cache dictionary for memoization of expensive function calls
_FUNCTION_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _FUNCTION_CACHE:
            _FUNCTION_CACHE[key] = func(*args, **kwargs)
        return _FUNCTION_CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 1000):
    """Generator to process large datasets in memory-efficient chunks."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTracker:
    """Context manager for tracking block execution time."""
    def __init__(self, label: str):
        self.label = label
        self.start_time = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        print(f"[PERF] {self.label} finished in {elapsed:.4f}s")