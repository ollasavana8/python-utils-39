import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any]):
        self._config = defaults.copy()

    def load_from_file(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                self._config.update(file_data)

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()

def get_config(filepath: str, defaults: Dict[str, Any]) -> ConfigLoader:
    loader = ConfigLoader(defaults)
    loader.load_from_file(filepath)
    return loader