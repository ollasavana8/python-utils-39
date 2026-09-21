import functools
import logging

class ConfigCache:
    """Thread-safe singleton for high-frequency configuration access."""
    _instance = None
    _cache = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigCache, cls).__new__(cls)
        return cls._instance

    @functools.lru_cache(maxsize=128)
    def get_setting(self, key: str, default: any = None):
        """Retrieve setting with lru_cache for performance optimization."""
        return self._cache.get(key, default)

    def update_settings(self, new_data: dict):
        """Bulk update of configuration parameters."""
        self._cache.update(new_data)
        self.get_setting.cache_clear()

def get_optimized_config(key: str, default: any = None):
    """Module-level access to cached configuration settings."""
    try:
        return ConfigCache().get_setting(key, default)
    except Exception as e:
        logging.error(f"Configuration retrieval error: {e}")
        return default

# Pre-initialize global instance for performance
config_instance = ConfigCache()