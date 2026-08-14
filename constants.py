# Constants used across the application

# Define common error messages
INVALID_INPUT = 'Invalid input provided'
RESOURCE_NOT_FOUND = 'Requested resource was not found'
UNAUTHORIZED_ACCESS = 'User is not authorized to perform this action'

# Define various thresholds and limits
MAX_RETRIES = 5
TIMEOUT_SECONDS = 30

# Minimum and maximum values for numeric inputs
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 20
MIN_PASSWORD_LENGTH = 8

# Commonly used statuses
STATUS_SUCCESS = 'success'
STATUS_FAILURE = 'failure'

# File paths
LOG_FILE_PATH = '/var/log/app.log'
CONFIG_FILE_PATH = '/etc/app/config.json'

# Roles within the application
ROLE_ADMIN = 'admin'
ROLE_USER = 'user'
ROLE_GUEST = 'guest'