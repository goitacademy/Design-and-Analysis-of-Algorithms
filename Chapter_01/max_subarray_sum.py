def max_crossing_sum(arr, left, mid, right):
    left_sum = float("-inf")
    total = 0
    max_left = mid
    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float("-inf")
    total = 0
    max_right = mid + 1
    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
            max_right = i

    return left_sum + right_sum, max_left, max_right


def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left], left, right

    mid = (left + right) // 2

    left_sum, left_start, left_end = max_subarray_sum(arr, left, mid)
    right_sum, right_start, right_end = max_subarray_sum(arr, mid + 1, right)
    cross_sum, cross_start, cross_end = max_crossing_sum(arr, left, mid, right)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_start, left_end
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_start, right_end
    else:
        return cross_sum, cross_start, cross_end


# Приклад використання
arr = [2, -4, 1, 9, -6, 7, -3]
max_sum, start, end = max_subarray_sum(arr, 0, len(arr) - 1)
print(f"Максимальна сума підмасиву: {max_sum}")
print(f"Підмасив: {arr[start:end+1]}")
