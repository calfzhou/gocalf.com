from heapq import heapify, heapreplace


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        if multiplier == 1: return nums

        heap = [(v, i) for i, v in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            v, i = heap[0]
            heapreplace(heap, (v * multiplier, i))

        n = len(nums)
        result = [0] * n
        for v, i in heap:
            result[i] = v
        return result
