import functools
import time
from typing import Callable, Any, Dict

# Cache for compute-intensive function results
_CACHE: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = f"{func.__name__}:{args}:{kwargs}"
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

class PerformanceOptimizer:
    """Utility class for execution time tracking."""
    @staticmethod
    def profile_execution(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            # Log performance metrics in production environments
            print(f"Execution of {func.__name__}: {end_time - start_time:.6f}s")
            return result
        return wrapper

def clear_optimization_cache() -> None:
    """Manual invalidation of global memoization cache."""
    _CACHE.clear()