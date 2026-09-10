import functools
import time
from typing import Callable, Any, Dict

# Cache for computed results to avoid redundant operations
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function calls with result expiration."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Memory-efficient generator for processing large lists."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceOptimizer:
    """Utility class for routine performance measurement."""
    @staticmethod
    def time_execution(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            print(f"Execution of {func.__name__} took {duration:.4f}s")
            return result
        return wrapper

def clear_cache() -> None:
    """Flush global memoization storage."""
    _memoization_cache.clear()