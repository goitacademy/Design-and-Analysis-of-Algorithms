def longest_increasing_subsequence(arr):
    n = len(arr)
    # Ініціалізація масиву dp, де dp[i] - довжина LIS, що закінчується на i-му елементі
    dp = [1] * n

    # Заповнення dp
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Знаходження максимального значення в dp
    max_length = max(dp)

    # Відновлення самої послідовності
    sequence = []
    max_index = dp.index(max_length)
    sequence.append(arr[max_index])
    for i in range(max_index - 1, -1, -1):
        if dp[i] == max_length - 1 and arr[i] < arr[max_index]:
            sequence.append(arr[i])
            max_length -= 1
            max_index = i

    return list(reversed(sequence))


if __name__ == "__main__":
    # Приклад використання
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    lis = longest_increasing_subsequence(arr)
    print(f"Найдовша зростаюча підпослідовність: {lis}")
    print(f"Довжина: {len(lis)}")
