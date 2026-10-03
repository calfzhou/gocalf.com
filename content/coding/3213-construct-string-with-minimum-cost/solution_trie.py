from typing import Generator


class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        trie: dict[str, dict] = {}
        n = len(target)

        def trie_add(word: str, cost: int) -> None:
            node = trie
            for c in word:
                if c not in node: node[c] = {}
                node = node[c]

            if '#' not in node or node['#'] > cost:
                node['#'] = cost

        def trie_lookup(start: int) -> Generator[tuple[int, int], None, None]:
            node = trie
            if '#' in node: yield start, node['#']
            while start < n and target[start] in node:
                node = node[target[start]]
                start += 1
                if '#' in node: yield start, node['#']

        for word, cost in zip(words, costs):
            trie_add(word, cost)

        dp = [-1] * (n + 1)
        dp[-1] = 0
        for left in range(n - 1, -1, -1):
            for right, cost in trie_lookup(left):
                if dp[right] < 0: continue
                if not 0 < dp[left] < cost + dp[right]:
                    dp[left] = cost + dp[right]

        return dp[0]
