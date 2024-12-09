import random
from functools import lru_cache

@lru_cache(maxsize=3)
def get_exchange_rate(currency):
    # Імітація отримання курсу з зовнішнього джерела
    print(f"Fetching exchange rate for {currency}")
    return round(random.uniform(20.0, 30.0), 2)

# Викликаємо функцію
print(get_exchange_rate('USD'))
print(get_exchange_rate('EUR'))

# Виводимо статистику кешу
print(get_exchange_rate.cache_info())

# Припустимо, дані у зовнішньому джерелі змінилися,
# і ми очищуємо кеш
get_exchange_rate.cache_clear()

# Викликаємо функцію знову для тих самих валют
print(get_exchange_rate('USD'))
print(get_exchange_rate('EUR'))

# Виводимо оновлену статистику кешу
print(get_exchange_rate.cache_info())
