"""Custom exception classes and error handling utilities for edge cases."""

from typing import Any, Optional


class BaseUtilsError(Exception):
    """Base exception for all utility module errors."""

    def __init__(self, message: str, payload: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message = message
        self.payload = payload

    def to_dict(self) -> dict[str, Any]:
        """Serialize exception details into a structured dictionary."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "payload": self.payload,
        }


class ValidationError(BaseUtilsError):
    """Raised when input validation fails across utility functions."""

    pass


class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource or file cannot be located."""

    pass


class ConfigurationError(BaseUtilsError):
    """Raised when invalid or missing configuration values are encountered."""

    pass


def safe_execute(func, *args, default_return: Any = None, **kwargs) -> Any:
    """Execute a callable safely, catching utility errors and returning a default value."""
    try:
        return func(*args, **kwargs)
    except BaseUtilsError:
        return default_return
    except (ValueError, TypeError, KeyError) as err:
        raise ValidationError(f"Invalid operation data: {err}") from err
