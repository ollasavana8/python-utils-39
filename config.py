import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    Returns the merged configuration dictionary.
    """
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

if __name__ == '__main__':
    # Example usage
    default_settings = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    
    current_config = load_config('settings.json', default_settings)
    print(f"Active config: {current_config}")