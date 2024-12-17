from typing import Generator


class TrieNode:
    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.cost = None


class TrieTree:
    def __init__(self):
        self._root = TrieNode()

    def add(self, word: str, cost: int) -> None:
        node = self._root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]

        if node.cost is None or node.cost > cost:
            node.cost = cost

    def lookup(self, target: str, start: int) -> Generator[tuple[int, int], None, None]:
        node = self._root
        n = len(target)
        while start < n and target[start] in node.children:
            node = node.children[target[start]]
            start += 1
            if node.cost: yield start, node.cost


class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        ac = TrieTree() # TODO

        for word, cost in zip(words, costs):
            ac.add(word, cost)

        n = len(target)
        dp = [-1] * (n + 1)
        dp[-1] = 0
        for left in range(n - 1, -1, -1):
            for right, cost in ac.lookup(target, left):
                if dp[right] < 0: continue
                if not 0 < dp[left] < cost + dp[right]:
                    dp[left] = cost + dp[right]

        return dp[0]
