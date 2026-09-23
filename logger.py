import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a standardized logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Standard output handler for logs
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

def log_data_summary(logger: logging.Logger, data: dict) -> None:
    """
    Logs a summary of dictionary data for debugging.
    """
    keys_count = len(data.keys())
    logger.info(f"Data processing initiated with {keys_count} keys")
    
    for key, value in data.items():
        logger.debug(f"Key: {key}, Type: {type(value).__name__}")

if __name__ == '__main__':
    # Example usage for verification
    test_logger = setup_logger('app_logger')
    test_logger.info("Logger initialization complete")
    log_data_summary(test_logger, {'id': 1, 'status': 'active'})