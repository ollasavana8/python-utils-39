import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with fallback to default values."""
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

def get_env_var(key: str, default: Any) -> Any:
    """Retrieves environment variable with type-safe default fallback."""
    val = os.getenv(key)
    if val is None:
        return default
    
    # Cast to type of default if possible
    try:
        return type(default)(val)
    except (ValueError, TypeError):
        return val

if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080, 'debug': False}
    current_config = load_config('settings.json', defaults)
    print(f'Loaded config: {current_config}')