import re
from typing import Any, Optional

# Regex pattern for basic email validation
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class DataValidator:
    """Utility class for common data validation tasks."""

    @staticmethod
    def is_email(email: Any) -> bool:
        """Verify email string format."""
        if not isinstance(email, str):
            return False
        return bool(EMAIL_PATTERN.match(email))

    @staticmethod
    def is_not_empty(value: Optional[str]) -> bool:
        """Check for non-null and non-whitespace string."""
        return isinstance(value, str) and len(value.strip()) > 0

    @classmethod
    def validate_range(cls, value: int, min_val: int, max_val: int) -> bool:
        """Ensure integer is within inclusive boundaries."""
        return isinstance(value, int) and min_val <= value <= max_val

def validate_input(data: dict, schema: dict) -> bool:
    """Core validation logic for dictionary payloads."""
    for key, validator_func in schema.items():
        if key not in data or not validator_func(data[key]):
            return False
    return True