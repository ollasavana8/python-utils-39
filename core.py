import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    jitter: bool = True,
) -> Callable:
    """Decorator to retry network operations with exponential backoff and jitter."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    retries += 1
                    if retries > max_retries:
                        logger.error(
                            f"Function '{func.__name__}' failed after {max_retries} retries: {exc}"
                        )
                        raise

                    sleep_time = backoff_factor * (2 ** (retries - 1))
                    if jitter:
                        sleep_time += random.uniform(0, sleep_time * 0.1)

                    logger.warning(
                        f"Attempt {retries}/{max_retries} for '{func.__name__}' failed ({exc}). Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)

        return wrapper

    return decorator
