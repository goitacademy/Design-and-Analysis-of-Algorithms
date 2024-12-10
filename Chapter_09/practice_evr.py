import numpy as np
import random

# Створення матриці відстаней для 10 магазинів + 1 склад (загалом 11 точок)
num_locations = 11  # 1 склад + 10 магазинів

# Ініціалізація матриці з відстанями між точками
# Матриця є квадратною: кожен елемент [i][j] показує відстань між точкою i та точкою j
# Відстані генеруються випадковим чином для спрощення (від 5 до 50 км)
distance_matrix = [[0 if i == j else random.randint(5, 50) for j in range(num_locations)] for i in range(num_locations)]

# Зробимо матрицю симетричною, оскільки відстань між точками однакова в обох напрямках
for i in range(num_locations):
    for j in range(i + 1, num_locations):
        distance_matrix[j][i] = distance_matrix[i][j]

# Виведемо матрицю для перевірки
print("Матриця відстаней (перший рядок - склад, інші - магазини):")
for row in distance_matrix:
    print(row)

def nearest_neighbor_algorithm(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    route = [0]  # починаємо з центрального складу (нульова точка)
    visited[0] = True

    for _ in range(n - 1):
        last_visited = route[-1]
        nearest_distance = float('inf')
        nearest_index = -1

        # Знаходимо найближчий невідвіданий магазин
        for i in range(n):
            if not visited[i] and 0 < distance_matrix[last_visited][i] < nearest_distance:
                nearest_distance = distance_matrix[last_visited][i]
                nearest_index = i

        route.append(nearest_index)
        visited[nearest_index] = True

    route.append(0)  # повертаємося на склад
    return route

# Використання створеної раніше матриці відстаней
route = nearest_neighbor_algorithm(distance_matrix)
print("Оптимальний маршрут за алгоритмом найближчого сусіда:", route)