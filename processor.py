import logging
from typing import Any, Optional, Dict

logger = logging.getLogger(__name__)

class DataProcessor:
    """Processes input dictionaries with robust error handling."""

    def __init__(self, schema: Optional[Dict[str, Any]] = None):
        self.schema = schema or {}

    def process(self, data: Any) -> Optional[Any]:
        """Validates and transforms data, handling structural edge cases."""
        try:
            if not isinstance(data, dict):
                raise ValueError(f"Expected dict, got {type(data).__name__}")
            
            if not data:
                logger.warning("Empty data payload received")
                return None

            # Simulate processing logic
            processed = {k: str(v).strip() for k, v in data.items()}
            return processed

        except (ValueError, TypeError) as e:
            logger.error(f"Data validation error: {e}")
            return None
        except Exception as e:
            logger.critical(f"Unexpected processing failure: {e}")
            return None

    def bulk_process(self, data_list: list) -> list:
        """Executes processing over a collection of items."""
        if not isinstance(data_list, list):
            return []
        
        results = []
        for item in data_list:
            result = self.process(item)
            if result is not None:
                results.append(result)
        return results