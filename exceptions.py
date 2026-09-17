"""Custom exception hierarchy for general utility operations."""

from typing import Any, Optional


class BaseUtilError(Exception):
    """Base exception class for python-utils-39 module errors."""

    def __init__(self, message: str, payload: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.payload = payload or {}

    def to_dict(self) -> dict[str, Any]:
        """Return error metadata and payload as a dictionary."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.payload,
        }


class ValidationError(BaseUtilError):
    """Raised when input validation fails."""

    pass


class ConfigurationError(BaseUtilError):
    """Raised when invalid or missing configuration parameters are detected."""

    pass


class ProcessingError(BaseUtilError):
    """Raised when a generic utility task fails during execution."""

    pass


class ResourceNotFoundError(BaseUtilError):
    """Raised when a requested file or memory resource cannot be found."""

    pass


def format_exception_chain(error: Exception) -> list[str]:
    """Extract and format messages from a chained exception sequence."""
    chain = []
    current: Optional[BaseException] = error
    while current is not None:
        chain.append(f"{current.__class__.__name__}: {str(current)}")
        current = current.__cause__ or current.__context__
    return chain
