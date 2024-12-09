def max_subarray_sum(arr):
    n = len(arr)
    max_sum = float("-inf")
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0

    for i in range(n):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return max_sum, arr[start : end + 1]


if __name__ == "__main__":
    # Приклад використання
    arr = [2, -4, 1, 9, -6, 7, -3]
    max_sum, subarray = max_subarray_sum(arr)
    print(f"Максимальна сума підмасиву: {max_sum}")
    print(f"Підмасив з максимальною сумою: {subarray}")
