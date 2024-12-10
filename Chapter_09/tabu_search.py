# Визначення цільової функції
def objective_function(x, y):
    return (x - 3) ** 2 + (y - 2) ** 2


# Функція для визначення сусідів поточної точки
def get_neighbors(current, step_size=1.0):
    x, y = current
    return [
        (x + step_size, y),
        (x - step_size, y),
        (x, y + step_size),
        (x, y - step_size)
    ]


# Реалізація алгоритму Tabu Search
def tabu_search(starting_point, max_iterations, tabu_list_size, step_size=1.0):
    current_point = starting_point
    current_value = objective_function(*current_point)
    best_point = current_point
    best_value = current_value

    tabu_list = []

    for iteration in range(max_iterations):
        # Отримання сусідів
        neighbors = get_neighbors(current_point, step_size)

        # Фільтрування сусідів, які є в таблиці табу
        feasible_neighbors = [neighbor for neighbor in neighbors if neighbor not in tabu_list]

        # Якщо всі сусіди в табу, дозволити вибір будь-якого
        if not feasible_neighbors:
            feasible_neighbors = neighbors

        # Вибір найкращого сусіда серед допустимих
        next_point = min(feasible_neighbors, key=lambda point: objective_function(*point))
        next_value = objective_function(*next_point)

        # Оновлення таблиці табу
        tabu_list.append(current_point)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

        # Перехід до наступної точки
        current_point, current_value = next_point, next_value

        # Оновлення найкращого знайденого рішення
        if current_value < best_value:
            best_point, best_value = current_point, current_value

    return best_point, best_value

if __name__ == "__main__":
    # Використання алгоритму
    starting_point = (0.0, 0.0)
    max_iterations = 50
    tabu_list_size = 5
    best_point, best_value = tabu_search(starting_point, max_iterations, tabu_list_size)

    print(f"Найкраща знайдена точка: {best_point}")
    print(f"Значення цільової функції в цій точці: {best_value}")