from itertools import chain, combinations


def subset_sum_bruteforce(items, T):
    # Генерація всіх можливих підмножин
    all_subsets = chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))

    # Знаходимо підмножину з максимальною сумою, що не перевищує T
    max_sum = 0
    best_subset = []

    for subset in all_subsets:
        subset_sum = sum(subset)
        if subset_sum <= T and subset_sum > max_sum:
            max_sum = subset_sum
            best_subset = subset

    return best_subset, max_sum


# Приклад використання
items = [3, 34, 4, 12, 5, 2]
T = 10
best_subset, max_sum = subset_sum_bruteforce(items, T)
print("Точний розв’язок методом перебору:", best_subset, "з максимальною сумою:", max_sum)
