import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults
        self.config = defaults.copy()

    def load_from_file(self, filepath: str) -> None:
        """Updates internal config with values from a JSON file."""
        if not os.path.exists(filepath):
            return
        
        try:
            with open(filepath, 'r') as f:
                user_data = json.load(f)
                self.config.update(user_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {filepath}: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves config value with fallback logic."""
        return self.config.get(key, default)

def load_app_config(path: str, defaults: Dict[str, Any]) -> ConfigLoader:
    """Factory function to instantiate and load config."""
    loader = ConfigLoader(defaults)
    loader.load_from_file(path)
    return loader