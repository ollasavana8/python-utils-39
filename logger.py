import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a standardized logger instance.

    Args:
        name: The name of the logger.
        level: The logging threshold, defaults to INFO.

    Returns:
        A configured logging.Logger object.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

def log_message(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Utility for logging messages with dynamic levels.

    Args:
        logger: The logger instance to use.
        message: The text string to log.
        level: The severity level string.
    """
    levels: dict = {
        "debug": logger.debug,
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)