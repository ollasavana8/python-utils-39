import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a robust logger with basic error handling."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        try:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        except Exception as e:
            sys.stderr.write(f"critical failure initializing logger: {e}\n")
    
    return logger

def safe_log(logger: logging.Logger, message: str, level: int = logging.INFO) -> None:
    """Logs messages safely, handling potential encoding issues."""
    try:
        if not isinstance(message, str):
            message = str(message)
        logger.log(level, message)
    except (UnicodeEncodeError, AttributeError) as e:
        sys.stderr.write(f"failed to log message: {str(e)}\n")

def get_logger_context(name: Optional[str]) -> logging.Logger:
    """Returns default logger if name is invalid."""
    if not name or not isinstance(name, str):
        return setup_logger("default_logger")
    return setup_logger(name)