import numpy as np
import matplotlib.pyplot as plt

# Визначення цільової функції
def objective_function(x, y):
    return np.sin(x) * np.cos(y) + 0.5 * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))

# Функція для визначення сусідів поточної точки
def get_neighbors(current, step_size=0.1):
    x, y = current
    return [
        (x + step_size, y),
        (x - step_size, y),
        (x, y + step_size),
        (x, y - step_size)
    ]

# Реалізація алгоритму "Підйом на гору"
def hill_climbing(starting_point, max_iterations, step_size=0.1):
    current_point = starting_point
    current_value = objective_function(*current_point)

    for iteration in range(max_iterations):
        neighbors = get_neighbors(current_point, step_size)

        # Пошук найкращого сусіда
        next_point = None
        next_value = -np.inf

        for neighbor in neighbors:
            value = objective_function(*neighbor)
            if value > next_value:
                next_point = neighbor
                next_value = value

        # Якщо не вдається знайти кращого сусіда — зупиняємось
        if next_value <= current_value:
            break

        # Переходимо до кращого сусіда
        current_point, current_value = next_point, next_value

    return current_point, current_value


if __name__ == "__main__":
    # Використання алгоритму
    starting_point = (0.0, 0.0)
    max_iterations = 100
    best_point, best_value = hill_climbing(starting_point, max_iterations)

    print(f"Найкраща знайдена точка: {best_point}")
    print(f"Значення цільової функції в цій точці: {best_value}")

    # Візуалізація поверхні та знайденої точки
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    X, Y = np.meshgrid(x, y)
    Z = objective_function(X, Y)

    plt.figure(figsize=(10, 6))
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    plt.scatter(*best_point, color='red', marker='o', label='Найкраща знайдена точка')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Цільова функція та знайдена точка максимуму')
    plt.legend()
    plt.show()