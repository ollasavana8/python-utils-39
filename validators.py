import re

# regex patterns for general utility validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_input(data, schema):
    """Validates dictionary data against a schema dict of types."""
    for key, expected_type in schema.items():
        if key not in data:
            raise ValueError(f"Missing required field: {key}")
        
        value = data[key]
        if not isinstance(value, expected_type):
            raise TypeError(f"Field '{key}' expects {expected_type}, got {type(value)}")

def validate_email(email):
    """Checks if string matches standard email format."""
    if not isinstance(email, str) or not EMAIL_REGEX.match(email):
        return False
    return True

def sanitize_input(value):
    """Removes potential injection characters from input."""
    if not isinstance(value, str):
        return value
    return re.sub(r'[;<>"\']', '', value)