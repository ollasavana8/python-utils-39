import functools
import time
from typing import Any, Callable, Dict

# Cache for expensive function computations
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Performance decorator for expensive repeated calculations"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    """Generator for memory-efficient batch processing"""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTracker:
    """Context manager for tracking execution time"""
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.duration = self.end - self.start
        print(f"Execution took {self.duration:.4f} seconds")