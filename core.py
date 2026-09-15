import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Executes a function safely with granular exception handling."""
    try:
        return func(*args, **kwargs)
    except TypeError as e:
        logger.error(f"Type mismatch in {func.__name__}: {e}")
    except ValueError as e:
        logger.error(f"Invalid input value in {func.__name__}: {e}")
    except Exception as e:
        logger.critical(f"Unexpected failure in {func.__name__}: {e}", exc_info=True)
    return default

def validate_resource(data: Optional[dict], keys: list[str]) -> bool:
    """Verifies dictionary presence and required key existence."""
    if not isinstance(data, dict):
        return False
    return all(key in data for key in keys)

def safe_coerce_int(value: Any, fallback: int = 0) -> int:
    """Converts input to integer with robust error handling."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return fallback