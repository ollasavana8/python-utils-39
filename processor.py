from typing import List, Dict, Any


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process a list of dictionaries and return processed data.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries to process.

    Returns:
        List[Dict[str, Any]]: A list of processed dictionaries.
    """
    processed = []
    for item in data:
        processed_item = {key: value for key, value in item.items() if value is not None}
        processed.append(processed_item)
    return processed


def filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Filter data based on a key-value pair.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries to filter.
        key (str): The key to check in each dictionary.
        value (Any): The value that the key should match.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries that match the filter criteria.
    """
    return [item for item in data if item.get(key) == value]