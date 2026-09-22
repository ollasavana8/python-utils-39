import logging
import sys
from typing import Optional

def setup_logger(name: str, log_file: Optional[str] = None, level: str = 'INFO') -> logging.Logger:
    '''Configures and returns a standardized logger with console and optional file output.'''
    logger = logging.getLogger(name)

    # Prevent adding handlers multiple times
    if logger.hasHandlers():
        return logger

    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(numeric_level)

    # Standard stream handler for console output
    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Optional file logger configuration
    if log_file:
        try:
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
        except OSError as e:
            logger.error(f'Failed to initialize file log handler: {e}')

    return logger