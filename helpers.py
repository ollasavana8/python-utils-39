import functools
import time
from typing import Callable, Any, Dict

def memoize_with_ttl(ttl_seconds: int = 300) -> Callable:
    """Performance decorator for caching function results with TTL."""
    def decorator(func: Callable) -> Callable:
        cache: Dict[tuple, tuple] = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            key = (args, frozenset(kwargs.items()))
            now = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def bulk_process(items: list, chunk_size: int = 100) -> Any:
    """Generator for efficient memory usage on large datasets."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceOptimizer:
    """Resource-conscious object wrapper for data operations."""
    def __init__(self, data: list):
        self._data = data

    @property
    def optimized_view(self) -> list:
        # Pre-allocation to avoid dynamic list resizing
        return [x for x in self._data if x is not None]