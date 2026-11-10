"""Data record processing module with strict input validation."""

from typing import Any, Dict, List, Optional, Tuple


class RecordProcessor:
    """Processes incoming data items after validating required fields and types."""

    def __init__(self, required_keys: Optional[List[str]] = None) -> None:
        self.required_keys = required_keys or ["id", "name", "payload"]
        self.processed_count = 0
        self.rejected_count = 0

    def validate_record(self, record: Any) -> Tuple[bool, str]:
        """Validate a single record structure and field constraints."""
        if not isinstance(record, dict):
            return False, "Record must be a dictionary"

        for key in self.required_keys:
            if key not in record:
                return False, f"Missing required field: '{key}'"

        if not isinstance(record["id"], (int, str)) or not str(record["id"]).strip():
            return False, "Field 'id' must be a non-empty string or integer"

        if not isinstance(record["name"], str) or not record["name"].strip():
            return False, "Field 'name' must be a non-empty string"

        return True, "Valid"

    def process_batch(self, items: List[Any]) -> List[Dict[str, Any]]:
        """Main processing loop with per-item validation."""
        valid_results = []

        for index, item in enumerate(items):
            is_valid, reason = self.validate_record(item)
            if not is_valid:
                self.rejected_count += 1
                continue

            processed_item = {
                "id": str(item["id"]),
                "name": item["name"].strip(),
                "payload": item["payload"],
                "status": "processed",
            }
            valid_results.append(processed_item)
            self.processed_count += 1

        return valid_results
