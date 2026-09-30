import functools
import time
from typing import Callable, Any, Dict

# Cache to store results of expensive computations
_cache: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

class DataProcessor:
    """Core processor with performance-oriented batch handling."""
    def __init__(self, chunk_size: int = 1000):
        self.chunk_size = chunk_size

    def batch_process(self, data: list) -> list:
        """Process data in chunks to optimize memory usage."""
        results = []
        for i in range(0, len(data), self.chunk_size):
            chunk = data[i:i + self.chunk_size]
            results.extend(self._transform(chunk))
        return results

    def _transform(self, chunk: list) -> list:
        """Internal transformation logic mapped efficiently."""
        return [item * 2 for item in chunk]

    def clear_cache(self) -> None:
        """Utility to force cache reset."""
        _cache.clear()