from collections import deque
from typing import Generator


class TrieNode:
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.words: dict[str, int] = {} # All {word: cost} for current node.
        self.fail: 'TrieNode' = None


class TrieTree:
    def __init__(self):
        self._root = TrieNode()

    def add(self, word: str, cost: int) -> None:
        node = self._root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]

        if word not in node.words or node.words[word] > cost:
            node.words[word] = cost

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

                # Set failure link, and remember words.
                child.fail = fail.children[c] if fail else self._root
                child.words |= child.fail.words

    def match(self, target: str) -> Generator[tuple[int, int, int], None, None]:
        """Finds all matched words in target, yields (start, end, cost) of each match."""
        node = self._root
        for i, c in enumerate(target):
            # Follow failure links until a match is found.
            while node and c not in node.children:
                node = node.fail

            if not node:
                node = self._root
                continue

            # Move to the next node base on current character.
            node = node.children[c]
            for word, cost in node.words.items():
                yield i + 1 - len(word), i + 1, cost


class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        trie = TrieTree()
        for word, cost in zip(words, costs): trie.add(word, cost)
        trie.build_ac()

        n = len(target)
        dp = [-1] * (n + 1)
        dp[0] = 0
        for i, j, cost in trie.match(target):
            if dp[i] < 0: continue
            if dp[j] < 0 or dp[j] > dp[i] + cost:
                dp[j] = dp[i] + cost

        return dp[n]
