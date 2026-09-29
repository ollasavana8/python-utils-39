import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for validation edge cases."""
    pass

def validate_input(value: Any, expected_type: type) -> bool:
    """Validates input type and handles null or edge cases."""
    try:
        if value is None:
            raise ValidationError("input value cannot be None")
        
        if not isinstance(value, expected_type):
            raise TypeError(f"expected {expected_type.__name__}, got {type(value).__name__}")
            
        return True
    except (ValidationError, TypeError) as e:
        logger.error("validation failure: %s", e)
        return False

def safe_get_index(data: list, index: int, default: Any = None) -> Any:
    """Retrieves list index with safe bounds handling."""
    if not isinstance(data, list):
        return default
        
    try:
        return data[index]
    except IndexError:
        logger.warning("index %d out of bounds for list length %d", index, len(data))
        return default
    except Exception as e:
        logger.error("unexpected error during index access: %s", e)
        return default