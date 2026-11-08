import re
from typing import Any, Optional

def is_email(value: str) -> bool:
    """Validate RFC 5322 email string format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, value))

def is_valid_uuid(val: str) -> bool:
    """Validate standard 8-4-4-4-12 UUID format."""
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    return bool(re.match(pattern, val.lower()))

def ensure_list(data: Any) -> list:
    """Force input into a flat list structure."""
    if data is None:
        return []
    if isinstance(data, (list, tuple, set)):
        return list(data)
    return [data]

def is_truthy(value: Any) -> bool:
    """Determine boolean status for loose input."""
    if isinstance(value, str):
        return value.lower() in ('true', '1', 'yes', 'y', 't')
    return bool(value)

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Check integer bounds for inclusive range."""
    return min_val <= value <= max_val