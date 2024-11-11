from typing import Generator, List


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children: dict[str, 'TrieNode'] = {}


class TrieTree:
    def __init__(self, words: list[str]):
        self._root = TrieNode()
        for word in words:
            self.add(word)

    def add(self, word: str):
        node = self._root
        for c in word:
            if (child := node.children.get(c)) is None:
                child = node.children[c] = TrieNode()

            node = child

        node.is_word = True

    def lookup(self, text: str, start: int) -> Generator[int, None, None]:
        node = self._root
        if node.is_word:
            yield start

        n = len(text)
        while start < n:
            node = node.children.get(text[start])
            if node is None:
                break

            start += 1
            if node.is_word:
                yield start


class Solution():
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        min_w = min(len(word) for word in wordDict)
        tree = TrieTree(wordDict)

        n = len(s)
        buffer = [False] * n
        for i in range(n - min_w, -1, -1):
            for p in tree.lookup(s, i):
                if p == n or buffer[p]:
                    buffer[i] = True
                    break

        return buffer[0]
