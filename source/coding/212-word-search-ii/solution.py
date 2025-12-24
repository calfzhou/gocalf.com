class Trie:
    def __init__(self):
        self._root: dict[str, dict] = {}
        self._size = 0

    @property
    def root(self):
        return self._root

    @property
    def size(self):
        return self._size

    def insert(self, word: str) -> None:
        node = self._root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        if '.' not in node:
            node['.'] = None # End of a word.
            self._size += 1

    def remove(self, word: str) -> None:
        node = self._root
        stack = [node]
        for c in word:
            if c not in node:
                return
            node = node[c]
            stack.append(node)

        if '.' not in node:
            return

        self._size -= 1
        n = len(word)
        while True:
            node = stack.pop()
            c = word[len(stack)] if len(stack) < n else '.'
            del node[c]
            if node or not stack:
                return


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        m = len(board)
        n = len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        founds = []

        # Returns True if all words were found.
        def find(r: int, c: int, node: dict[str, dict], chars: list[str]) -> bool:
            if not (0 <= r < m and 0 <= c < n and (ch := board[r][c]) in node):
                return False

            node = node[ch]
            chars.append(ch)
            if '.' in node:
                word = ''.join(chars)
                founds.append(word)
                trie.remove(word)
                if trie.size == 0:
                    return True

            board[r][c] = '' # Avoid reuse the same cell.
            finished = any(find(r + dr, c + dc, node, chars) for dr, dc in dirs)
            board[r][c] = chars.pop()
            return finished

        for i in range(m):
            for j in range(n):
                if find(i, j, trie.root, []):
                    return founds

        return founds


Solution().findWords(
    [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
    ["oath","pea","eat","rain"]
)
