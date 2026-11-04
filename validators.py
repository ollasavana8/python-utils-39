import re
from functools import lru_cache
from typing import Optional

# Pre-compile regex patterns for performance
_EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

@lru_cache(maxsize=128)
def validate_email_format(email: str) -> bool:
    """Validates email format using cached regex evaluation."""
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_REGEX.match(email))

def sanitize_input(value: str) -> str:
    """Strips whitespace and normalizes string input."""
    if not isinstance(value, str):
        return ''
    return value.strip()

def batch_validate(items: list[str]) -> list[bool]:
    """Efficient batch validation using cached function calls."""
    return [validate_email_format(item) for item in items]

class ValidatorContext:
    """Contextual wrapper for validation logic."""
    def __init__(self, strict: bool = True):
        self.strict = strict

    def check(self, email: Optional[str]) -> bool:
        if email is None:
            return not self.strict
        return validate_email_format(email)