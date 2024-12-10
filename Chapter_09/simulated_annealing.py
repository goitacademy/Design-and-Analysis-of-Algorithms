import random
import math

def simulated_annealing(initial_solution, temperature, cooling_rate):
    def evaluate(solution):
        x, y = solution
        return (x - 3) ** 2 + (y - 2) ** 2

    def generate_neighbor(solution):
        x, y = solution
        new_x = x + random.uniform(-1, 1)
        new_y = y + random.uniform(-1, 1)
        return (new_x, new_y)

    current_solution = initial_solution
    current_energy = evaluate(current_solution)

    while temperature > 0.001:
        new_solution = generate_neighbor(current_solution)
        new_energy = evaluate(new_solution)
        delta_energy = new_energy - current_energy

        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
            current_solution = new_solution
            current_energy = new_energy

        temperature *= cooling_rate

    return current_solution, current_energy


if __name__ == "__main__":
    # Налаштування для алгоритму
    initial_solution = (0, 0)  # Початкова точка
    temperature = 1000         # Початкова температура
    cooling_rate = 0.85        # Швидкість охолодження
    runs = 10                  # Кількість запусків

    best_solution = None
    best_energy = float("inf")

    for i in range(runs):
        print(f"Запуск #{i + 1}")
        solution, energy = simulated_annealing(initial_solution, temperature, cooling_rate)
        print(f"Рішення: {solution}, Енергія: {energy}")
        if energy < best_energy:
            best_solution = solution
            best_energy = energy

    print("\nНайкраще знайдене рішення:")
    print(f"Рішення: {best_solution}, Енергія: {best_energy}")