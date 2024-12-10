# Універсальна множина
U = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Набір підмножин, які покривають універсальну множину
S = [
    {1, 2, 3},
    {2, 4, 5},
    {3, 6},
    {4, 5, 7},
    {5, 6, 8, 9},
    {7, 8}
]


def greedy_set_cover(U, S):
    # Зберігатиме обрані підмножини
    chosen_sets = []
    # Непокриті елементи з U
    uncovered_elements = U.copy()

    # Поки є непокриті елементи
    while uncovered_elements:
        # Знайдемо підмножину, яка покриває найбільшу кількість непокритих елементів
        best_subset = max(S, key=lambda subset: len(subset & uncovered_elements))

        # Додаємо цю підмножину до списку обраних
        chosen_sets.append(best_subset)

        # Видаляємо покриті елементи з множини непокритих
        uncovered_elements -= best_subset

    return chosen_sets


# Виклик алгоритму
solution = greedy_set_cover(U, S)
print("Обрані підмножини для покриття множини U:", solution)
