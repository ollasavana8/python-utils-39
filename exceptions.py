class CustomError(Exception):
    """Exception raised for specific errors in the application."""
    def __init__(self, message: str, code: int = 500) -> None:
        """Initialize CustomError with a message and an error code."""
        super().__init__(message)
        self.code = code

    def __str__(self) -> str:
        """Return string representation of the error."""
        return f"{self.code}: {self.args[0]}"

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, message: str) -> None:
        """Initialize ValidationError with a custom message."""
        super().__init__(message, code=400)

class NotFoundError(CustomError):
    """Exception raised when a resource is not found."""
    def __init__(self, resource: str) -> None:
        """Initialize NotFoundError with the resource that was not found."""
        message = f"{resource} not found"
        super().__init__(message, code=404)
