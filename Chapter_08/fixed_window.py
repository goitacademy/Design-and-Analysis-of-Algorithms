def max_sum_fixed_window(arr, k):
    current_sum = sum(arr[:k])  # Сума першого вікна
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]  # Додаємо новий елемент і видаляємо старий
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    # Приклад використання
    arr = [3, 4, 1, 5, 6, 2, 6]
    k = 3
    max_sum = max_sum_fixed_window(arr, k)
    print(f"Максимальна сума у фіксованому вікні: {max_sum}")