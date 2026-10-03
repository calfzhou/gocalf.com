from bisect import bisect_right
from collections import defaultdict
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

        queue = [(m, cnt) for m, cnt in counts.items() if m > 2]
        if not queue: return 2

        queue.sort()
        q = len(queue)
        l = 2
        r = queue[-1][0]
        while l <= r:
            mid = (l + r) >> 1
            i = bisect_right(queue, (mid,)) # ∀queue[i:][0] > mid
            k = sum(ceil((queue[j][0] - mid) / (mid + 1)) * queue[j][1] for j in range(i, q))
            if k > numOps:
                l = mid + 1
            else:
                r = mid - 1

        return r + 1
