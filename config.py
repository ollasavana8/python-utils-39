import os
from typing import Any, Dict

class ConfigManager:
    """Handles application environment settings and defaults."""
    
    def __init__(self, prefix: str = "APP_"):
        self.prefix = prefix
        self.settings: Dict[str, Any] = {}

    def load_from_env(self) -> None:
        """Extracts prefixed variables from system environment."""
        for key, value in os.environ.items():
            if key.startswith(self.prefix):
                clean_key = key[len(self.prefix):].lower()
                self.settings[clean_key] = self.parse_value(value)

    @staticmethod
    def parse_value(value: str) -> Any:
        """Coerces string values into appropriate python types."""
        if value.lower() in ('true', 'yes', 'on'):
            return True
        if value.lower() in ('false', 'no', 'off'):
            return False
        try:
            return int(value)
        except ValueError:
            return value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves setting by key with fallback."""
        return self.settings.get(key, default)

# Initialize default instance
default_config = ConfigManager()
default_config.load_from_env()