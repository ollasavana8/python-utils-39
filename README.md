# python-utils-39

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, zero-dependency collection of helper functions designed to streamline daily Python development tasks. This library simplifies common operations like nested dictionary manipulation, robust datetime parsing, and safe file operations.

## Features

* **Deep Dict Access**: Safely retrieve or set values in deeply nested dictionaries using dot-notation path keys.
* **Smart Datetime Parsing**: Automatically convert chaotic, multi-format string timestamps into timezone-aware datetime objects.
* **Atomic File Writing**: Prevent data corruption with safe write operations that use temporary files under the hood.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-39
```

## Quick Start

```python
from python_utils_39 import deep_get, safe_write, parse_datetime

# 1. Safely extract nested data
data = {"user": {"profile": {"email": "developer@example.com"}}}
email = deep_get(data, "user.profile.email")
print(email)  # Output: developer@example.com

# 2. Parse unpredictable timestamps
dt = parse_datetime("2023-10-27T15:30:00Z")
print(dt.tzinfo)  # Output: UTC

# 3. Perform an atomic file write
config_data = '{"theme": "dark", "volume": 80}'
safe_write("config.json", config_data)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.