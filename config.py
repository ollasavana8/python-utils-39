import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """A simple configuration loader that supports defaults, file loading, and environment variables."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        # Initialize with defaults
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_json(self, filepath: str) -> None:
        """Load configuration from a JSON file, overriding defaults."""
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                self._config.update(file_config)
        # No error if file missing, just use defaults

    def load_from_env(self, prefix: str = "CONFIG_") -> None:
        """Load configuration from environment variables with given prefix."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                # Try to convert to int or bool if possible
                if value.lower() in ("true", "false"):
                    self._config[config_key] = value.lower() == "true"
                else:
                    try:
                        self._config[config_key] = int(value)
                    except ValueError:
                        self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value, falling back to provided default."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a config value."""
        self._config[key] = value

    def get_all(self) -> Dict[str, Any]:
        """Return a copy of all configuration values."""
        return self._config.copy()

# Example usage at the end for testing
if __name__ == "__main__":
    defaults = {
        "debug": False,
        "port": 8000,
        "host": "0.0.0.0",
        "log_level": "INFO"
    }
    config = ConfigLoader(defaults)
    # Load from file if exists (example)
    config.load_from_json("app_config.json")
    # Load from env, e.g. CONFIG_PORT=9000
    config.load_from_env()
    print("Debug mode:", config.get("debug"))
    print("Port:", config.get("port"))
    print("All config:", config.get_all())
