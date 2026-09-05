from typing import Any, Optional

def validate_email(email: Any) -> bool:
    """Check if the provided input is a valid email string format."""
    if not isinstance(email, str):
        return False
    return "@" in email and "." in email.split("@")[-1]

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Verify that an integer falls within a specified inclusive range."""
    return min_val <= value <= max_val

def sanitize_input(value: Optional[str]) -> str:
    """Remove whitespace and return empty string if input is None."""
    if value is None:
        return ""
    return value.strip()

def is_not_empty(data: Any) -> bool:
    """Return true if the object has a length greater than zero."""
    try:
        return len(data) > 0
    except TypeError:
        return False