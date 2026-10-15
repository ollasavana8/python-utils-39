import functools
import time
from typing import Callable, Any, Dict

# Cache for performance-critical transformations
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Memory-efficient batch processing for large lists."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Profiler for measuring function latency."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        print(f"Execution of {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def clear_cache() -> None:
    """Memory management for memoization storage."""
    _memoization_cache.clear()