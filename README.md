# python-utils-39

A collection of lightweight, high-performance Python utilities designed to streamline common development tasks. This library focuses on efficiency and readability, providing drop-in solutions for data validation, file system operations, and task orchestration.

## Features

*   **Robust File Operations:** Advanced directory traversal and recursive file-type filtering with built-in concurrency support.
*   **Data Validation:** A decorator-based schema validator for function arguments to ensure type safety without complex boilerplate.
*   **Time-Series Logging:** Simplified rotating log handlers that automatically compress archived files to minimize disk footprint.
*   **Task Orchestrator:** A lightweight execution wrapper for managing async sub-processes with configurable timeout and retry logic.

## Installation

Install the package directly from PyPI using pip:

```bash
pip install python-utils-39
```

Alternatively, install from source:

```bash
git clone https://github.com/Developer/python-utils-39.git
cd python-utils-39
pip install .
```

## Basic Usage

Quickly validate function inputs or execute sub-processes with our core utilities:

```python
from pyutils import validate_args, run_task

# Validate function arguments using type hints
@validate_args
def process_data(value: int, label: str):
    print(f"Processing {label}: {value}")

# Execute a system command with a 5-second timeout
result = run_task(["ls", "-la"], timeout=5)
print(result.stdout)
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.