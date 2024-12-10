import time
from functools import wraps

def throttle(rate):
    def decorator(func):
        last_call = [0]

        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            if current_time - last_call[0] >= rate:
                last_call[0] = current_time
                return func(*args, **kwargs)
            else:
                print("Function call throttled")
        return wrapper
    return decorator

@throttle(1.0)  # Функція може викликатися не частіше одного разу на секунду
def my_function():
    print("Function executed")

# Виклик функції кілька разів
for _ in range(5):
    my_function()
    time.sleep(0.3)