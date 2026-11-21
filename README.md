# python-utils-39

A collection of lightweight, high-performance utility functions designed to streamline daily Python development tasks. This library focuses on reducing boilerplate code for common file operations, data manipulation, and logging routines.

## Features

*   **Robust File Operations:** Simplified wrappers for directory traversal and atomic file writes.
*   **Data Serialization:** Helper methods for rapid conversion between nested dictionaries, JSON, and YAML formats.
*   **Enhanced Logging:** Pre-configured handlers for instant console and rotating file output with color-coded levels.
*   **Concurrency Helpers:** Decorators for quick thread-pool execution and asynchronous timeout management.

## Installation

Install the package directly from PyPI using `pip`:

```bash
pip install python-utils-39
```

Or, if you are working within a virtual environment using `poetry`:

```bash
poetry add python-utils-39
```

## Usage

Below is a quick example of how to utilize the custom logger and the atomic file writer provided by the package:

```python
from pyutils39.logger import get_logger
from pyutils39.file_io import write_atomic

# Initialize logger
log = get_logger("app_module")
log.info("Process starting...")

# Safely write data to disk
data = {"status": "success", "id": 101}
write_atomic("config.json", data, format="json")

log.info("Data written successfully.")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue to discuss proposed changes or submit a pull request with unit tests covering your modifications.