from typing import Callable # import Callable from typing module


def caching_fibonacci() -> Callable[[int], int]:  # define a function caching_fibonacci that returns a callable function
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int: # define a nested function fibonacci that takes an integer n and returns an integer
        if not isinstance(n, int):
            raise TypeError("n має бути цілим числом")
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci