from functools import cache


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 1_000_000_007
        CHARS = 'abcd'
        n = len(s)

        c_lasts = {c: [-1] * n for c in CHARS}
        c_firsts = {c: [n] * n for c in CHARS}
        c_lasts[s[0]][0] = 0
        c_firsts[s[n-1]][n-1] = n-1
        for i in range(1, n):
            j = n - i - 1
            for c in CHARS:
                c_lasts[c][i] = c_lasts[c][i-1]
                c_firsts[c][j] = c_firsts[c][j+1]

            c_lasts[s[i]][i] = i
            c_firsts[s[j]][j] = j

        @cache
        def dp(left: int, right: int) -> int:
            if left > right: return 0

            cnt = 0
            for c in CHARS:
                first = c_firsts[c][left]
                last = c_lasts[c][right]
                if first > right or last < left:
                    continue

                cnt += 1 # The single-char palindromic `c`.
                if first < last:
                    cnt += dp(first + 1, last - 1) + 1 # Plus the empty subsequence.

            return cnt % MOD

        return dp(0, n - 1)
