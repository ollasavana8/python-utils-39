import logging

# Configure basic logging for the processor
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary containing integer keys."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not data:
        raise ValueError("Input dictionary cannot be empty")
    for key, value in data.items():
        if not isinstance(key, int):
            raise TypeError(f"Key {key} must be an integer")
    return True

def process_data_stream(stream):
    """Main loop for processing incoming data batches."""
    for batch in stream:
        try:
            if validate_input(batch):
                # Simulate processing logic
                result = {k: v * 2 for k, v in batch.items()}
                logger.info(f"Processed batch with {len(result)} items")
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid batch encountered: {e}")
            continue
        except Exception as e:
            logger.critical(f"Unexpected failure: {e}")
            break

if __name__ == "__main__":
    test_stream = [{1: 10, 2: 20}, {1: 5}, "invalid", {3: 30}]
    process_data_stream(test_stream)