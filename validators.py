from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """Verify if a string follows basic email format."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return email.count("@") == 1 and "." in email.split("@")[-1]

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if number falls within inclusive boundary."""
    return min_val <= value <= max_val

def sanitize_input(data: Any, default: Any = None) -> Any:
    """Ensure data is not None, return default if empty."""
    return data if data is not None else default

def validate_required_keys(data: dict, keys: list[str]) -> bool:
    """Confirm all mandatory keys exist in dictionary."""
    return all(key in data for key in keys)

def is_truthy(value: Any) -> bool:
    """Check if value evaluates to True including string checks."""
    if isinstance(value, str):
        return value.lower() in ("true", "1", "yes", "on")
    return bool(value)