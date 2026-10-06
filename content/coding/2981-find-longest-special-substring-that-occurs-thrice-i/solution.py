from collections import defaultdict
from heapq import heapreplace


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        top3s: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0]) # char: its three longest continuous pieces.
        prev = s[0]
        cnt = 1
        for i in range(1, n + 1):
            if i < n and (c := s[i]) == prev:
                cnt += 1
                continue

            if cnt > top3s[prev][0]:
                heapreplace(top3s[prev], cnt)

            if i < n:
                prev = c
                cnt = 1

        max_len = 0
        for x, y, z in top3s.values():
            if y == z:
                cnt = z if z == x else z - 1
            else:
                if y > z:
                    y, z = z, y
                cnt = max(y, z - 2)

            if cnt > max_len:
                max_len = cnt

        return max_len or -1
