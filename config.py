import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with provided default values."""
    config = defaults.copy()

    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def get_env_or_config(key: str, config: Dict[str, Any], env_prefix: str = "APP_") -> Any:
    """Prioritizes environment variables over configuration dicts."""
    env_val = os.getenv(f"{env_prefix}{key.upper()}")
    if env_val is not None:
        return env_val
    return config.get(key)

if __name__ == "__main__":
    defaults = {"host": "localhost", "port": 8080, "debug": False}
    app_config = load_config("config.json", defaults)
    print(f"Loaded config: {app_config}")