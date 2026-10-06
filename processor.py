import logging
from typing import Any, List, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Utility class for processing collections of data."""

    def __init__(self, debug: bool = False):
        self.debug = debug

    def clean_data(self, items: List[Any]) -> List[Any]:
        """Removes null entries from a provided list."""
        if not isinstance(items, list):
            raise ValueError("Input must be a list")
        
        cleaned = [item for item in items if item is not None]
        
        if self.debug:
            logger.debug(f"Processed {len(items)} items, kept {len(cleaned)}")
            
        return cleaned

    def batch_process(self, data: List[Any], chunk_size: int = 10) -> List[List[Any]]:
        """Splits data into smaller chunks for processing."""
        if chunk_size <= 0:
            raise ValueError("Chunk size must be positive")
            
        return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    def validate_and_transform(self, data: List[Any], transform_func: callable) -> List[Any]:
        """Applies transformation function to valid list items."""
        results = []
        for item in data:
            try:
                if item is not None:
                    results.append(transform_func(item))
            except Exception as e:
                logger.error(f"Transformation failed for item {item}: {e}")
        return results