class Trie:
    def __init__(self):
        self._root: dict[str, dict] = {}

    def insert(self, word: str) -> None:
        node = self._root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        node['.'] = None # End of a word.

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and '.' in node

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, word: str) -> dict | None:
        node = self._root
        for c in word:
            if c not in node:
                return None
            node = node[c]

        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
