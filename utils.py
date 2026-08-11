from typing import List, Dict


def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): A list of float numbers.

    Returns:
        float: The average of the numbers.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filter out the even numbers from a list.

    Args:
        numbers (List[int]): A list of integer numbers.

    Returns:
        List[int]: A list containing only the odd numbers.
    """
    return [num for num in numbers if num % 2 != 0]


def count_occurrences(items: List[str]) -> Dict[str, int]:
    """
    Count the occurrences of each item in a list.

    Args:
        items (List[str]): A list of strings.

    Returns:
        Dict[str, int]: A dictionary with items as keys and their occurrences as values.
    """
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts
