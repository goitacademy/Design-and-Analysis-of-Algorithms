import numpy as np
import matplotlib.pyplot as plt

# Задамо випадкові дані для навчання
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Параметри моделі
m = len(X)
alpha = 0.01  # Крок навчання
n_iterations = 50  # Кількість ітерацій

# Ініціалізація ваг моделі (w) і вільного члена (b)
w = np.random.randn(1, 1)
b = np.random.randn(1, 1)  # змінено форму b на (1, 1)


# Функція для прогнозування
def predict(X):
    return X.dot(w) + b


# Стохастичний градієнтний спуск
for iteration in range(n_iterations):
    for i in range(m):
        random_index = np.random.randint(m)  # Обираємо випадковий зразок
        xi = X[random_index:random_index + 1]
        yi = y[random_index:random_index + 1]

        # Обчислення прогнозу
        y_pred = predict(xi)

        # Обчислення градієнтів для w та b
        gradient_w = 2 * xi.T.dot(y_pred - yi)
        gradient_b = 2 * (y_pred - yi)

        # Оновлення параметрів
        w -= alpha * gradient_w
        b -= alpha * gradient_b

# Візуалізація результатів
plt.scatter(X, y, color="blue", label="Дані")
plt.plot(X, predict(X), color="red", label="Модель (SGD)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
