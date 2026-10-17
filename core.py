"""Core utility framework for python-utils-39.

Provides unified execution pipeline and dictionary restructuring utilities.
"""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional
import time


@dataclass
class ExecutionResult:
    """Container for execution status and outcome metrics."""
    success: bool
    result: Optional[Any] = None
    error: Optional[Exception] = None
    duration_ms: float = 0.0


class TaskPipeline:
    """Sequential task processing pipeline with execution metrics tracking."""

    def __init__(self, name: str = "default_pipeline") -> None:
        self.name = name
        self.steps: List[Callable[[], Any]] = []

    def add_step(self, func: Callable[[], Any]) -> "TaskPipeline":
        """Registers a callable step to the pipeline execution chain."""
        self.steps.append(func)
        return self

    def run(self) -> List[ExecutionResult]:
        """Executes all registered pipeline steps sequentially."""
        results: List[ExecutionResult] = []
        for step in self.steps:
            start_time = time.perf_counter()
            try:
                res = step()
                elapsed = (time.perf_counter() - start_time) * 1000
                results.append(ExecutionResult(success=True, result=res, duration_ms=elapsed))
            except Exception as err:
                elapsed = (time.perf_counter() - start_time) * 1000
                results.append(ExecutionResult(success=False, error=err, duration_ms=elapsed))
        return results


def flatten_dict(data: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flattens nested dictionary structures into single-level key paths."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)
