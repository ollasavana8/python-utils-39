from typing import Any, Iterable, Dict, List, Optional

def batch_process(data: Iterable[Any], chunk_size: int = 100) -> List[List[Any]]:
    """Split data into smaller chunks for batch operations."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    
    data_list = list(data)
    return [data_list[i : i + chunk_size] for i in range(0, len(data_list), chunk_size)]

def extract_nested_key(data: Dict[str, Any], keys: str, delimiter: str = '.') -> Optional[Any]:
    """Retrieve value from nested dictionary using dot notation."""
    parts = keys.split(delimiter)
    current = data
    
    try:
        for part in parts:
            current = current[part]
        return current
    except (KeyError, TypeError):
        return None

def sanitize_payload(data: Dict[str, Any], allowed_keys: Iterable[str]) -> Dict[str, Any]:
    """Filter dictionary to include only permitted keys."""
    return {k: v for k, v in data.items() if k in allowed_keys}

if __name__ == "__main__":
    # Example usage for verification
    sample = {"user": {"profile": {"id": 123}}}
    print(extract_nested_key(sample, "user.profile.id"))