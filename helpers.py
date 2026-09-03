import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """
    Executes a function safely with error catching for common edge cases.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Data validation error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure in {func.__name__}: {e}", exc_info=True)
        return default

def validate_input(data: Any, expected_type: type) -> bool:
    """
    Validates input type and handles empty edge cases.
    """
    if data is None:
        return False
    return isinstance(data, expected_type)

def format_data_safely(data: Any) -> str:
    """
    Safely stringifies inputs avoiding attribute access errors.
    """
    if data is None:
        return ""
    try:
        return str(data)
    except Exception:
        return "[Unparseable Data]"

def get_dict_path(data: dict, path: str, default: Any = None) -> Any:
    """
    Accesses nested dictionary keys safely without KeyError.
    """
    try:
        keys = path.split('.')
        val = data
        for key in keys:
            val = val[key]
        return val
    except (KeyError, TypeError, AttributeError):
        return default