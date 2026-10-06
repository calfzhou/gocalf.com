from typing import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        occ = Counter(s)
        t = Counter()
        for i in range(n >> 1):
            t[s[i]] += 1
            i += 1
            if n % i or any(t[c] == 0 or f % t[c] for c, f in occ.items()):
                continue

            for j in range(i, n, i):
                if Counter(s[j:j+i]) != t:
                    break
            else:
                return i

        return n
