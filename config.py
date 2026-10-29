import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with fallback to provided defaults."""
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            # Update defaults with values from file
            config.update(user_config)
    except (json.JSONDecodeError, IOError) as e:
        # Log error silently and return defaults in case of corruption
        print(f"Configuration load error: {e}")

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Configuration save error: {e}")