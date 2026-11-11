import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Loads and manages application configuration with default fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Merge custom dictionary into current configuration."""
        self._config = self._deep_update(self._config, data)

    def load_from_json(self, filepath: str) -> None:
        """Load configuration settings from a JSON file."""
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.load_from_dict(data)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve configuration value by key supporting dot notation."""
        keys = key.split(".")
        value = self._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def _deep_update(self, base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively update nested dictionaries."""
        result = base.copy()
        for key, val in update.items():
            if isinstance(val, dict) and key in result and isinstance(result[key], dict):
                result[key] = self._deep_update(result[key], val)
            else:
                result[key] = val
        return result

    @property
    def config(self) -> Dict[str, Any]:
        """Return copy of whole configuration dict."""
        return self._config.copy()
