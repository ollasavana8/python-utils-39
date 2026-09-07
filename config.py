import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with fallback defaults."""

    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults

    def load(self, filepath: str) -> Dict[str, Any]:
        """Load config from file or return defaults if missing."""
        if not os.path.exists(filepath):
            return self.defaults

        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                return {**self.defaults, **data}
        except (json.JSONDecodeError, IOError):
            return self.defaults

def get_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Functional interface for configuration loading."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)

if __name__ == '__main__':
    # Example usage for demonstration
    default_settings = {"host": "localhost", "port": 8080}
    settings = get_config("config.json", default_settings)
    print(f"Loaded settings: {settings}")