import functools
import logging
import random
import time
from typing import Any, Callable, Sequence, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: Sequence[Type[BaseException]] = (Exception,),
) -> Callable:
    """Decorator to retry network operations with exponential backoff."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            "Operation %s failed after %d attempts: %s",
                            func.__name__,
                            max_retries,
                            exc,
                        )
                        raise

                    sleep_time = delay
                    if jitter:
                        sleep_time += random.uniform(0, delay * 0.1)

                    logger.warning(
                        "Attempt %d/%d failed for %s (%s). Retrying in %.2fs...",
                        attempt,
                        max_retries,
                        func.__name__,
                        exc,
                        sleep_time,
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor

        return wrapper

    return decorator
