from collections import deque


# Функція для пошуку збільшуючого шляху (BFS)
def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(capacity_matrix)):
            # Перевірка, чи є залишкова пропускна здатність у каналі
            if (
                not visited[neighbor]
                and capacity_matrix[current_node][neighbor]
                - flow_matrix[current_node][neighbor]
                > 0
            ):
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)

    return False


# Основна функція для обчислення максимального потоку
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [
        [0] * num_nodes for _ in range(num_nodes)
    ]  # Ініціалізуємо матрицю потоку нулем
    parent = [-1] * num_nodes
    max_flow = 0

    # Поки є збільшуючий шлях, додаємо потік
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Знаходимо мінімальну пропускну здатність уздовж знайденого шляху (вузьке місце)
        path_flow = float("Inf")
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(
                path_flow,
                capacity_matrix[previous_node][current_node]
                - flow_matrix[previous_node][current_node],
            )
            current_node = previous_node

        # Оновлюємо потік уздовж шляху, враховуючи зворотний потік
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        # Збільшуємо максимальний потік
        max_flow += path_flow

    return max_flow


if __name__ == "__main__":
    # Матриця пропускної здатності для каналів у мережі (capacity_matrix)
    capacity_matrix = [
        [0, 0, 15, 10, 0, 0, 0],  # Джерело 1
        [0, 0, 20, 0, 0, 0, 0],  # Джерело 2
        [0, 0, 0, 0, 10, 5, 0],  # Проміжний Вузол 1
        [0, 0, 0, 0, 0, 0, 15],  # Проміжний Вузол 2
        [0, 0, 0, 0, 0, 0, 0],  # Споживач 1
        [0, 0, 0, 0, 0, 0, 0],  # Споживач 2
        [0, 0, 0, 0, 0, 0, 0],  # Споживач 3
    ]

    source = 0  # Джерело 1
    sink = 6  # Споживач 3

    print(f"Максимальний потік: {edmonds_karp(capacity_matrix, source, sink)}")
