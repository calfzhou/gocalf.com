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
        i = 0
        node = self._root
        stack = []
        while node or stack:
            if not node:
                i, node = stack.pop()

            if i == n:
                if '#' in node:
                    return True
                else:
                    node = None
            elif (c := word[i]) == '.':
                stack.extend((i + 1, child) for key, child in node.items() if key != '#')
                node = None
            else:
                i += 1
                node = node.get(c)

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
