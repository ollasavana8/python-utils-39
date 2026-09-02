import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """A configuration loader that merges file data with defaults."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize with optional defaults dictionary."""
        self.defaults: Dict[str, Any] = defaults or {}
        self.config: Dict[str, Any] = {}

    def load_from_file(self, filepath: str) -> None:
        """Load configuration from a JSON file, falling back to defaults."""
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if isinstance(data, dict):
                        self.config.update(data)
            except (json.JSONDecodeError, IOError, OSError):
                pass  # Ignore errors, use defaults
        self._merge_defaults()

    def _merge_defaults(self) -> None:
        """Merge defaults into config for missing keys."""
        for key, value in self.defaults.items():
            if key not in self.config:
                self.config[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value by key, using provided default if missing."""
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        self.config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the current configuration."""
        return self.config.copy()

    def save_to_file(self, filepath: str) -> None:
        """Save current config to a JSON file."""
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(self.config, file, indent=2)
        except (IOError, OSError):
            pass  # Silently fail on save errors
