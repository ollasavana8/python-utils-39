# python-utils-39

A collection of Python utility functions designed to enhance productivity and make scripting tasks easier. Whether you're working with data processing, file handling, or string manipulation, python-utils-39 streamlines common operations with minimal setup.

## Features
- **Data Processing Utilities**: Efficiently manipulate lists and dictionaries for quick data transformations without boilerplate code.
- **File Handling Functions**: Simplify read/write operations with robust methods that support various file formats, including JSON and CSV.
- **String Manipulation Tools**: Comprehensive functions to sanitize, format, and validate strings, perfect for preparing user inputs.
- **Customizable Logging**: Built-in logging mechanisms for easy tracking of application behavior during development and debugging.

## Installation

To install python-utils-39, simply clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/python-utils-39.git
cd python-utils-39
pip install -r requirements.txt
```

## Basic Usage Example

Here's a quick demonstration of how to utilize some of the features of python-utils-39:

```python
from utils import file_handler, string_utils

# Read a JSON file
data = file_handler.read_json('data.json')

# Sanitize a string
clean_string = string_utils.sanitize("   Hello, World!  ")

# Print results
print(clean_string)  # Output: "Hello, World!"
print(data)          # Output: Content of data.json
```

For more detailed examples and advanced usage, please refer to the [Wiki](https://github.com/yourusername/python-utils-39/wiki).

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)