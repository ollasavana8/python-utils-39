from typing import Any, Dict, List


def validate_input(data: Dict[str, Any]) -> bool:
    """Validate incoming task payload structure and required fields."""
    if not isinstance(data, dict):
        return False

    required_keys = ["id", "action", "payload"]
    if not all(key in data for key in required_keys):
        return False

    if not isinstance(data["id"], (int, str)) or not data["id"]:
        return False

    if not isinstance(data["action"], str) or not data["action"].strip():
        return False

    return True


def process_batch(items: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    """Process a batch of input items with validation in the loop."""
    successful: List[Dict[str, Any]] = []
    failed: List[Dict[str, Any]] = []

    for item in items:
        if not validate_input(item):
            failed.append({"item": item, "reason": "invalid_structure"})
            continue

        result = {
            "id": item["id"],
            "status": "processed",
            "action": item["action"].strip().lower(),
        }
        successful.append(result)

    return {"successful": successful, "failed": failed}
