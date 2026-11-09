import os
from typing import Any, Dict

class ConfigManager:
    """Handles application configuration loading and access."""
    
    def __init__(self, defaults: Dict[str, Any] = None):
        self._settings = defaults or {}
        self._load_from_env()

    def _load_from_env(self) -> None:
        """Overwrites settings with environment variables if present."""
        for key in self._settings.keys():
            env_val = os.getenv(key.upper())
            if env_val is not None:
                self._settings[key] = self._parse_env_type(env_val)

    def _parse_env_type(self, value: str) -> Any:
        """Coerces environment string to correct data type."""
        if value.lower() in ('true', 'yes'): return True
        if value.lower() in ('false', 'no'): return False
        try:
            return int(value)
        except ValueError:
            return value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves config value by key."""
        return self._settings.get(key, default)

    def update(self, new_settings: Dict[str, Any]) -> None:
        """Merges new settings into existing configuration."""
        self._settings.update(new_settings)

# Global default configuration instance
default_config = ConfigManager({
    "debug": False,
    "log_level": "INFO",
    "max_retries": 3
})