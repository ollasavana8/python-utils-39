import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """Decorator to retry network-bound operations."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay * (2 ** attempt))
            logger.error("Max retries reached. Operation failed.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3)
def fetch_data_with_retry(url: str):
    """Example usage for network data retrieval."""
    # Simulated network call
    print(f"Fetching data from {url}")
    return True