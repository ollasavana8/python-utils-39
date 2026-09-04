import os
from pathlib import Path
from typing import Final

# Application-wide configuration and environment constants

APP_NAME: Final[str] = 'python-utils-39'

# Paths based on project root
BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent
LOG_DIR: Final[Path] = BASE_DIR / 'logs'
DATA_DIR: Final[Path] = BASE_DIR / 'data'

# Environment settings with fallback defaults
DEBUG_MODE: Final[bool] = os.getenv('DEBUG', 'False').lower() == 'true'
MAX_RETRIES: Final[int] = int(os.getenv('MAX_RETRIES', '3'))
TIMEOUT_SECONDS: Final[int] = int(os.getenv('TIMEOUT', '30'))

# Standard naming conventions
DEFAULT_ENCODING: Final[str] = 'utf-8'
SUPPORTED_EXTENSIONS: Final[list[str]] = ['.json', '.csv', '.yaml']

# Ensure directories exist upon import
for directory in [LOG_DIR, DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

def get_app_info() -> dict[str, str | bool]:
    """Return a summary of current constants for diagnostics."""
    return {
        'app': APP_NAME,
        'debug': DEBUG_MODE,
        'max_retries': MAX_RETRIES,
        'base_path': str(BASE_DIR)
    }