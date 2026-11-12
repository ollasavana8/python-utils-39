import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger(__name__)


def retry_on_exception(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
    exceptions: Union[Type[BaseException], Tuple[Type[BaseException], ...]] = (Exception,),
) -> Callable:
    """
    Decorator that retries a function with exponential backoff and jitter.

    Useful for handling transient errors in network operations.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == retries:
                        logger.error(
                            "Call to '%s' failed after %d attempts: %s",
                            func.__name__, retries, exc
                        )
                        raise

                    sleep_time = current_delay
                    if jitter:
                        sleep_time += random.uniform(0, current_delay * 0.5)

                    logger.warning(
                        "Attempt %d/%d for '%s' failed: %s. Retrying in %.2fs...",
                        attempt, retries, func.__name__, exc, sleep_time
                    )
                    time.sleep(sleep_time)
                    current_delay *= backoff

        return wrapper

    return decorator
