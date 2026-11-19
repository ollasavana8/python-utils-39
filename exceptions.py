class UtilsError(Exception):
    """Base exception for python-utils-39 operations."""
    pass

class ConfigurationError(UtilsError):
    """Raised when configuration validation fails."""
    pass

class ProcessingError(UtilsError):
    """Raised when a data processor encounters bad input."""
    pass

class ValidationError(UtilsError):
    """Raised for input data validation failures."""
    pass

def handle_exception(exc: Exception) -> None:
    """Centralized error reporting utility."""
    if isinstance(exc, UtilsError):
        print(f"[Handled] {type(exc).__name__}: {exc}")
    else:
        print(f"[Unhandled] Unexpected error: {exc}")

def safe_execute(func, *args, **kwargs):
    """Decorator pattern for wrapping risky calls."""
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, KeyError) as e:
        raise ProcessingError(f"Input operation failed: {e}") from e
    except Exception as e:
        handle_exception(e)
        raise