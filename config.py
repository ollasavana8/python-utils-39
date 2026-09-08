import os
import json
from typing import Any, Dict, Optional


class ConfigManager:
    """Utility class to manage application configurations from files and environment variables."""

    def __init__(self, default_config: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = default_config or {}

    def load_from_json(self, filepath: str) -> None:
        """Load configuration key-values from a JSON file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Config file not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                self._config.update(data)
            else:
                raise ValueError("JSON config root must be a dictionary")

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Load environment variables starting with a specific prefix."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set or update a configuration key."""
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the current configuration dictionary."""
        return self._config.copy()
