import numpy as np

# Матриця переходів
P = np.array([
    [0.1, 0.4, 0.2],
    [0.6, 0.5, 0.3],
    [0.3, 0.1, 0.5]
])

# Початковий розподіл імовірностей (наприклад, 100% користувачів починають з A)
initial_distribution = np.array([1.0, 0.0, 0.0])

# Кількість ітерацій для досягнення нерухомого розподілу
num_iterations = 100

# Наближене знаходження нерухомого розподілу
distribution = initial_distribution
for _ in range(num_iterations):
    distribution = P @ distribution

# Виведення результатів
print("Нерухомий розподіл:")
print("Імовірність перебування на сайті A:", distribution[0])
print("Імовірність перебування на сайті B:", distribution[1])
print("Імовірність перебування на сайті C:", distribution[2])
