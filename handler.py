import logging
import traceback
from typing import Any, Callable, Optional, Tuple

logger = logging.getLogger(__name__)


class ExecutionError(Exception):
    """Custom exception raised when task execution fails safely."""
    def __init__(self, message: str, original_exception: Optional[Exception] = None):
        super().__init__(message)
        self.original_exception = original_exception


class SafeTaskHandler:
    """Handles execution of arbitrary tasks with robust error catching."""

    def __init__(self, suppress_exceptions: bool = False, default_return: Any = None):
        self.suppress_exceptions = suppress_exceptions
        self.default_return = default_return

    def execute(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Tuple[bool, Any]:
        """Execute a callable safely, handling standard edge cases and unhandled exceptions."""
        if func is None or not callable(func):
            logger.error("Invalid task provided: task is None or not callable")
            if self.suppress_exceptions:
                return False, self.default_return
            raise ExecutionError("Target task must be a valid callable")

        try:
            result = func(*args, **kwargs)
            return True, result
        except (TypeError, ValueError) as err:
            logger.warning(f"Data or type mismatch during execution: {err}")
            if self.suppress_exceptions:
                return False, self.default_return
            raise ExecutionError(f"Invalid input data or type: {err}", err) from err
        except ZeroDivisionError as err:
            logger.warning("Attempted division by zero in task execution")
            if self.suppress_exceptions:
                return False, self.default_return
            raise ExecutionError("Math error: division by zero", err) from err
        except Exception as err:
            func_name = getattr(func, '__name__', str(func))
            logger.error(f"Unexpected error executing {func_name}: {err}\n{traceback.format_exc()}")
            if self.suppress_exceptions:
                return False, self.default_return
            raise ExecutionError(f"Task failed unexpectedly: {err}", err) from err
