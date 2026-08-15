class StatusCodes:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

class Messages:
    USER_CREATED = 'User created successfully'
    USER_UPDATED = 'User updated successfully'
    USER_DELETED = 'User deleted successfully'
    INVALID_INPUT = 'Invalid input provided'
    UNAUTHORIZED_ACCESS = 'Unauthorized access'

class Config:
    API_VERSION = 'v1'
    DATABASE_URI = 'sqlite:///mydb.db'
    SECRET_KEY = 'your-secret-key-here'

class Roles:
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'

