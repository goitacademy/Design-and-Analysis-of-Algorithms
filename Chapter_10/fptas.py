import math


# Функція для знаходження наближеного розв’язку задачі рюкзака за допомогою FPTAS
def knapsack_fptas(items, max_weight, epsilon):
    # Знаходимо максимальну вартість предметів
    max_value = max(v for w, v in items)

    # Масштабування коефіцієнта точності
    scaling_factor = epsilon * max_value / len(items)

    # Масштабування вартостей предметів
    scaled_items = [(w, math.floor(v / scaling_factor)) for w, v in items]

    # Використовуємо динамічне програмування для наближеного розв’язку
    n = len(items)
    # Ініціалізуємо масив dp з великими значеннями
    max_scaled_value = sum(v for _, v in scaled_items)
    dp = [float('inf')] * (max_scaled_value + 1)
    dp[0] = 0

    # Заповнюємо таблицю dp
    for w, v in scaled_items:
        for j in range(max_scaled_value, v - 1, -1):
            dp[j] = min(dp[j], dp[j - v] + w)

    # Знаходимо максимальну вартість, яка не перевищує вагу рюкзака
    for value in range(max_scaled_value, -1, -1):
        if dp[value] <= max_weight:
            # Повертаємо наближену вартість рюкзака
            return value * scaling_factor

    return 0


# Приклад використання
items = [(2, 40), (3, 50), (4, 60), (5, 90)]  # Кожен предмет - (вага, вартість)
max_weight = 8  # Максимальна вага рюкзака
epsilon = 0.5  # Точність наближення

approx_value = knapsack_fptas(items, max_weight, epsilon)
print("Наближене значення рюкзака:", approx_value)
