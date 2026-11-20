import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading configuration from JSON with fallback defaults."""

    def __init__(self, default_config: Dict[str, Any] = None):
        self.defaults = default_config or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Reads JSON file and merges with default settings."""
        if not os.path.exists(filepath):
            return self.defaults.copy()

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
            
            config = self.defaults.copy()
            config.update(file_data)
            return config
        except (json.JSONDecodeError, IOError):
            return self.defaults.copy()

if __name__ == "__main__":
    defaults = {"host": "localhost", "port": 8080, "debug": False}
    loader = ConfigLoader(defaults)
    current_config = loader.load("config.json")
    print(f"Active configuration: {current_config}")