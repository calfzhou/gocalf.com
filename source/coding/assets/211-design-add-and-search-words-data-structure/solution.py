class WordDictionary:
    def __init__(self):
        self._root: dict[str, dict] = {}

    def addWord(self, word: str) -> None:
        node = self._root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        node['#'] = None # End of a word.

    def search(self, word: str) -> bool:
        n = len(word)

        def backtrack(i: int, node: dict[str, dict]) -> bool:
            if i == n:
                return '#' in node
            elif (c := word[i]) == '.':
                return any(backtrack(i + 1, child) for key, child in node.items() if key != '#')
            elif c not in node:
                return False
            else:
                return backtrack(i + 1, node[c])

        return backtrack(0, self._root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
