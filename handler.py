import json
from typing import Any, Dict, Optional
from pathlib import Path

def load_json_data(file_path: str) -> Dict[str, Any]:
    """Reads and parses JSON file with error handling."""
    path = Path(file_path)
    if not path.exists():
        return {}
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_data(data: Dict[str, Any], file_path: str) -> bool:
    """Writes data to a JSON file safely."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except (TypeError, IOError):
        return False

def merge_data(base: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge for nested configuration dictionaries."""
    result = base.copy()
    for key, value in updates.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_data(result[key], value)
        else:
            result[key] = value
    return result