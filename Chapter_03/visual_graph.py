import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.DiGraph()

# Додаємо ребра з пропускною здатністю
edges = [
    (0, 2, 15),  # Джерело 1 -> Проміжний Вузол 1
    (0, 3, 10),  # Джерело 1 -> Проміжний Вузол 2
    (1, 2, 20),  # Джерело 2 -> Проміжний Вузол 1
    (2, 4, 10),  # Проміжний Вузол 1 -> Споживач 1
    (2, 5, 5),  # Проміжний Вузол 1 -> Споживач 2
    (3, 6, 15),  # Проміжний Вузол 2 -> Споживач 3
]

# Додаємо всі ребра до графа
G.add_weighted_edges_from(edges)

# Позиції для малювання графа
pos = {
    0: (0, 2),  # Джерело 1
    1: (0, 0),  # Джерело 2
    2: (2, 2),  # Проміжний Вузол 1
    3: (2, 1),  # Проміжний Вузол 2
    4: (4, 2),  # Споживач 1
    5: (4, 1),  # Споживач 2
    6: (4, 0),  # Споживач 3
}

# Малюємо граф
plt.figure(figsize=(10, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="skyblue",
    font_size=12,
    font_weight="bold",
    arrows=True,
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Відображаємо граф
plt.show()
