from typing import Any, Optional, Union

def validate_numeric(value: Any, min_val: Optional[float] = None, max_val: Optional[float] = None) -> bool:
    """Checks if value is a valid number within specified bounds."""
    try:
        numeric_val = float(value)
    except (TypeError, ValueError):
        return False
    
    if min_val is not None and numeric_val < min_val:
        return False
    if max_val is not None and numeric_val > max_val:
        return False
        
    return True

def sanitize_string(value: Any, strip: bool = True, default: str = "") -> str:
    """Ensures input is a string, optionally stripping whitespace."""
    if not isinstance(value, str):
        return default
    return value.strip() if strip else value

def validate_required(data: dict, keys: list[str]) -> bool:
    """Ensures all specified keys exist in dictionary and are non-empty."""
    for key in keys:
        if key not in data or data[key] is None:
            return False
        if isinstance(data[key], str) and not data[key].strip():
            return False
    return True

def cast_to_bool(value: Any) -> bool:
    """Converts common truthy values to boolean."""
    if isinstance(value, bool):
        return value
    str_val = str(value).lower()
    return str_val in ('true', '1', 't', 'y', 'yes')