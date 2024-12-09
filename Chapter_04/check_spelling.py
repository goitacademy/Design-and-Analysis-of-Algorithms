from trie import Trie


def check_spelling(trie, word):
    if not isinstance(word, str) or not word:
        raise TypeError(
            f"Illegal argument for contains: key = {word} must be a non-empty string"
        )
    return trie.get(word) is not None


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

# Приклади використання перевірки орфографії
words_to_check = ["apple", "app", "banner", "bat", "batman"]
for word in words_to_check:
    if check_spelling(trie, word):
        print(f"'{word}' написане правильно.")
    else:
        print(f"'{word}' не знайдено в словнику.")
