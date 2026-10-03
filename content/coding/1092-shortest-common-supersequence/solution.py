class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        lcs = [[0] * (n + 1) for _ in range(m + 1)]
        for i, c1 in enumerate(str1, 1):
            for j, c2 in enumerate(str2, 1):
                if c1 == c2:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                else:
                    lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

        res: list[str] = []
        i, j = m, n
        while i > 0 and j > 0:
            if lcs[i][j] == lcs[i-1][j]:
                res.append(str1[i-1])
                i -= 1
            elif lcs[i][j] == lcs[i][j-1]:
                res.append(str2[j-1])
                j -= 1
            else:
                res.append(str1[i-1])
                i -= 1
                j -= 1

        while i > 0:
            res.append(str1[i-1])
            i -= 1

        while j > 0:
            res.append(str2[j-1])
            j -= 1

        return ''.join(reversed(res))
