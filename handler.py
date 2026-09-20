import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

class ExecutionHandler:
    """Utility to safely execute callables with error boundaries."""

    @staticmethod
    def execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
        """
        Executes a function safely, returning a default value on failure.
        Handles common runtime exceptions to prevent application crashes.
        """
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, AttributeError) as e:
            logger.error(f"Execution error in {func.__name__}: {str(e)}")
            return default
        except Exception as e:
            logger.critical(f"Unexpected system error: {str(e)}", exc_info=True)
            return default

    @staticmethod
    def validate_input(data: Optional[Any], expected_type: type) -> bool:
        """
        Strict validation for input types to handle edge cases.
        Returns False if data is None or wrong type.
        """
        if data is None:
            logger.warning("Input validation failed: data is None")
            return False
        
        if not isinstance(data, expected_type):
            logger.warning(f"Expected {expected_type}, got {type(data)}")
            return False
            
        return True