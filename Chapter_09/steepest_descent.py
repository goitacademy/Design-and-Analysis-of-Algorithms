import numpy as np


# Визначення цільової функції
def objective_function(x, y):
    return (x - 3) ** 2 + (y - 2) ** 2


# Обчислення градієнта цільової функції
def gradient(x, y):
    df_dx = 2 * (x - 3)
    df_dy = 2 * (y - 2)
    return np.array([df_dx, df_dy])


# Реалізація алгоритму «Спадний пошук»
def steepest_descent(starting_point, learning_rate, max_iterations, tolerance=1e-6):
    x = np.array(starting_point)

    for iteration in range(max_iterations):
        grad = gradient(x[0], x[1])
        # Перевірка умови зупинки (градієнт майже нульовий)
        if np.linalg.norm(grad) < tolerance:
            break
        # Оновлення змінних
        x = x - learning_rate * grad

    return x

if __name__ == "__main__":
    # Використання алгоритму
    starting_point = (0.0, 0.0)
    learning_rate = 0.1
    max_iterations = 100
    minimum_point = steepest_descent(starting_point, learning_rate, max_iterations)

    print(f"Найкраща знайдена точка: {minimum_point}")