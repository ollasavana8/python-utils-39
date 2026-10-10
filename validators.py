class ValidationError(Exception):
    """Custom exception for data validation failures."""
    pass

def validate_input(data):
    """Ensures input is a non-empty dictionary with expected keys."""
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict, got {type(data).__name__}")
    
    if 'id' not in data or 'payload' not in data:
        raise ValidationError("Missing required fields: 'id' and 'payload'")
    
    if not isinstance(data['id'], int):
        raise ValidationError("Field 'id' must be an integer")

def process_stream(input_data):
    """
    Main processing loop with integrated input validation.
    Handles data streams and logs validation outcomes.
    """
    results = []
    for item in input_data:
        try:
            validate_input(item)
            # Perform business logic processing
            processed = f"PROCESSED_{item['id']}"
            results.append(processed)
        except ValidationError as e:
            print(f"Validation error for item {item}: {e}")
            continue
        except Exception as e:
            print(f"Unexpected error during processing: {e}")
            continue
    return results