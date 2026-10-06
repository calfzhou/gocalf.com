from collections import deque
from typing import Generator


class TrieNode:
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.level = 0
        self.fail: 'TrieNode' = None


class TrieTree:
    def __init__(self):
        self._root = TrieNode()

    def add(self, word: str) -> None:
        node = self._root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
                node.children[c].level = node.level + 1
            node = node.children[c]

    def build_ac(self) -> None:
        """Builds failure links for ac-machine using BFS."""
        queue = deque()
        for node in self._root.children.values():
            queue.append(node)
            node.fail = self._root

        # Breadth-first traversal of the trie.
        while len(queue):
            node = queue.popleft()
            for c, child in node.children.items():
                queue.append(child)
                fail = node.fail

                # Find the longest proper suffix that is also a prefix.
                while fail and c not in fail.children:
                    fail = fail.fail

                # Set failure link.
                child.fail = fail.children[c] if fail else self._root

    def prefix(self, target: str) -> Generator[tuple[int, int], None, None]:
        """Finds all matched prefix in target, yields (start, end), where target[start:end] is a prefix.
        For 0 <= i < k < j < n, if target[i:k], target[k:j], and target[i:j] are all prefixes, (k, j) will be ignore.
        """
        node = self._root
        for i, c in enumerate(target):
            # Follow failure links until a match is found.
            while node and c not in node.children:
                node = node.fail

            if not node:
                node = self._root
                continue
            else:
                yield i - node.level, i + 1

            # Move to the next node based on current character.
            node = node.children[c]


class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        trie = TrieTree()
        for word in words: trie.add(word)
        trie.build_ac()

        n = len(target)
        dp = [-1] * (n + 1)
        dp[0] = 0
        for i, j in trie.prefix(target):
            if dp[i] < 0: continue
            if dp[j] < 0 or dp[j] > dp[i] + 1:
                dp[j] = dp[i] + 1

        return dp[n]
