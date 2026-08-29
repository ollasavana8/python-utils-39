import json
from typing import Any, Callable, Dict, List, Optional, Union

def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Safely divide two numbers.

    Returns None if the denominator is zero to avoid errors.
    """
    if b == 0:
        return None
    return a / b

def parse_json_safe(json_str: str) -> Optional[Dict[str, Any]]:
    """Attempt to parse a string as JSON.

    Returns the dict if successful and it's a dict, else None.
    """
    try:
        parsed = json.loads(json_str)
        return parsed if isinstance(parsed, dict) else None
    except (json.JSONDecodeError, TypeError, ValueError):
        return None

def apply_filter(items: List[Any], condition: Callable[[Any], bool]) -> List[Any]:
    """Filter a list using the provided condition function.

    Only items where condition returns True are included.
    """
    return [item for item in items if condition(item)]

class DataHandler:
    """Handles storage, retrieval, and transformation of key-value data."""

    def __init__(self, data: Optional[Dict[str, Any]] = None) -> None:
        """Create a new handler, optionally with initial data."""
        self._data: Dict[str, Any] = data or {}

    def set_value(self, key: str, value: Any) -> None:
        """Store a value under the specified key."""
        self._data[key] = value

    def get_value(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve value for key or return default if absent."""
        return self._data.get(key, default)

    def transform_values(self, func: Callable[[Any], Any]) -> Dict[str, Any]:
        """Apply func to every value and return the new dict."""
        return {key: func(val) for key, val in self._data.items()}

    def export_json(self) -> str:
        """Return the data as a JSON formatted string."""
        return json.dumps(self._data, indent=2)

def create_sample_handler() -> DataHandler:
    """Create and populate a sample DataHandler for testing."""
    handler = DataHandler()
    handler.set_value("id", 123)
    handler.set_value("name", "test")
    handler.set_value("score", 95.5)
    return handler

if __name__ == "__main__":
    # Demo the functionality
    h = create_sample_handler()
    print(h.get_value("name"))
    print(h.transform_values(lambda x: str(x).upper()))
    print(safe_divide(20, 4))
    print(parse_json_safe('{"a": 1}'))
    print(apply_filter([1,2,3,4], lambda x: x > 2))