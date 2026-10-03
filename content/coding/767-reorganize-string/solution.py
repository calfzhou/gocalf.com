from heapq import heapify, heappop, heappush, heapreplace
from typing import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if max(counts.values()) > ((len(s) + 1) >> 1):
            return ''

        parts = []
        queue = [(-f, c) for c, f in counts.items()]
        heapify(queue)
        while len(queue) > 1:
            f1, c1 = heappop(queue)
            f2, c2 = queue[0]
            parts.append(c1)
            parts.append(c2)
            f1 += 1
            f2 += 1
            if f2:
                heapreplace(queue, (f2, c2))
                heappush(queue, (f1, c1))
            elif f1:
                heapreplace(queue, (f1, c1))
            else:
                heappop(queue)

        if queue:
            parts.append(queue[0][1])

        return ''.join(parts)
