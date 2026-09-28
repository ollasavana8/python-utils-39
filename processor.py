import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures data is a non-empty dictionary."""
    if not isinstance(data, dict) or not data:
        raise ValueError("Invalid input: payload must be a non-empty dictionary.")
    if 'id' not in data:
        raise KeyError("Invalid input: missing required key 'id'.")
    return True

def run_processing_loop(items):
    """Processes items with mandatory input validation."""
    for item in items:
        try:
            validate_input(item)
            process_item(item)
        except (ValueError, KeyError) as e:
            logger.error(f"Skipping item due to error: {e}")
        except Exception as e:
            logger.critical(f"Unexpected failure during processing: {e}")

def process_item(data):
    """Business logic for item processing."""
    logger.info(f"Successfully processed item: {data['id']}")

if __name__ == '__main__':
    data_stream = [{'id': 1}, 'bad_data', {'id': 2}, {}]
    run_processing_loop(data_stream)