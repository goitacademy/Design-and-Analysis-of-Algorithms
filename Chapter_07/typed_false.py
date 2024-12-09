from functools import lru_cache

@lru_cache(maxsize=None, typed=False)
def square_false(x):
    print(f"Computing square for {x}")
    return x * x

@lru_cache(maxsize=None, typed=True)
def square_true(x):
    print(f"Computing square for {x}")
    return x * x

a = 3
b = 3.0

print(square_false(a))  # Output: Computing square for 3
print(square_false(b))  # Output: 9 (без повторного обчислення)

print(square_true(3))  # Output: Computing square for 3
print(square_true(3.0))  # Output: Computing square for 3.0

help(lru_cache)