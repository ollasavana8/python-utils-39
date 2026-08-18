class CustomError(Exception):
    """
    Custom exception class for handling specific errors.
    """
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

class ValidationError(CustomError):
    """
    Exception raised for validation errors.
    """
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field

class NotFoundError(CustomError):
    """
    Exception raised when an item is not found.
    """
    def __init__(self, message):
        super().__init__(message)

class AuthenticationError(CustomError):
    """
    Exception raised for authentication failures.
    """
    def __init__(self, message):
        super().__init__(message)

class PermissionDeniedError(CustomError):
    """
    Exception raised for permission related errors.
    """
    def __init__(self, message):
        super().__init__(message)
