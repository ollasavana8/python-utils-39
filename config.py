import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading and merging configuration files."""

    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads json config and merges with defaults."""
        config = self.defaults.copy()

        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config: {e}")
            
        return config

def get_config(path: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    """Convenience function for configuration loading."""
    loader = ConfigLoader(defaults)
    return loader.load(path)