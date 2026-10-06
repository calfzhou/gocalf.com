from collections import defaultdict
from heapq import heapify, heappop, heappush
from math import ceil


class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        # Check whether the length of longest substring could be 1.
        # It needs `k` operations on `s` to change it to '010101...'.
        # So, `n - k` operations to change it to '101010...'.
        k = sum(i & 1 ^ int(c) for i, c in enumerate(s))
        if k <= numOps or n - k <= numOps: return 1

        counts: dict[int, int] = defaultdict(int) # substring length: freq
        i = 0
        for j in range(1, n + 1):
            if j == n or s[j] != s[i]:
                counts[j - i] += 1
                i = j

        queue = [(-m, cnt, m) for m, cnt in counts.items() if m > 2] # Max-heap.
        if not queue: return 2

        min2 = lambda a, b: a if a <= b else b
        max2 = lambda a, b: a if a >= b else b

        heapify(queue)
        while numOps > 0 and queue[0][0] < -2:
            a, cnt, m = heappop(queue)
            if m != -a:
                numOps += ceil((m + a) / (1 - a)) * cnt

            b = -queue[0][0] - 1 if queue else 2
            if b == 1: b = 2

            k = ceil((m - b) / (b + 1))
            op = min2(k * cnt, numOps)
            k, r = divmod(op, cnt)

            if r > 0:
                a = ceil((m - k - 1) / (k + 2))
                numOps -= (k + 1) * r
                heappush(queue, (-a, r, m))
                cnt -= r

            a = ceil((m - k) / (k + 1))
            numOps -= k * cnt
            heappush(queue, (-a, cnt, m))

        return max2(-queue[0][0], 2)
