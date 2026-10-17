import functools
import logging
import time
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)


def retry(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """
    Decorator that retries a function upon failure using exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed permanently after "
                            f"{max_retries} attempts. Error: {exc}"
                        )
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed: {exc}. "
                        f"Retrying in {current_delay:.2f} seconds..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator


def execute_with_retry(
    func: Callable,
    *args: Any,
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    **kwargs: Any,
) -> Any:
    """Helper to execute a function directly with retry logic."""
    decorated_func = retry(
        max_retries=max_retries,
        delay=delay,
        backoff=backoff,
        exceptions=exceptions,
    )(func)
    return decorated_func(*args, **kwargs)
