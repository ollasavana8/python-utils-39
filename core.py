import logging

# Configure basic logging for the utility module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data: dict) -> bool:
    """Ensures input dictionary contains mandatory keys."""
    required_keys = {'id', 'payload'}
    return all(key in data for key in required_keys)

def process_items(items: list):
    """
    Main processing loop with integrated input validation.
    """
    for index, item in enumerate(items):
        try:
            if not isinstance(item, dict):
                raise ValueError(f"Item at index {index} is not a dictionary")
            
            if not validate_input(item):
                logger.warning(f"Skipping invalid item at index {index}")
                continue
                
            # Proceed with data transformation
            result = item['payload'].upper()
            logger.info(f"Processed item {item['id']}: {result}")
            
        except (ValueError, KeyError, AttributeError) as e:
            logger.error(f"Failed to process item at index {index}: {e}")

if __name__ == "__main__":
    data_stream = [
        {'id': 1, 'payload': 'data_a'},
        {'id': 2, 'payload': 'data_b'},
        {'invalid': 'entry'},
        {'id': 3, 'payload': 'data_c'}
    ]
    process_items(data_stream)