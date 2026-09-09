import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a logger instance with robust error handling."""
    logger = logging.getLogger(name)
    
    try:
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(level)
    except (OSError, ValueError) as e:
        # Fallback to null handler if stream is unavailable
        logger.addHandler(logging.NullHandler())
        print(f"Critical failure initializing logger: {e}", file=sys.stderr)
        
    return logger

def log_safe(logger: logging.Logger, level: int, message: str, exc_info: bool = False) -> None:
    """Ensures log operations do not crash the application."""
    try:
        if logger and callable(getattr(logger, 'log', None)):
            logger.log(level, message, exc_info=exc_info)
    except Exception:
        # Silence logger errors to prevent cascading application failures
        pass

# Default instance for quick access
app_logger = setup_logger('python-utils-39')