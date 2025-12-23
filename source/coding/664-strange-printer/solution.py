from bisect import bisect_left


class Solution:
    def strangePrinter(self, s: str) -> int:
        min2 = lambda a, b: a if a <= b else b
        ss: list[int] = [] # `ss` is `s` without consecutive identical characters.
        occurs: list[list[int]] = [[] for _ in range(26)] # occurs[char]: char's occurrences in ss
        prev = ''
        for c in s:
            if c == prev: continue
            val = ord(c) - 97
            occurs[val].append(len(ss))
            ss.append(val)
            prev = c

        n = len(ss)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                dp[i][j] = 1 + dp[i+1][j]
                if ss[j] == ss[i]: dp[i][j] = min2(dp[i][j], dp[i][j-1])

                occ = occurs[ss[i]]
                for k in occ[bisect_left(occ, i)+1:]:
                    if k >= j: break
                    dp[i][j] = min2(dp[i][j], dp[i][k-1] + dp[k+1][j])

        return dp[0][n-1]
