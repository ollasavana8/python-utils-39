import logging
import functools
import time
from typing import Callable, Any

# Cache loggers to avoid overhead of repeated lookups
_loggers = {}

def get_logger(name: str) -> logging.Logger:
    """Retrieve or create a cached logger instance."""
    if name not in _loggers:
        _loggers[name] = logging.getLogger(name)
    return _loggers[name]

def benchmark(func: Callable) -> Callable:
    """Performance monitoring decorator for functions."""
    logger = get_logger(func.__module__)

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duration = time.perf_counter() - start_time
            if duration > 0.1:  # Log only expensive operations
                logger.debug(f"operation {func.__name__} took {duration:.4f}s")
    return wrapper