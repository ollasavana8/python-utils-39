[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-39

`python-utils-39` is a lightweight, zero-dependency utility toolkit designed to streamline common Python 3.9+ development patterns. It provides optimized helpers for data manipulation, thread-safe caching, and resilient asynchronous task execution.

## Features

- **Thread-Safe Caching:** In-memory LRU cache decorator featuring automatic TTL expiration and thread safety.
- **Enhanced File I/O:** Atomic file writing and stream parsing for large JSON and YAML payloads to prevent data corruption.
- **Async Retry Decorator:** Configurable retry handler supporting exponential backoff, custom exception filtering, and event logging.
- **Dict Deep-Merge:** Recursive dictionary merging utility that gracefully handles nested lists and set combinations without mutating source objects.

## Installation

Install the package directly via `pip`:

```bash
pip install python-utils-39
```

Or install from the repository source:

```bash
git clone https://github.com/Developer/python-utils-39.git
cd python-utils-39
pip install .
```

## Basic Usage

Here is a quick example demonstrating dictionary deep merging and TTL caching:

```python
import time
from python_utils_39.cache import ttl_cache
from python_utils_39.dict_utils import deep_merge

# 1. Thread-safe TTL Cache Example
@ttl_cache(ttl_seconds=300, maxsize=128)
def fetch_user_permissions(user_id: int) -> dict:
    # Simulating an expensive database call
    return {"user_id": user_id, "roles": ["admin", "developer"]}

# 2. Deep Dictionary Merge Example
base_config = {"db": {"host": "localhost", "port": 5432}, "debug": False}
env_override = {"db": {"port": 5433}, "debug": True}

merged_config = deep_merge(base_config, env_override)

print(merged_config)
# Output: {'db': {'host': 'localhost', 'port': 5433}, 'debug': True}

permissions = fetch_user_permissions(42)
print(permissions)
# Output: {'user_id': 42, 'roles': ['admin', 'developer']}
```

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.