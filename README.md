# python-utils-39

A collection of lightweight, high-performance utility functions designed to streamline repetitive tasks in Python 3.9+ projects. This library focuses on type-hinted, dependency-free code to keep your production environment lean and efficient.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## Features

*   **Data Validation Helpers**: Pre-built decorators and functions for rapid schema validation without the overhead of heavy frameworks like Pydantic.
*   **File System Traversals**: Optimized context managers for recursive directory walking and batch file renaming.
*   **Performance Decorators**: Built-in `@timeit` and `@memoize` wrappers to instantly profile or cache resource-intensive function calls.
*   **String Sanitization**: Robust utility suite for slugifying, normalizing, and stripping sensitive data from user inputs.

## Installation

Install the package directly from PyPI using pip:

```bash
pip install python-utils-39
```

Alternatively, if you are working within a virtual environment, ensure your requirements file is updated:

```bash
echo "python-utils-39>=1.0.0" >> requirements.txt
pip install -r requirements.txt
```

## Basic Usage

Quickly profile your functions or handle complex path operations with minimal boilerplate:

```python
from pyutils39.decorators import timeit
from pyutils39.fs import ensure_dir

# Automatically profile function execution time
@timeit
def process_data(data):
    return [d * 2 for d in data]

# Safely create nested directories if they don't exist
ensure_dir("./logs/2023/october")

data = process_data([1, 2, 3, 4, 5])
```

## License

Distributed under the MIT License. See `LICENSE` for more information.