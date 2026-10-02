import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Configuration manager providing defaults, file parsing, and env overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._defaults: Dict[str, Any] = defaults or {}
        self._config: Dict[str, Any] = self._defaults.copy()

    def load_dict(self, data: Dict[str, Any]) -> None:
        """Merge custom dictionary values into active config."""
        self._config.update(data)

    def load_json(self, filepath: Union[str, Path]) -> None:
        """Load configuration options from a JSON file."""
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError(f"Configuration file not found: {path}")

        with open(path, "r", encoding="utf-8") as file:
            content = json.load(file)
            if isinstance(content, dict):
                self._config.update(content)
            else:
                raise ValueError("JSON config root must be an object")

    def load_env(self, prefix: str = "APP_") -> None:
        """Override options using environment variables with specified prefix."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix) :].lower()
                self._config[config_key] = value

    def get(self, key: str, fallback: Any = None) -> Any:
        """Fetch a configuration value with fallback support."""
        return self._config.get(key, fallback)

    def as_dict(self) -> Dict[str, Any]:
        """Return a copy of the final merged configuration."""
        return self._config.copy()
