import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry(exceptions: Tuple[Type[Exception], ...], tries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"{func.__name__} failed: {e}. Retrying in {mdelay}s...")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage:
# @retry((ConnectionError, TimeoutError), tries=3, delay=2)
# def fetch_data(url):
#     pass