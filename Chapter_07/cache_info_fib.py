from functools import lru_cache

@lru_cache(maxsize=10)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Викликаємо функцію з різними значеннями
print(fib(10))
print(fib(15))
print(fib(20))

# Виводимо статистику кешу
print(fib.cache_info())
