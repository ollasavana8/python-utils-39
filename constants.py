"""Centralized constants and default configuration settings."""

from typing import Final

# Application Metadata
APP_NAME: Final[str] = "python-utils-39"
VERSION: Final[str] = "1.4.0"

# Encoding & Formatting
DEFAULT_ENCODING: Final[str] = "utf-8"
DEFAULT_DATETIME_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"
DEFAULT_DATE_FORMAT: Final[str] = "%Y-%m-%d"

# Network & Timeouts (in seconds)
DEFAULT_TIMEOUT: Final[int] = 30
CONNECT_TIMEOUT: Final[int] = 10
MAX_RETRIES: Final[int] = 3
BACKOFF_FACTOR: Final[float] = 0.5

# File & Buffer Sizes (in bytes)
DEFAULT_BUFFER_SIZE: Final[int] = 8192  # 8 KiB
MAX_FILE_SIZE_BYTES: Final[int] = 104_857_600  # 100 MiB

# Regex Patterns
EMAIL_REGEX: Final[str] = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
SLUG_REGEX: Final[str] = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"

# Common HTTP Status Codes
HTTP_OK: Final[int] = 200
HTTP_CREATED: Final[int] = 201
HTTP_BAD_REQUEST: Final[int] = 400
HTTP_UNAUTHORIZED: Final[int] = 401
HTTP_FORBIDDEN: Final[int] = 403
HTTP_NOT_FOUND: Final[int] = 404
HTTP_INTERNAL_SERVER_ERROR: Final[int] = 500
