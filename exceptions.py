class UtilityError(Exception):
    """Base exception class for python-utils-39."""
    pass

class ConfigurationError(UtilityError):
    """Raised when configuration requirements are not met."""
    pass

class ValidationError(UtilityError):
    """Raised during data integrity check failures."""
    pass

def handle_execution(func):
    """Decorator for centralized error wrapping and logging."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError) as e:
            raise ValidationError(f"Input validation failed: {str(e)}") from e
        except KeyError as e:
            raise ConfigurationError(f"Missing required configuration: {str(e)}") from e
        except Exception as e:
            # Catch-all for unexpected runtime edge cases
            raise UtilityError(f"Unexpected system failure: {str(e)}") from e
    return wrapper

if __name__ == "__main__":
    # Verification logic for robust error wrapping
    @handle_execution
    def test_op(data):
        return data['key']

    try:
        test_op({})
    except ConfigurationError:
        pass