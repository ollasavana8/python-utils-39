from functools import lru_cache
import itertools
from typing import Callable, Generator, Iterable, List, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class CoreOptimizer:
    """Performance optimizations for sequence processing and cached transformations."""

    def __init__(self, cache_size: int = 512):
        self.cache_size = cache_size

    @staticmethod
    def chunkify(sequence: Sequence[T], chunk_size: int) -> Generator[Sequence[T], None, None]:
        """Efficiently yield slices of a sequence without memory duplication."""
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        for i in range(0, len(sequence), chunk_size):
            yield sequence[i : i + chunk_size]

    @staticmethod
    def memoized_transform(fn: Callable[..., R], maxsize: int = 128) -> Callable[..., R]:
        """Wraps a callable with LRU caching for performance optimization."""
        return lru_cache(maxsize=maxsize)(fn)

    @classmethod
    def deduplicate_fast(cls, items: Iterable[T]) -> List[T]:
        """Deduplicates items while preserving order using dict keys."""
        return list(dict.fromkeys(items))

    @classmethod
    def batch_map(cls, fn: Callable[[T], R], items: Sequence[T], batch_size: int = 100) -> List[R]:
        """Applies a transformation in memory-efficient batches."""
        cached_fn = lru_cache(maxsize=256)(fn)
        results: List[R] = []
        for chunk in cls.chunkify(items, batch_size):
            results.extend(cached_fn(item) for item in chunk)
        return results
