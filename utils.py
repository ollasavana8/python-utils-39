import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """Decorator for retrying functions on network-related exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries:
                        logger.error(f"Failed after {max_retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator