"""Configuration management module.

This module provides a Config class for handling application settings
with support for defaults, environment variables, and type safety.
"""

import os

from typing import Any, Dict, Optional

class Config:
    """A configuration manager that stores settings in a dictionary.

    Supports loading from environment variables and provides
    type-annotated methods for getting and setting values.
    """

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the configuration with optional default values.

        Args:
            defaults: A dictionary of default configuration values.
        """
        self._config: Dict[str, Any] = dict(defaults) if defaults is not None else {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a value from the configuration.

        Args:
            key: The key to look up in the configuration.
            default: The value to return if the key is not found.
        Returns:
            The value associated with the key or the default.
        """
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a value in the configuration.

        Args:
            key: The key to set.
            value: The value to associate with the key.
        """
        self._config[key] = value

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Load configuration values from environment variables.

        Only variables starting with the given prefix are loaded,
        and the prefix is stripped before storing.

        Args:
            prefix: The prefix for environment variables to consider.
        """
        for env_key, env_value in os.environ.items():
            if env_key.startswith(prefix):
                config_key = env_key[len(prefix):].lower()
                # Attempt basic type conversion for common values
                if env_value.lower() in ('true', 'false'):
                    self._config[config_key] = env_value.lower() == 'true'
                elif env_value.isdigit():
                    self._config[config_key] = int(env_value)
                else:
                    self._config[config_key] = env_value

    def update(self, updates: Dict[str, Any]) -> None:
        """Update multiple configuration values at once.

        Args:
            updates: A dictionary of key-value pairs to update.
        """
        self._config.update(updates)

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the current configuration as a dictionary.

        Returns:
            A shallow copy of the internal configuration dictionary.
        """
        return self._config.copy()