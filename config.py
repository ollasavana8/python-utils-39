import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with defaults."""

    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load(self, file_path: str) -> Dict[str, Any]:
        """Loads JSON file and merges with internal defaults."""
        if not os.path.exists(file_path):
            return self.config

        try:
            with open(file_path, 'r') as f:
                user_config = json.load(f)
                return {**self.config, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a value from the current configuration."""
        return self.config.get(key, default)

def get_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Helper function for quick configuration initialization."""
    loader = ConfigLoader(defaults)
    return loader.load(path)