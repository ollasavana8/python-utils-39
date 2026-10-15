import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles data transformation with safety checks."""

    def process_input(self, data: Any) -> Optional[dict]:
        try:
            if not isinstance(data, dict):
                raise ValueError(f"Expected dict, got {type(data).__name__}")
            
            if not data:
                logger.warning("Empty data payload received")
                return None
                
            # Simulate processing logic
            result = {"status": "success", "payload": data}
            return result
            
        except ValueError as ve:
            logger.error(f"Validation error: {ve}")
            return None
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}", exc_info=True)
            return None

    def batch_process(self, items: list) -> list:
        if not isinstance(items, list):
            return []
        
        results = []
        for item in items:
            processed = self.process_input(item)
            if processed:
                results.append(processed)
        return results