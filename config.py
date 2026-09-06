import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with fallback defaults."""

    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults

    def load(self, filepath: str) -> Dict[str, Any]:
        """Reads config file and merges with default values."""
        config = self.defaults.copy()
        
        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            # Returns defaults if file is corrupted or unreadable
            pass
            
        return config

# Example usage:
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080, 'debug': False}
    loader = ConfigLoader(defaults)
    current_config = loader.load('config.json')
    print(f"Active configuration: {current_config}")