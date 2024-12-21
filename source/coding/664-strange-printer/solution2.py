from bisect import bisect_left
from functools import cache


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

        @cache
        def dfs(l: int, r: int) -> int:
            if l >= r: return 0
            elif l == r - 1: return 1

            min_cnt = 1 + dfs(l+1, r)

            occ = occurs[ss[l]]
            for k in occ[bisect_left(occ, l)+1:]:
                if k >= r: break
                min_cnt = min2(min_cnt, dfs(l, k) + dfs(k+1, r))

            return min_cnt

        return dfs(0, len(ss))
