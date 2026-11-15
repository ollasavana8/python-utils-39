import logging
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates and configures a standard stream logger.

    Args:
        name: Name of the logger instance.
        level: Logging threshold level.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_message(logger: logging.Logger, message: str, level: str = 'info') -> None:
    """
    Logs a message at the specified level.

    Args:
        logger: The logger instance to use.
        message: Text content to record.
        level: Severity level string.
    """
    log_map = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error
    }
    
    log_func = log_map.get(level.lower(), logger.info)
    log_func(message)