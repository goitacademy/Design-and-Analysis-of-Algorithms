from collections import deque

from trie import Trie


# Функція для пошуку можливих варіантів виправлення з використанням редакційної відстані
def get_corrections(trie, word, max_distance=1):
    queue = deque([(trie.root, "", 0)])
    corrections = []

    while queue:
        current_node, current_word, current_distance = queue.popleft()

        if current_distance > max_distance:
            continue

        if current_node.value is not None and current_distance > 0:
            corrections.append(current_word)

        for char, next_node in current_node.children.items():
            next_distance = current_distance + (
                0 if char == word[len(current_word)] else 1
            )
            queue.append((next_node, current_word + char, next_distance))

    return corrections


if __name__ == "__main__":
    # Ініціалізація Trie та вставка слів у словник
    trie = Trie()
    words = [
        "apple",
        "application",
        "appetizer",
        "banana",
        "band",
        "banner",
        "ball",
        "bat",
        "battery",
    ]

    # Додаємо слова до Trie
    for index, word in enumerate(words):
        trie.put(word, index)

    # Приклад використання пошуку виправлень
    word_with_typo = "battary"
    corrections = get_corrections(trie, word_with_typo, max_distance=1)
    print(f"Можливі варіанти виправлення для '{word_with_typo}': {corrections}")
