import functools
import time
from typing import Callable, Any, Dict

_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Cache function results to avoid redundant computation."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, batch_size: int = 100):
    """Yield successive chunks from items for memory efficiency."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

class PerformanceTracker:
    """Context manager for tracking execution duration."""
    def __init__(self, name: str):
        self.name = name
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[PERF] {self.name}: {elapsed:.4f}s")