import functools
import time
from typing import Callable, Any, Dict

# Cache for function results to reduce redundant computation
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
    """Generator to yield chunks for memory-efficient iteration."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Decorator for monitoring execution performance."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"DEBUG: {func.__name__} executed in {end_time - start_time:.4f}s")
        return result
    return wrapper

# Global cleanup function for memory management
def clear_cache() -> None:
    """Flushes the memoization cache."""
    _memoization_cache.clear()