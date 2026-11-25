class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_payload(data: dict, required_keys: list):
    """Ensures dictionary contains all mandatory keys and non-empty values."""
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")
    
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
        if data[key] is None or data[key] == "":
            raise ValidationError(f"Key {key} cannot be empty")

def process_stream(items: list, schema: list):
    """Main loop processing with strict input validation."""
    results = []
    for item in items:
        try:
            validate_payload(item, schema)
            results.append(item['id'])
        except ValidationError as e:
            # Log validation failure and skip item
            continue
    return results