import time


def fibonacci_memo(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def time_function(func, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    print(f"{func.__name__}({n}) = {result}, Time: {end - start:.6f} seconds")


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    n = 35
    time_function(fibonacci_recursive, n)
    time_function(fibonacci_memo, n)
