import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility to load JSON configurations with default values."""

    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load(self, file_path: str) -> Dict[str, Any]:
        """Reads JSON file and merges with existing defaults."""
        config = self.defaults.copy()
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass
        
        return config

    @staticmethod
    def save(file_path: str, data: Dict[str, Any]) -> None:
        """Persists dictionary to a JSON file."""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)