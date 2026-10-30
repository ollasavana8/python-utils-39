import re
from typing import Final

# Date and Time patterns
ISO_DATE_FORMAT: Final[str] = "%Y-%m-%d"
ISO_DATETIME_FORMAT: Final[str] = "%Y-%m-%dT%H:%M:%S%z"

# Regex patterns for validation
EMAIL_REGEX: Final[re.Pattern] = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
URL_REGEX: Final[re.Pattern] = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

# Pagination defaults
DEFAULT_PAGE_SIZE: Final[int] = 20
MAX_PAGE_SIZE: Final[int] = 100

# File system defaults
DEFAULT_ENCODING: Final[str] = "utf-8"
CHUNK_SIZE_BYTES: Final[int] = 8192

# HTTP status code references for readability
HTTP_OK: Final[int] = 200
HTTP_CREATED: Final[int] = 201
HTTP_BAD_REQUEST: Final[int] = 400
HTTP_UNAUTHORIZED: Final[int] = 401
HTTP_NOT_FOUND: Final[int] = 404
HTTP_SERVER_ERROR: Final[int] = 500