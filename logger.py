import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a standard stream logger instance.

    Args:
        name: The name of the logger instance.
        level: The logging severity level, defaults to INFO.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_message(logger: logging.Logger, message: str, level: str = 'info') -> None:
    """
    Logs a message to the provided logger instance.

    Args:
        logger: The logger instance to use.
        message: The message string to log.
        level: The level name as a string (debug, info, warning, error).
    """
    levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)