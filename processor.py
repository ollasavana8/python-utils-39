import json
from typing import Any, Dict

class ProcessorError(Exception):
    pass

class DataProcessor:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def process_data(self) -> Dict[str, Any]:
        if not isinstance(self.data, dict):
            raise ProcessorError('Data must be a dictionary.')
        try:
            result = self.perform_computation(self.data)
            return result
        except (KeyError, ValueError) as e:
            raise ProcessorError(f'Error in processing data: {e}')

    def perform_computation(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Dummy computation to simulate processing
        if 'value' not in data:
            raise KeyError('Missing required field: value')
        if not isinstance(data['value'], (int, float)):
            raise ValueError('Field value must be a number.')
        data['result'] = data['value'] * 2  # Simple operation
        return data

if __name__ == '__main__':
    sample_data = {'value': 10}
    processor = DataProcessor(sample_data)
    try:
        processed_data = processor.process_data()
        print(json.dumps(processed_data, indent=4))
    except ProcessorError as e:
        print(f'Processing failed: {e}')