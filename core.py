import json
from typing import Any, Dict, Union

class ConfigLoader:
    def __init__(self, default_config: Dict[str, Any]) -> None:
        self.default_config = default_config
        self.config = default_config.copy()

    def load(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as config_file:
                file_config = json.load(config_file)
                self._update_config(file_config)
        except FileNotFoundError:
            print(f'Config file not found: {file_path}')
        except json.JSONDecodeError:
            print(f'Error decoding JSON from: {file_path}')

    def _update_config(self, file_config: Dict[str, Any]) -> None:
        self.config.update({k: v for k, v in file_config.items() if v is not None})

    def get(self, key: str) -> Union[Any, None]:
        return self.config.get(key, None)

# Example usage
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080, 'debug': False}
    loader = ConfigLoader(defaults)
    loader.load('config.json')
    print(loader.config)  # Outputs the merged configuration
