import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with default values."""

    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults

    def load(self, filepath: str) -> Dict[str, Any]:
        """Reads JSON file and merges it with provided defaults."""
        config = self.defaults.copy()

        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

        return config

def get_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Helper function to instantiate and load config."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)