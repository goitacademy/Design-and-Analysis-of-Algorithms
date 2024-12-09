import heapq
from collections import defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    # Підрахунок частот
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    # Створення листа пріоритетів
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Побудова дерева
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        heapq.heappush(heap, internal)

    return heap[0]  # Корінь дерева


def generate_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    return codes


if __name__ == "__main__":
    # Використання
    text = "ABRACADABRA"
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    print(codes)
