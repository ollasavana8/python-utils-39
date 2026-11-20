import functools
import time
from typing import Any, Callable, Dict

# Cache for storing expensive function results
_cache: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Performance decorator for caching function outputs."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

class DataHandler:
    def __init__(self, data_source: list):
        self._data = data_source

    @memoize
    def process_heavy_computation(self, threshold: int) -> int:
        """Simulated intensive data processing task."""
        # Simulate latency to demonstrate caching benefit
        time.sleep(0.5)
        return sum(x for x in self._data if x > threshold)

    def clear_cache(self) -> None:
        """Manual cache invalidation for memory management."""
        _cache.clear()

if __name__ == "__main__":
    handler = DataHandler([1, 2, 3, 4, 5])
    # First call is slow
    print(handler.process_heavy_computation(2))
    # Second call uses cache
    print(handler.process_heavy_computation(2))