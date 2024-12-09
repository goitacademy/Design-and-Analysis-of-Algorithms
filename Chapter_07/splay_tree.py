class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None


class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Вставка нового елемента в дерево."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_node(data, self.root)

    def _insert_node(self, data, current_node):
        """Рекурсивна вставка елемента у дерево."""
        if data < current_node.data:
            if current_node.left_node:
                self._insert_node(data, current_node.left_node)
            else:
                current_node.left_node = Node(data, current_node)
        else:
            if current_node.right_node:
                self._insert_node(data, current_node.right_node)
            else:
                current_node.right_node = Node(data, current_node)

    def find(self, data):
        """Пошук елемента в дереві із застосуванням сплайювання."""
        node = self.root
        while node is not None:
            if data < node.data:
                node = node.left_node
            elif data > node.data:
                node = node.right_node
            else:
                self._splay(node)
                return node.data
        return None  # Якщо елемент не знайдено.

    def _splay(self, node):
        """Реалізація сплайювання для переміщення вузла до кореня."""
        while node.parent is not None:
            if node.parent.parent is None:  # Zig ситуація
                if node == node.parent.left_node:
                    self._rotate_right(node.parent)
                else:
                    self._rotate_left(node.parent)
            elif node == node.parent.left_node and node.parent == node.parent.parent.left_node:  # Zig-Zig
                self._rotate_right(node.parent.parent)
                self._rotate_right(node.parent)
            elif node == node.parent.right_node and node.parent == node.parent.parent.right_node:  # Zig-Zig
                self._rotate_left(node.parent.parent)
                self._rotate_left(node.parent)
            else:  # Zig-Zag
                if node == node.parent.left_node:
                    self._rotate_right(node.parent)
                    self._rotate_left(node.parent)
                else:
                    self._rotate_left(node.parent)
                    self._rotate_right(node.parent)

    def _rotate_right(self, node):
        """Права ротація вузла."""
        left_child = node.left_node
        if left_child is None:
            return

        node.left_node = left_child.right_node
        if left_child.right_node:
            left_child.right_node.parent = node

        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.left_node:
            node.parent.left_node = left_child
        else:
            node.parent.right_node = left_child

        left_child.right_node = node
        node.parent = left_child

    def _rotate_left(self, node):
        """Ліва ротація вузла."""
        right_child = node.right_node
        if right_child is None:
            return

        node.right_node = right_child.left_node
        if right_child.left_node:
            right_child.left_node.parent = node

        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left_node:
            node.parent.left_node = right_child
        else:
            node.parent.right_node = right_child

        right_child.left_node = node
        node.parent = right_child


if __name__ == '__main__':
    splay_tree = SplayTree()
    splay_tree.insert(10)
    splay_tree.insert(8)
    splay_tree.insert(3)
    splay_tree.insert(7)

    print("Accessing 7:", splay_tree.find(7))
    print("Accessing 3:", splay_tree.find(3))
    print("Accessing 8:", splay_tree.find(8))
    print("Accessing 3:", splay_tree.find(3))
    print("Root after operations:", splay_tree.root.data)
