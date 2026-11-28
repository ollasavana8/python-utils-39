from typing import List, Dict, Any, Optional

class DataProcessor:
    """Handles batch processing of dictionary datasets with validation."""

    def __init__(self, target_key: str) -> None:
        self.target_key: str = target_key

    def extract_values(self, data: List[Dict[str, Any]]) -> List[Any]:
        """
        Extracts values associated with the target key from a list of dicts.

        Args:
            data: A list of dictionaries to process.

        Returns:
            A list of values matching the target key.
        """
        return [item[self.target_key] for item in data if self.target_key in item]

    def filter_by_threshold(self, data: List[Dict[str, Any]], threshold: float) -> List[Dict[str, Any]]:
        """
        Filters items where the target key value exceeds a numeric threshold.

        Args:
            data: The dataset to filter.
            threshold: The minimum value required for inclusion.

        Returns:
            Filtered list of dictionaries.
        """
        return [item for item in data if item.get(self.target_key, 0) >= threshold]

    def summarize(self, data: List[Dict[str, Any]]) -> Optional[Dict[str, float]]:
        """
        Calculates the mean value of the target key.

        Returns:
            Dictionary with the average or None if dataset is empty.
        """
        values = [item[self.target_key] for item in data if isinstance(item.get(self.target_key), (int, float))]
        if not values:
            return None
        return {"average": sum(values) / len(values)}