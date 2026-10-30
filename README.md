# python-utils-39

A collection of lightweight, high-performance utility functions designed to streamline daily Python development. This library reduces boilerplate code for common file operations, string manipulation, and system-level tasks.

## Features

*   **File Streamliner:** Simplified decorators and context managers for atomic file writes and recursive directory scanning.
*   **Data Normalization:** Robust helper functions to clean, validate, and transform nested dictionaries and lists.
*   **System Helpers:** Cross-platform wrappers for executing shell commands with real-time timeout and logging capabilities.
*   **Format Converters:** Built-in tools for seamless conversion between JSON, YAML, and CSV formats with custom schema support.

## Installation

Install `python-utils-39` via pip:

```bash
pip install python-utils-39
```

Or, add it to your `requirements.txt`:

```text
python-utils-39>=1.0.0
```

## Basic Usage

Quickly manage file I/O and perform data normalization using the core utilities:

```python
from pyutils39 import file_io, data_tools

# Efficiently read and transform nested data
raw_data = {"user": {"id": 123, "meta": None}}
clean_data = data_tools.strip_nulls(raw_data)

# Safe atomic writing
file_io.safe_write("config.json", clean_data, format="json")

print(f"Processed: {clean_data}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request for any bug fixes or improvements to existing utility modules. Ensure all new features include unit tests in the `/tests` directory.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.