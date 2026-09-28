# python-utils-39

A collection of lightweight, high-performance utility functions designed to streamline repetitive tasks in Python 3.9+ projects. This library focuses on type-hinted, dependency-free helpers for data manipulation, file I/O, and system introspection.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## Features

*   **Robust File Handling:** Simplified context managers for safe atomic file writes and recursive directory synchronization.
*   **Data Transformation:** Efficient batch processing utilities for nested dictionary flattening and type-safe schema validation.
*   **System Diagnostics:** Easy-to-use wrappers for measuring function execution time, memory footprint, and CPU utilization.
*   **Object Helpers:** Fluent interface for deep-merging dictionaries and safe attribute access for complex configuration objects.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-39
```

Or add it to your `requirements.txt` file:

```text
python-utils-39>=1.0.0
```

## Usage

Easily integrate the utilities into your existing workflow with minimal overhead:

```python
from pyutils import FileSystem, Timer

# Safely write data to a file
FileSystem.write_json("config.json", {"debug": True, "version": 1.2})

# Profile a function execution
with Timer("Data Processing"):
    # Perform intensive calculations
    result = [x**2 for x in range(1000000)]
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.