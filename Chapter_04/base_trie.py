class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key, value=None):
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for put: key = {key} must be a non-empty string"
            )

        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value


if __name__ == "__main__":
    trie = Trie()
    trie.put("cat", 1)
    trie.put("cat", 2)
    trie.put("dog", 3)
    trie.put("cats", 4)
