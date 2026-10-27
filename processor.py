"""Data processing utilities with robust edge case handling."""

from typing import Any, Callable, Dict, List, Optional, Union


def safe_cast(value: Any, target_type: type, default: Any = None) -> Any:
    """Safely cast a value to a target type without raising exceptions."""
    if value is None:
        return default
    try:
        return target_type(value)
    except (ValueError, TypeError, OverflowError):
        return default


def safe_divide(numerator: Any, denominator: Any, default: Union[int, float] = 0.0) -> float:
    """Perform division with zero and non-numeric edge case protection."""
    num = safe_cast(numerator, float)
    den = safe_cast(denominator, float)
    
    if num is None or den is None or den == 0.0:
        return float(default)
    
    try:
        return num / den
    except (ZeroDivisionError, OverflowError):
        return float(default)


def safe_get_nested(data: Any, keys: List[Union[str, int]], default: Any = None) -> Any:
    """Traverse nested dicts or lists safely handling missing keys and index errors."""
    if not isinstance(keys, (list, tuple)):
        return default
    
    current = data
    for key in keys:
        if isinstance(current, dict) and isinstance(key, str):
            current = current.get(key, default)
        elif isinstance(current, (list, tuple)) and isinstance(key, int):
            try:
                current = current[key]
            except IndexError:
                return default
        else:
            return default
        
        if current is default:
            break
            
    return current


def process_batch_safely(
    items: List[Any], 
    transform: Callable[[Any], Any], 
    skip_errors: bool = True
) -> Dict[str, Any]:
    """Process a batch of items with error isolation per item."""
    results = []
    errors = []
    
    if not isinstance(items, (list, tuple, set)):
        return {"results": [], "errors": [{"index": -1, "error": "Invalid iterable provided"}]}

    for idx, item in enumerate(items):
        try:
            results.append(transform(item))
        except Exception as exc:
            errors.append({"index": idx, "item": str(item), "error": str(exc)})
            if not skip_errors:
                break
                
    return {"results": results, "errors": errors}
