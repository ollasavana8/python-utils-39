import logging
from logging.handlers import RotatingFileHandler
import os
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: Optional[str] = "logs/app.log",
    level: int = logging.INFO,
    max_bytes: int = 10_485_760,
    backup_count: int = 5,
    console: bool = True,
    fmt: Optional[str] = None,
) -> logging.Logger:
    """Configures and returns a custom logger with rotating file handler."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers when called multiple times
    if logger.handlers:
        return logger

    if fmt is None:
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)

    if console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
