import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

class NetworkProcessor:
    """Service class for executing network-bound tasks."""
    
    @with_retry(retries=3, delay=2.0)
    def fetch_data(self, url: str):
        """Mock function representing a volatile network request."""
        # Simulated transient error logic
        import random
        if random.random() < 0.7:
            raise ConnectionError("Temporary server timeout")
        return {"status": 200, "data": "success"}