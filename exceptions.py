"""Custom exception classes for python-utils-39.

This module defines the standard hierarchy of exceptions used across the
utility library, allowing for precise error handling and rich error contexts.
"""

from typing import Any, Dict, Optional


class BaseUtilError(Exception):
    """Base exception for all errors raised by this utility library."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the base exception with a message and optional metadata.

        Args:
            message: A human-readable error description.
            details: Optional dictionary containing additional error context.
        """
        super().__init__(message)
        self.message: str = message
        self.details: Dict[str, Any] = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} (Context: {self.details})"
        return self.message


class ValidationError(BaseUtilError):
    """Exception raised when utility arguments or configuration fail validation."""


class ConfigurationError(BaseUtilError):
    """Exception raised when configuration parameters are missing or invalid."""


class ResourceNotFoundError(BaseUtilError):
    """Exception raised when a requested resource, file, or key is not found."""

    def __init__(
        self, message: str, resource_identifier: Optional[str] = None
    ) -> None:
        """Initialize with resource-specific identifier.

        Args:
            message: Description of the missing resource.
            resource_identifier: The name or path of the missing resource.
        """
        details = {"resource": resource_identifier} if resource_identifier else None
        super().__init__(message, details=details)
        self.resource_identifier: Optional[str] = resource_identifier
