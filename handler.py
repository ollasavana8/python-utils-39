from typing import Any, Dict, Optional, Callable
import logging

logger = logging.getLogger(__name__)

class RequestHandler:
    """Handles incoming request payloads with transformation support."""

    def __init__(self, processor: Optional[Callable[[Any], Any]] = None) -> None:
        self.processor = processor

    def handle(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Processes raw request data and returns a structured response."""
        try:
            processed_data = self.processor(data) if self.processor else data
            return {
                "status": "success",
                "payload": processed_data
            }
        except Exception as e:
            logger.error(f"Processing error: {e}")
            return {
                "status": "error",
                "message": str(e)
            }

    def validate_keys(self, data: Dict[str, Any], required: list[str]) -> bool:
        """Checks if all required keys exist in the input dictionary."""
        return all(key in data for key in required)