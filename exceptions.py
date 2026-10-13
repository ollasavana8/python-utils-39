from typing import Optional

class BaseUtilsError(Exception):
    """Base exception for the python-utils-39 library."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when configuration settings are invalid."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised when data processing fails."""
    def __init__(self, message: str, code: Optional[int] = None):
        super().__init__(message)
        self.code = code

class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""
    pass

def raise_if_none(value: Optional[object], name: str) -> None:
    """Helper to ensure required values are present."""
    if value is None:
        raise ValidationError(f"Required parameter '{name}' cannot be None.")

# Standardized exception hierarchy for consistent error handling
# across all project modules.