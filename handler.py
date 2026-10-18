import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class OperationHandler:
    def __init__(self, retries: int = 3):
        self.retries = retries

    def execute(self, func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
        """Executes a callable with basic error handling and retry logic."""
        attempt = 0
        while attempt <= self.retries:
            try:
                return func(*args, **kwargs)
            except ValueError as ve:
                logger.error(f"Invalid input encountered: {ve}")
                break
            except ConnectionError as ce:
                attempt += 1
                if attempt > self.retries:
                    logger.critical("Max retries reached for connection.")
                    raise ce
                logger.warning(f"Retry {attempt}/{self.retries} after connection failure")
            except Exception as e:
                logger.exception(f"Unexpected system error: {e}")
                return None
        return None

def safe_wrapper(func: Callable) -> Callable:
    """Decorator for capturing and logging execution errors."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Execution failed in {func.__name__}: {e}")
            return None
    return wrapper