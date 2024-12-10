# Список прикладів

## Алгоритми контролю потоку та обмеження швидкості

1. [`fixed_window.py`](/Chapter_08/fixed_window.py) - реалізація Sliding Window з фіксованим вікном
2. [`sliding_window.py`](/Chapter_08/sliding_window.py) - реалізація Sliding Window з змінним вікном
3. [`token_bucket.py`](/Chapter_08/token_bucket.py) - реалізація алгоритму Token Bucket
4. [`leaky_bucket.py`](/Chapter_08/leaky_bucket.py) - реалізація Leaky Bucket
5. [`ratelimit_token.py`](/Chapter_08/ratelimit_token.py) - реалізацію Rate Limiting за допомогою алгоритму Token Bucket
6. [`fastapi_ratelimit.py`](/Chapter_08/fastapi_ratelimit.py) - використання бібліотеки `slowapi` з використанням фреймворку FastAPI. Після запуску прикладу перейти на [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
7. [`back.py`](/Chapter_08/back.py) - використання Backpressure при обробці даних з потоку
8. [`throttle.py`](/Chapter_08/throttle.py) - Приклад реалізації Throttle Control
