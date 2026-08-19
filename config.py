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
        merged_config = {**default_config, **user_config}
        return merged_config

    def load_json(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json', 'user_config.json')
    some_setting = config_loader.get('some_setting', 'default_value')
    print(some_setting)