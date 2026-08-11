import json
from typing import Any, Dict


def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file and return it as a dictionary."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file {file_path} is not a valid JSON file.")


def save_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """Save a dictionary as JSON data to a file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise IOError(f"An error occurred while writing to the file {file_path}: {str(e)}")


def update_json_file(file_path: str, updates: Dict[str, Any]) -> None:
    """Load a JSON file, update it with new data, and save it back."""
    data = load_json_file(file_path)
    data.update(updates)
    save_json_file(file_path, data)
