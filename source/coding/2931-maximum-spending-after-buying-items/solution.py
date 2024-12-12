from heapq import heapify, heappop, heapreplace


class Solution:
    def maxSpending(self, values: list[list[int]]) -> int:
        m = len(values)
        n = len(values[0])
        heap = [(values[i][-1], n-1, i) for i in range(m)]
        heapify(heap)

        amt = 0
        for d in range(1, m * n + 1):
            price, j, i = heap[0]
            amt += price * d
            if j == 0:
                heappop(heap)
            else:
                j -= 1
                heapreplace(heap, (values[i][j], j, i))

        return amt
