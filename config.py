import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Load configuration from JSON file with fallback defaults."""
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

def get_env_config(prefix: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Override configuration values using environment variables."""
    config = defaults.copy()
    for key in config.keys():
        env_key = f"{prefix}_{key.upper()}"
        value = os.environ.get(env_key)
        if value is not None:
            config[key] = type(config[key])(value)
    return config