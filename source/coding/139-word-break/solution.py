from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        min_w = min(len(word) for word in wordDict)
        max_w = max(len(word) for word in wordDict)
        words = set(wordDict)

        n = len(s)
        # buffer = [[False] * n for _ in range(n)]
        buffer = set()
        for w in range(min_w, n + 1):
            for i in range(n - w + 1):
                j = i + w - 1
                can = w <= max_w and s[i:j+1] in words
                # can = can or any(buffer[i][p] and buffer[p+1][j] for p in range(i, j))
                # buffer[i][j] = can
                can = can or any((i, p) in buffer and (p + 1, j) in buffer for p in range(i, j))
                if can:
                    buffer.add((i, j))

        # return buffer[0][n - 1]
        return (0, n - 1) in buffer
