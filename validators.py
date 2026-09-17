import re
from typing import Any, Optional

def validate_input_schema(data: dict) -> bool:
    """Validates that input dictionary contains required keys and valid types."""
    required_fields = {"task_id": int, "payload": str}
    
    for field, expected_type in required_fields.items():
        if field not in data:
            return False
        if not isinstance(data[field], expected_type):
            return False
    return True

def sanitize_string(value: str) -> Optional[str]:
    """Removes malicious characters from input strings."""
    if not isinstance(value, str):
        return None
    # Allow only alphanumeric and underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '', value)
    return sanitized if sanitized else None

def process_validated_payload(data: dict) -> dict:
    """Main entry point for payload validation logic."""
    if not validate_input_schema(data):
        raise ValueError("Invalid schema format")
        
    clean_payload = sanitize_string(data['payload'])
    if not clean_payload:
        raise ValueError("Empty or invalid payload content")
        
    return {
        "task_id": data['task_id'],
        "payload": clean_payload,
        "status": "validated"
    }