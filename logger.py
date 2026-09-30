import logging
import functools
import time
from typing import Callable, Any

# Cache for logger instances to reduce object instantiation overhead
_LOGGERS = {}

def get_logger(name: str) -> logging.Logger:
    """Provides a cached logger instance for performance."""
    if name not in _LOGGERS:
        _LOGGERS[name] = logging.getLogger(name)
    return _LOGGERS[name]

def timed_execution(func: Callable) -> Callable:
    """Decorator to log execution time of core methods."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            logger = get_logger(func.__module__)
            logger.debug(f"function {func.__name__} took {elapsed:.4f}s")
    return wrapper

class PerformanceLogger:
    """Lightweight logger wrapper for high-frequency operations."""
    def __init__(self, name: str):
        self._logger = get_logger(name)
        self._enabled = self._logger.isEnabledFor(logging.DEBUG)

    def log_if_slow(self, threshold: float, func_name: str, duration: float) -> None:
        if self._enabled and duration > threshold:
            self._logger.warning(f"Slow operation in {func_name}: {duration:.4f}s")