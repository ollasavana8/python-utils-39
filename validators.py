class ValidationError(Exception):
    pass

def validate_positive_integer(value):
    """Validates that the input is a positive integer."""
    if not isinstance(value, int):
        raise ValidationError(f'Expected integer, got {type(value).__name__}')
    if value <= 0:
        raise ValidationError('Value must be a positive integer')
    return True

def validate_non_empty_string(value):
    """Validates that the input is a non-empty string."""
    if not isinstance(value, str):
        raise ValidationError(f'Expected string, got {type(value).__name__}')
    if not value:
        raise ValidationError('String cannot be empty')
    return True

def validate_email(email):
    """Validates that the input is a valid email format."""
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValidationError('Invalid email format')
    return True

# Example Usages:
try:
    validate_positive_integer(10)
    validate_non_empty_string('Hello World')
    validate_email('test@example.com')
except ValidationError as e:
    print(f'Validation error: {e}')