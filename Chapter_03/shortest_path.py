import networkx as nx
from collections import deque

# Створення графа
G = nx.Graph()

# Додавання вершин та ребер
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "E"),
    ("C", "G"),
    ("D", "F"),
    ("E", "G"),
    ("F", "H"),
    ("G", "I"),
    ("H", "I"),
    ("H", "J"),
    ("D", "J"),
    ("E", "J"),
]
G.add_edges_from(edges)


# Реалізація алгоритму BFS для знаходження найкоротшого шляху
def bfs_shortest_path(graph, start, goal):
    # Черга для зберігання шляхів
    queue = deque([[start]])
    # Множина для відвіданих вершин
    visited = set()

    while queue:
        # Беремо перший шлях з черги
        path = queue.popleft()
        # Остання вершина в поточному шляху
        node = path[-1]

        # Якщо ми дісталися мети, повертаємо шлях
        if node == goal:
            return path

        # Якщо вершина ще не відвідана, перевіряємо її сусідів
        elif node not in visited:
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            # Позначаємо вершину як відвідану
            visited.add(node)

    # Якщо шляху не знайдено
    return None


if __name__ == "__main__":
    # Використання BFS для знаходження найкоротшого шляху від 'A' до 'J'
    shortest_path = bfs_shortest_path(G, "A", "J")
    if shortest_path:
        print("Найкоротший шлях від A до J:", " -> ".join(shortest_path))
    else:
        print("Шлях не знайдено")
