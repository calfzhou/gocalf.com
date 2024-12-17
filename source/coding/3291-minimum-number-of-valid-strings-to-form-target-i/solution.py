class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        trie: dict[str, dict] = {}
        n = len(target)

        def trie_add(word: str) -> None:
            node = trie
            for c in word:
                if c not in node: node[c] = {}
                node = node[c]

        def trie_match(left: int) -> int:
            """Returns the maximum length k, where trie.startsWith(target[left:left+k])"""
            node = trie
            curr = left
            while curr < n and target[curr] in node:
                node = node[target[curr]]
                curr += 1
            return curr - left

        for word in words:
            trie_add(word)

        dp = [-1] * (n + 1)
        dp[-1] = 0
        for left in range(n - 1, -1, -1):
            plen = trie_match(left)
            for right in range(left + 1, left + plen + 1):
                if dp[right] < 0: continue
                if not 0 < dp[left] < 1 + dp[right]:
                    dp[left] = 1 + dp[right]

        return dp[0]
