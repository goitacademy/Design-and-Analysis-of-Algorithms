from BTrees.OOBTree import OOBTree

# Створення OOBTree
tree = OOBTree()

# Додавання об'єктів з ключами одного типу (цілі числа)
tree.update({1: "red", 2: "green", 3: "blue", 4: "spades"})

# Пошук об'єктів
print(tree.get(1))  # Виведе 'red'
print(tree.get(5, "not found"))  # Виведе 'not found'

# Видалення об'єктів
del tree[2]

# Перегляд усіх об'єктів
for key, value in tree.items():
    print(key, value)
