import logging
from typing import Any, Callable, Optional, TypeVar

T = TypeVar('T')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_execute(func: Callable[..., T], *args: Any, default: Optional[T] = None, **kwargs: Any) -> Optional[T]:
    """
    Executes a function with graceful error handling.
    Logs exceptions and returns a default value on failure.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error(f"Execution failed in {func.__name__}: {str(e)}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system error: {str(e)}")
        raise

def validate_input(data: Any, expected_type: type) -> bool:
    """
    Validates input type to prevent downstream crashes.
    """
    if data is None:
        return False
    if not isinstance(data, expected_type):
        logger.warning(f"Type mismatch: expected {expected_type}, got {type(data)}")
        return False
    return True

if __name__ == '__main__':
    # Example usage for demonstration
    result = safe_execute(lambda x: 10 / x, 0, default=0)
    logger.info(f"Safe result: {result}")