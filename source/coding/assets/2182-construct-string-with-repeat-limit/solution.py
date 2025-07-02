from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        chars = sorted(counts, reverse=True)
        m = len(chars)
        parts = []
        i = 0
        j = 1
        while i < m:
            c = chars[i]
            k = min(counts[c], repeatLimit)
            parts.append(c * k)
            counts[c] -= k
            if counts[c] > 0:
                if j == m: break
                c2 = chars[j]
                parts.append(c2)
                counts[c2] -= 1
                if counts[c2] == 0: j += 1
            else:
                i, j = j, j + 1

        return ''.join(parts)
