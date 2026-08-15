from typing import List, Optional


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filters out even numbers from a list.

    Parameters:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list containing only the even integers from the input list.
    """
    return [num for num in numbers if num % 2 == 0]


def find_maximum(numbers: List[float]) -> Optional[float]:
    """
    Finds the maximum number in a list.

    Parameters:
    numbers (List[float]): A list of float numbers.

    Returns:
    Optional[float]: The maximum number in the list, or None if the list is empty.
    """
    return max(numbers) if numbers else None


def count_occurrences(items: List[str]) -> dict:
    """
    Counts the occurrences of each item in a list.

    Parameters:
    items (List[str]): A list of strings.

    Returns:
    dict: A dictionary with items as keys and their counts as values.
    """
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def reverse_string(s: str) -> str:
    """
    Reverses the given string.

    Parameters:
    s (str): A string to be reversed.

    Returns:
    str: The reversed string.
    """
    return s[::-1]
