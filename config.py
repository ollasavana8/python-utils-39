import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        default_config = self.load_json(self.default_config_path)
        user_config = self.load_json(self.user_config_path)

        # Override default configuration with user settings
        if user_config:
            default_config.update(user_config)
        return default_config

    def load_json(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    # Example usage
    loader = ConfigLoader('default_config.json', 'user_config.json')
    print(loader.get('some_setting', 'default_value'))