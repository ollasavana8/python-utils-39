import logging
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates and configures a standard logger instance.

    Args:
        name: The name of the logger instance.
        level: The logging threshold (e.g., logging.DEBUG).

    Returns:
        A configured logging.Logger object.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler: logging.StreamHandler = logging.StreamHandler()
        formatter: logging.Formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_message(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Utility for logging messages with specific levels.

    Args:
        logger: The logger instance to use.
        message: The text string to log.
        level: Severity level string.
    """
    levels: dict = {
        "debug": logger.debug,
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)