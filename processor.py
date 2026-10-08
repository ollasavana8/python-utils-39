import logging
from typing import Any, List, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles batch processing and data sanitization."""

    def __init__(self, settings: Optional[dict] = None):
        self.settings = settings or {}
        self.strict_mode = self.settings.get('strict', False)

    def sanitize(self, data: Any) -> Any:
        """Removes null entries from dictionaries."""
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return data

    def process_batch(self, items: List[Any]) -> List[Any]:
        """Applies sanitization to a collection of items."""
        results = []
        for item in items:
            try:
                cleaned = self.sanitize(item)
                results.append(cleaned)
            except Exception as e:
                logger.error(f"processing error: {e}")
                if self.strict_mode:
                    raise
        return results

    def format_output(self, data: List[Any]) -> str:
        """Serializes processed data to a string representation."""
        return " | ".join(map(str, data))
