import logging
import sys
from typing import Optional

class DataLogger:
    """Utility for standardized application logging."""

    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Standard console handler
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, message: str, context: Optional[dict] = None) -> None:
        log_msg = f"{message} | context: {context}" if context else message
        self.logger.info(log_msg)

    def error(self, message: str, exc: Optional[Exception] = None) -> None:
        if exc:
            self.logger.error(f"{message}: {str(exc)}", exc_info=True)
        else:
            self.logger.error(message)

def get_logger(name: str) -> DataLogger:
    """Factory method for logger instances."""
    return DataLogger(name)