class BaseUtilsError(Exception):
    """Base exception class for python-utils-39."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when configuration validation fails."""
    pass

class ValidationError(BaseUtilsError):
    """Raised during data integrity validation."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised during pipeline execution tasks."""
    def __init__(self, message: str, stage: str = "unknown"):
        super().__init__(f"{message} (stage: {stage})")
        self.stage = stage

class ResourceNotFoundError(BaseUtilsError):
    """Raised when a required resource is missing."""
    pass

def handle_exception(e: Exception) -> None:
    """Standardized exception formatting for logs."""
    if isinstance(e, BaseUtilsError):
        print(f"Application error: {type(e).__name__} - {str(e)}")
    else:
        print(f"Unexpected system error: {str(e)}")