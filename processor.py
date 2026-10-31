"""Batch data processor with built-in input validation."""

import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Raised when input item fails schema or domain validation."""
    pass


def validate_item(item: Any) -> Dict[str, Any]:
    """Validate item structure and data types before processing."""
    if not isinstance(item, dict):
        raise ValidationError(f"Expected dict, got {type(item).__name__}")

    if "id" not in item or item["id"] is None:
        raise ValidationError("Missing required field: 'id'")

    if "payload" in item and not isinstance(item["payload"], (str, dict, list)):
        raise ValidationError(f"Invalid payload type: {type(item['payload']).__name__}")

    return item


def process_records(
    records: List[Any], allow_failures: bool = True
) -> Tuple[List[Dict[str, Any]], List[Dict[str, str]]]:
    """Main processing loop with input validation for incoming batch items."""
    processed_results: List[Dict[str, Any]] = []
    errors: List[Dict[str, str]] = []

    for idx, raw_record in enumerate(records):
        try:
            validated = validate_item(raw_record)
            result = {
                "id": validated["id"],
                "status": "completed",
                "size": len(str(validated.get("payload", ""))),
            }
            processed_results.append(result)
        except ValidationError as err:
            err_msg = f"Record at index {idx} failed validation: {err}"
            logger.warning(err_msg)
            errors.append({"index": str(idx), "error": str(err)})
            if not allow_failures:
                raise ValidationError(err_msg) from err

    return processed_results, errors
