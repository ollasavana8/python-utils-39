import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_on_failure(exceptions: tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0):
    """Decorator to retry network functions on specific exceptions."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        sleep_time = delay * (2 ** attempt)
                        logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {sleep_time}s...")
                        time.sleep(sleep_time)
                    else:
                        logger.error(f"Max retries reached. Final failure: {e}")
            raise last_exception
        return wrapper
    return decorator

def execute_with_retry(func: Callable, *args: Any, **kwargs: Any) -> Any:
    """Functional wrapper for one-off retry logic."""
    retry_wrapper = retry_on_failure((ConnectionError, TimeoutError))(func)
    return retry_wrapper(*args, **kwargs)