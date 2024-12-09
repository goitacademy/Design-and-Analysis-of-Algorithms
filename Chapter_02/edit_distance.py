def edit_distance(str1: str, str2: str) -> int:
    m, n = len(str1), len(str2)

    # Створення таблиці для зберігання результатів підзадач
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Заповнення першої колонки та першого рядка
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Заповнення решти таблиці
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]  # видалення  # вставка
                )  # заміна

    return dp[m][n]


if __name__ == "__main__":
    # Приклад використання
    str1 = "kitten"
    str2 = "sitting"
    print(f"Редакційна відстань між '{str1}' та '{str2}': {edit_distance(str1, str2)}")

    str1 = "ABRACADABRA"
    str2 = "ABRACADABRA"
    print(f"Редакційна відстань між '{str1}' та '{str2}': {edit_distance(str1, str2)}")
