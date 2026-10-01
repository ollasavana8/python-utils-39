import collections
from itertools import islice
from typing import Generator, Iterable, Any, Dict, List

def chunk_iterable(iterable: Iterable[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """
    Yield successive chunks from an iterable.
    
    Optimized with itertools.islice to avoid loading the full iterable into memory.
    """
    if chunk_size < 1:
        raise ValueError("Chunk size must be at least 1")
    iterator = iter(iterable)
    while True:
        chunk = list(islice(iterator, chunk_size))
        if not chunk:
            break
        yield chunk

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flatten a nested dictionary iteratively.
    
    Optimized using a queue to prevent recursion overhead and stack limit errors.
    """
    items: List[tuple] = []
    queue = collections.deque([(d, parent_key)])

    while queue:
        current_dict, prefix = queue.popleft()
        for k, v in current_dict.items():
            new_key = f"{prefix}{sep}{k}" if prefix else k
            if isinstance(v, dict):
                queue.append((v, new_key))
            else:
                items.append((new_key, v))
                
    return dict(items)