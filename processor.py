import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not data:
        raise ValueError("Input data cannot be empty")
    return True

def process_data_stream(stream):
    """
    Processes incoming data stream with validation
    for each record to ensure data integrity.
    """
    for record in stream:
        try:
            if validate_input(record):
                # Perform core processing logic here
                result = record.get("value", 0) * 2
                logger.info(f"Processed record with result: {result}")
        except (ValueError, TypeError) as e:
            logger.error(f"Skipping invalid record: {e}")
            continue

if __name__ == "__main__":
    # Example usage for verification
    sample_stream = [{"value": 10}, {}, "invalid_type", {"value": 5}]
    process_data_stream(sample_stream)