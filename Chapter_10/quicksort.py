import random

def randomized_quick_sort(arr):
    # Якщо масив має менше двох елементів, він вже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо випадковий індекс для опорного елемента
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Розділяємо масив на частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Приклад використання
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = randomized_quick_sort(arr)
print("Відсортований масив:", sorted_arr)
