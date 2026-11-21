import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a standard logger with basic error handling."""
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        try:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(level)
        except (OSError, ValueError) as e:
            # Fallback to stderr if stdout is unreachable or invalid
            sys.stderr.write(f"Failed to initialize logger {name}: {e}\n")
            
    return logger

def safe_log(logger: logging.Logger, message: str, level: int = logging.INFO) -> None:
    """Logs messages safely without raising exceptions."""
    try:
        if not isinstance(message, str):
            message = str(message)
        logger.log(level, message)
    except Exception as e:
        # Silence unexpected logging errors in production environments
        sys.stderr.write(f"Logging failure: {e}\n")

if __name__ == '__main__':
    log = get_logger('python-utils-39')
    safe_log(log, 'Logger initialized successfully')
    safe_log(log, None) # Edge case: non-string input handling