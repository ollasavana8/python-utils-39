import json
import os
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Loads configuration settings with support for default fallback values."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.defaults: Dict[str, Any] = defaults or {}
        self._config: Dict[str, Any] = self.defaults.copy()

    def _deep_merge(self, base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively merge updated values into the base configuration."""
        merged = base.copy()
        for key, value in update.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = self._deep_merge(merged[key], value)
            else:
                merged[key] = value
        return merged

    def load_dict(self, config_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Load and merge configuration settings from a dictionary."""
        self._config = self._deep_merge(self.defaults, config_dict)
        return self._config

    def load_json(self, filepath: Union[str, os.PathLike]) -> Dict[str, Any]:
        """Load and merge configuration settings from a JSON file."""
        path = str(filepath)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Config file not found at path: {path}")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return self.load_dict(data)

    def get(self, key: str, fallback: Any = None) -> Any:
        """Retrieve a configuration value using dot notation for nested keys."""
        keys = key.split(".")
        val = self._config
        for k in keys:
            if isinstance(val, dict) and k in val:
                val = val[k]
            else:
                return fallback
        return val
