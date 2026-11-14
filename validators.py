import re
from functools import lru_cache
from typing import Pattern

# Cache compiled regex patterns to avoid overhead
@lru_cache(maxsize=32)
def get_regex(pattern: str) -> Pattern:
    return re.compile(pattern)

class DataValidator:
    """High-performance data validation utilities."""

    def __init__(self):
        self._email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def is_valid_email(self, email: str) -> bool:
        """Checks email format using cached compiled regex."""
        if not email or not isinstance(email, str):
            return False
        
        regex = get_regex(self._email_pattern)
        return bool(regex.match(email))

    def bulk_validate_emails(self, email_list: list[str]) -> list[bool]:
        """Efficient batch processing of email addresses."""
        regex = get_regex(self._email_pattern)
        return [bool(regex.match(email)) for email in email_list if isinstance(email, str)]

def validate_numeric_range(value: int, min_val: int, max_val: int) -> bool:
    """Fast bound check for integer values."""
    return min_val <= value <= max_val