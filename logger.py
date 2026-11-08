import logging
from logging.handlers import RotatingFileHandler
import sys

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def get_logger(name: str, log_file: str = "app.log", level: int = logging.INFO) -> logging.Logger:
    """Configures a rotating file logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if get_logger is called multiple times
    if not logger.handlers:
        # Rotating file handler: 5MB max size, keep 3 backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5 * 1024 * 1024, backupCount=3
        )
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        
        # Console handler for development visibility
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger