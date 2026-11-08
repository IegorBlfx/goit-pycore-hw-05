import re
from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]: # define a generator function generator_numbers that takes a string text and yields float numbers found in the text
    if not text:
        return

    for match in re.finditer(r'(?<!\S)\d+(?:\.\d+)?(?!\S)', text): # use regular expression to find all numbers in the text, including integers and floats
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float: # define a function sum_profit that takes a string text and a callable func, and returns a float
    return sum(func(text))


