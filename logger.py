import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: Optional[str] = "logs/app.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    fmt: Optional[str] = None,
) -> logging.Logger:
    """Configures and returns a logger instance with rotating file and stream handlers.

    Args:
        name: Logger identification name.
        log_file: Path to the log file. If None, only stream logging is enabled.
        level: Logging level (e.g., logging.INFO).
        max_bytes: Maximum size of log file before rotation (default: 5MB).
        backup_count: Number of rotated backup log files to retain.
        fmt: Custom log message formatting pattern.

    Returns:
        Configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers on repeated setup calls
    if logger.handlers:
        return logger

    log_format = fmt or "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # Console stream handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
