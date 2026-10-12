import functools
import time
from typing import Any, Callable, Dict, Optional, Tuple


class LRUTTLMemoryCache:
    """A lightweight cache supporting maximum size and time-to-live (TTL) expiration."""

    def __init__(self, maxsize: int = 1024, ttl_seconds: float = 60.0):
        self.maxsize = maxsize
        self.ttl_seconds = ttl_seconds
        self._cache: Dict[Any, Tuple[Any, float]] = {}

    def get(self, key: Any) -> Optional[Any]:
        """Retrieve a non-expired cached value."""
        if key not in self._cache:
            return None
        value, timestamp = self._cache[key]
        if time.time() - timestamp > self.ttl_seconds:
            del self._cache[key]
            return None
        return value

    def set(self, key: Any, value: Any) -> None:
        """Cache a value, evicting the oldest entry if size limit is exceeded."""
        if len(self._cache) >= self.maxsize and key not in self._cache:
            first_key = next(iter(self._cache))
            del self._cache[first_key]
        self._cache[key] = (value, time.time())

    def clear(self) -> None:
        """Purge all cached entries."""
        self._cache.clear()


def memoize_with_ttl(ttl_seconds: float = 300.0, maxsize: int = 512):
    """Decorator to cache function results with TTL and capacity limits."""
    cache = LRUTTLMemoryCache(maxsize=maxsize, ttl_seconds=ttl_seconds)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, frozenset(kwargs.items()))
            cached_result = cache.get(key)
            if cached_result is not None:
                return cached_result
            result = func(*args, **kwargs)
            cache.set(key, result)
            return result

        wrapper.cache_clear = cache.clear
        return wrapper

    return decorator


@memoize_with_ttl(ttl_seconds=120.0, maxsize=2048)
def fast_hash_transform(data: str, iterations: int = 100) -> str:
    """Perform optimized iterative string transformation with memoized lookups."""
    result = data
    for _ in range(iterations):
        result = f"{hash(result):x}"
    return result
