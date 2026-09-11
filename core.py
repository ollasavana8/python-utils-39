from typing import Any, Dict, List, Optional, Callable

def batch_process(items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
    """
    Applies a function to a list of items and returns the results.

    Args:
        items: A list of arbitrary elements to process.
        func: A callable function to apply to each item.

    Returns:
        A list of processed items.
    """
    return [func(item) for item in items]

def merge_configs(base: Dict[str, Any], override: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merges an override dictionary into a base configuration dictionary.

    Args:
        base: The default configuration dictionary.
        override: An optional dictionary containing override values.

    Returns:
        A new dictionary with merged configuration values.
    """
    if not override:
        return base.copy()
    
    result = base.copy()
    result.update(override)
    return result

def get_safe(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """
    Retrieves a value from a dictionary safely.

    Args:
        data: The dictionary to search.
        key: The key to retrieve.
        default: The fallback value if key is missing.

    Returns:
        The value associated with the key or the default.
    """
    return data.get(key, default)