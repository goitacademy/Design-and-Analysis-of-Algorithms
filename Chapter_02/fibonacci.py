import time


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dp(n):
    # Ініціалізація масиву для зберігання результатів підзадач
    fib = [0] * (n + 1)

    # Базові випадки
    fib[0] = 0
    if n > 0:
        fib[1] = 1

    # Заповнення масиву
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def time_function(func, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    print(f"{func.__name__}({n}) = {result}, Time: {end - start:.6f} seconds")


if __name__ == "__main__":
    # Порівняння ефективності
    n = 35
    time_function(fibonacci_recursive, n)
    time_function(fibonacci_dp, n)
