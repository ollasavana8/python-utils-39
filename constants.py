from typing import Final, Dict, List

# Network timeout settings in seconds
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported configuration environments
ENVIRONMENTS: Final[List[str]] = ['development', 'staging', 'production']

# Mapping for status code definitions
STATUS_CODES: Final[Dict[int, str]] = {
    200: 'OK',
    400: 'BAD_REQUEST',
    401: 'UNAUTHORIZED',
    404: 'NOT_FOUND',
    500: 'INTERNAL_SERVER_ERROR'
}

def get_status_description(code: int) -> str:
    """Return the descriptive string for a given status code."""
    return STATUS_CODES.get(code, 'UNKNOWN')

class AppConfig:
    """Global application configuration constants."""
    VERSION: Final[str] = "1.0.0"
    BASE_DIR: Final[str] = "/opt/python-utils-39"