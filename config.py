import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.user_config = {}

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.user_config = json.load(file)
        except FileNotFoundError:
            print(f"Configuration file not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the configuration file.")

    def get_config(self):
        # Merge user config with defaults, user config takes precedence
        config = self.default_config.copy()
        config.update(self.user_config)
        return config

# Example default configuration
if __name__ == '__main__':
    default_config = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    config_loader = ConfigLoader(default_config)
    config_loader.load_from_file('config.json')
    final_config = config_loader.get_config()
    print(final_config)  # Should print the merged configuration
