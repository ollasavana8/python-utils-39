# python-utils-39

A collection of lightweight, high-performance Python utilities designed to streamline daily development tasks. This library bridges common gaps in the standard library by providing robust helpers for data transformation, path manipulation, and logging.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Key Features

*   **Smart File Operations:** Simplifies recursive file searching and batch renaming with intuitive, chainable syntax.
*   **Data Validation Helpers:** Includes decorators to enforce strict type checking and schema validation for dictionary-based configurations.
*   **Time-Series Converters:** Streamlined utility functions for handling timezone-aware ISO strings and Unix timestamp conversions.
*   **Robust Logging Wrapper:** A pre-configured `log_utils` module that formats logs for cloud environments without external dependencies.

## Installation

Install the package via pip:

```bash
pip install python-utils-39
```

Or, if you are working within a poetry-managed environment:

```bash
poetry add python-utils-39
```

## Basic Usage

Import the necessary utility modules to enhance your script functionality immediately.

```python
from python_utils_39.files import find_files
from python_utils_39.logger import get_logger

# Initialize a structured logger
logger = get_logger("app_main")
logger.info("Starting file synchronization...")

# Search for all JSON files in the current directory
json_files = find_files(extension="json", recursive=True)

for file in json_files:
    logger.info(f"Processing: {file.name}")
```

## Contributing

We welcome contributions! Please open an issue to discuss proposed features or submit a pull request with unit tests included.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.