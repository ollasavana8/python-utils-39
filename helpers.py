import time
import random
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry(exceptions=(Exception,), tries=3, delay=1.0, backoff=2.0, jitter=0.1):
    """
    Decorator to retry a function call with exponential backoff and jitter.

    :param exceptions: Exception or tuple of exceptions to catch and retry.
    :param tries: Maximum number of times to try the operation.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each retry.
    :param jitter: Maximum random jitter ratio added/subtracted to/from delay.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            m_tries, m_delay = tries, delay
            while m_tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    # Calculate backoff with optional jitter
                    rand_jitter = random.uniform(-jitter, jitter) * m_delay
                    sleep_time = max(0.0, m_delay + rand_jitter)
                    
                    logger.warning(
                        f"Retrying {func.__name__} in {sleep_time:.2f} seconds "
                        f"due to {e.__class__.__name__}: {e}. "
                        f"Attempts remaining: {m_tries - 1}."
                    )
                    
                    time.sleep(sleep_time)
                    m_tries -= 1
                    m_delay *= backoff
            
            # Final attempt without catching exceptions
            return func(*args, **kwargs)
        return wrapper
    return decorator
