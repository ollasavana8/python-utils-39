import os

# Application path configurations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# System operation constants
DEFAULT_ENCODING = 'utf-8'
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Environment status flags
IS_DEBUG = os.getenv('DEBUG', 'False') == 'True'
ENVIRONMENT = os.getenv('APP_ENV', 'development')

# Resource limits
CHUNK_SIZE = 8192
BUFFER_SIZE = 1024 * 1024

# Standard error messages
ERR_MISSING_CONFIG = "Missing required configuration key: {key}"
ERR_CONNECTION_FAILED = "Failed to establish connection to {host}"

def get_version():
    """Return utility package version."""
    return "1.0.4"