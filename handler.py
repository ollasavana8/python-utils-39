import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataHandler:
    """Manages data processing and cleanup tasks."""
    
    def __init__(self, temp_dir: str = '/tmp/processor'):
        self.temp_dir = temp_dir

    def cleanup(self) -> None:
        """Removes all temporary files from the workspace."""
        if not os.path.exists(self.temp_dir):
            return
        
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        logger.info(f"Cleanup of {self.temp_dir} completed")

    def process(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Validates and transforms input data dictionary."""
        if not data:
            logger.warning("Received empty data package")
            return None
            
        try:
            processed = {k.lower(): v for k, v in data.items()}
            processed['status'] = 'processed'
            return processed
        except Exception as e:
            logger.error(f"Processing error: {e}")
            return None

if __name__ == "__main__":
    handler = DataHandler()
    handler.cleanup()