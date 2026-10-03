class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        lcs = [[0] * (n + 1) for _ in range(m + 1)]
        for i, c1 in enumerate(text1, 1):
            for j, c2 in enumerate(text2, 1):
                if c1 == c2:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                else:
                    lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

        return lcs[m][n]
