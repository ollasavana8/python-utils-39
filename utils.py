import os
from typing import List, Dict, Any, Optional

def read_text_file(filepath: str, encoding: str = 'utf-8') -> str:
    """Read the entire content of a text file.
    Args:
        filepath: Path to the file to read.
        encoding: Encoding to use (default utf-8).
    Returns:
        The file content as a string.
    """
    with open(filepath, 'r', encoding=encoding) as file:
        return file.read()

def write_text_file(filepath: str, content: str, encoding: str = 'utf-8') -> None:
    """Write string content to a file.
    Parent dirs created if missing.
    Args:
        filepath: Path to write to.
        content: Text to write.
        encoding: Encoding (default utf-8).
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding=encoding) as file:
        file.write(content)

def merge_dicts(d1: Dict[str, Any], d2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge d1 and d2.
    d2 overrides d1 on conflicts.
    Args:
        d1: First dictionary.
        d2: Second dictionary.
    Returns:
        The merged dict.
    """
    result = d1.copy()
    for key, value in d2.items():
        # check for nested dict to recurse
        if (key in result and isinstance(result[key], dict) and isinstance(value, dict)):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def safe_divide(a: float, b: float) -> Optional[float]:
    """Perform division or return None if divisor is zero.
    Args:
        a: Dividend.
        b: Divisor.
    Returns:
        Result or None.
    """
    if b == 0:
        return None
    return a / b

def format_size(size_bytes: int) -> str:
    """Format bytes to readable size string.
    Args:
        size_bytes: Number of bytes.
    Returns:
        String like '2.0 MB'.
    """
    if size_bytes == 0:
        return '0 B'
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0
    # loop to find appropriate unit
    while size_bytes >= 1024 and i < len(units)-1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {units[i]}"