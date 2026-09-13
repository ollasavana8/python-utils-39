from typing import Any, Dict, List, Generator

def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    '''Recursively merges dict2 into dict1.'''
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def nested_get(dictionary: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    '''Safely retrieves a value from a nested dictionary using a list of keys.'''
    current = dictionary
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def chunk_list(lst: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    '''Yields successive n-sized chunks from a list.'''
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(lst), chunk_size):
        yield lst[i : i + chunk_size]