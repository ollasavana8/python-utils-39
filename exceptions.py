class BaseUtilsError(Exception):
    """Base exception class for all library errors."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when configuration settings are invalid."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when input data fails validation."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised during unexpected task execution failure."""
    def __init__(self, message: str, context: dict = None):
        super().__init__(message)
        self.context = context or {}

class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource is missing."""
    pass

def raise_if_none(value: object, name: str) -> None:
    """Validate that the provided value is not None."""
    if value is None:
        raise ValidationError(f"Argument '{name}' cannot be None")