class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_data(data, required_keys):
    """Ensures input dictionary contains required keys and values are non-empty."""
    if not isinstance(data, dict):
        raise ValidationError("Input must be a dictionary")
    
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required field: {key}")
        if data[key] is None or (isinstance(data[key], str) and not data[key].strip()):
            raise ValidationError(f"Field '{key}' cannot be empty")

def process_main_loop(data_list, required_fields):
    """Processes data list with validation step."""
    processed_results = []
    for entry in data_list:
        try:
            validate_input_data(entry, required_fields)
            # Mock business logic execution
            processed_results.append(entry.get('id', 'unknown'))
        except ValidationError as e:
            print(f"Skipping invalid entry: {e}")
            continue
    return processed_results