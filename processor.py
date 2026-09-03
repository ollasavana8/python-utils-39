import logging
from typing import Any, List, Dict

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles data normalization and cleanup tasks."""

    def __init__(self, settings: Dict[str, Any] = None):
        self.settings = settings or {}
        self.verbose = self.settings.get("verbose", False)

    def normalize_batch(self, data_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Cleans dictionary keys and strips whitespace values."""
        cleaned_data = []
        for entry in data_items:
            if not isinstance(entry, dict):
                continue
            
            processed = {
                str(k).strip().lower(): str(v).strip() if isinstance(v, str) else v
                for k, v in entry.items()
            }
            cleaned_data.append(processed)
        
        if self.verbose:
            logger.info(f"Processed {len(cleaned_data)} items")
        return cleaned_data

    def filter_nulls(self, data_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Removes entries containing empty values."""
        return [item for item in data_items if all(item.values())]

    def execute_pipeline(self, raw_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Orchestrates normalization and filtering sequence."""
        normalized = self.normalize_batch(raw_data)
        return self.filter_nulls(normalized)