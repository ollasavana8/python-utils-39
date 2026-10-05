import os
import logging
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('python-utils-39')

class DataProcessor:
    """Handles core data transformation and cleanup tasks."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}

    def clean_env(self, prefix: str = "TMP_") -> None:
        """Removes environment variables matching prefix."""
        keys_to_remove = [k for k in os.environ if k.startswith(prefix)]
        for key in keys_to_remove:
            del os.environ[key]
            logger.debug(f"Removed env var: {key}")

    def reorganize_payload(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Flattens dictionary structure for easier parsing."""
        output = {}
        for key, value in data.items():
            if isinstance(value, dict):
                for sub_key, sub_val in value.items():
                    output[f"{key}_{sub_key}"] = sub_val
            else:
                output[key] = value
        return output

    @staticmethod
    def validate_path(path: str) -> bool:
        """Ensures path exists and is accessible."""
        return os.path.exists(path) and os.access(path, os.R_OK)