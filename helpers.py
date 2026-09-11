import json
import math
from typing import Any, Generator, Iterable


def chunk_iterable(iterable: Iterable[Any], size: int) -> Generator[list[Any], None, None]:
    """Yield successive n-sized chunks from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def format_bytes(size_bytes: int) -> str:
    """Format bytes into a human-readable string (KB, MB, GB, etc.)."""
    if size_bytes < 0:
        raise ValueError("Size cannot be negative.")
    if size_bytes == 0:
        return "0 B"
    power = int(math.floor(math.log(size_bytes, 1024)))
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    if power >= len(units):
        power = len(units) - 1
    scaled_size = size_bytes / math.pow(1024, power)
    return f"{scaled_size:.2f} {units[power]}"


def safe_json_load(json_str: str, default: Any = None) -> Any:
    """Safely parse a JSON string, returning a default value on failure."""
    if not json_str:
        return default
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return default
