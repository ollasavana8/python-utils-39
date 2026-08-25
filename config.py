import os
import json
from typing import Any, Dict, Optional

class Config:
    """Configuration manager for loading and accessing settings."""

    def __init__(self, initial_config: Optional[Dict[str, Any]] = None) -> None:
        """Create config instance.

        Args:
            initial_config: Optional starting configuration dict.
        """
        self._data: Dict[str, Any] = initial_config or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve config value.

        Args:
            key: The setting name.
            default: Returned if key not present.

        Returns:
            Configuration value.
        """
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Update a config setting.

        Args:
            key: Setting name.
            value: New value.
        """
        self._data[key] = value

    def load_from_json(self, filepath: str) -> None:
        """Load configuration from JSON file.

        Args:
            filepath: Full path to the file.
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            loaded_data: Dict[str, Any] = json.load(f)
            self._data.update(loaded_data)

    def load_from_env(self, prefix: str = 'CONFIG_') -> None:
        """Import environment variables as config.

        Args:
            prefix: Filter for relevant variables.
        """
        for env_key, env_val in os.environ.items():
            if env_key.startswith(prefix):
                cfg_key: str = env_key[len(prefix):].lower()
                self._data[cfg_key] = env_val

    def to_dict(self) -> Dict[str, Any]:
        """Get all settings as dict.

        Returns:
            Copy of internal data.
        """
        return self._data.copy()

# Moderate comment: This provides a simple yet practical config utility
def create_config(initial: Optional[Dict[str, Any]] = None) -> Config:
    """Create and return a Config object.

    Args:
        initial: Starting values.

    Returns:
        Initialized Config.
    """
    return Config(initial)
