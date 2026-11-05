import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger(__name__)


def retry_network_op(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = (Exception,),
) -> Callable:
    """Decorator that retries a network operation with exponential backoff.

    Args:
        retries: Maximum number of attempts before raising the exception.
        delay: Initial delay between retries in seconds.
        backoff: Multiplier applied to delay after each failure.
        exceptions: Exception types to catch and retry.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == retries:
                        logger.error("Final attempt %d failed for %s: %s", attempt, func.__name__, err)
                        raise

                    jitter = random.uniform(0, 0.1 * current_delay)
                    sleep_time = current_delay + jitter
                    logger.warning(
                        "Attempt %d/%d for %s failed (%s). Retrying in %.2fs...",
                        attempt, retries, func.__name__, err, sleep_time
                    )
                    time.sleep(sleep_time)
                    current_delay *= backoff

        return wrapper

    return decorator
