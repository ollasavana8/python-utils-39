import os
from typing import Final

# Application path configurations
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Operational limits and defaults
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[float] = 30.0
CHUNK_SIZE: Final[int] = 1024 * 64

# Supported data formats
SUPPORTED_EXTENSIONS: Final[tuple] = ('.json', '.yaml', '.csv')

# Environment keys
ENV_PREFIX: Final[str] = 'PYUTILS_'
DEFAULT_ENCODING: Final[str] = 'utf-8'

def get_app_version() -> str:
    """Return static application version identifier."""
    return "0.1.0"

# Global flag for debug mode initialization
DEBUG_MODE: bool = os.getenv(f"{ENV_PREFIX}DEBUG", "False").lower() == "true"