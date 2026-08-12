class CustomError(Exception):
    """Base class for custom exceptions in this module."""
    pass

class DataNotFoundError(CustomError):
    """Exception raised when expected data is not found."""
    def __init__(self, message='Data not found.'):  
        self.message = message
        super().__init__(self.message)

class InvalidDataError(CustomError):
    """Exception raised for invalid data types or values."""
    def __init__(self, data, expected_type):
        self.message = f'Invalid data: {data}. Expected type: {expected_type}'
        super().__init__(self.message)

class DatabaseConnectionError(CustomError):
    """Exception raised for errors related to database connections."""
    def __init__(self, message='Could not connect to the database.'):  
        self.message = message
        super().__init__(self.message)

# Example usage:
# raise DataNotFoundError()
# raise InvalidDataError(data='abc', expected_type='int')
# raise DatabaseConnectionError()