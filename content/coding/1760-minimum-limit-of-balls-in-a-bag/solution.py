from heapq import heapify, heappop, heappush
from math import ceil


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        if len(nums) == 1:
            return ceil(nums[0] / (maxOperations + 1))

        target = ceil(sum(nums) / (maxOperations + 1))
        queue = [None] * len(nums)
        for i, a in enumerate(nums):
            k = ceil(a / target) - 1
            maxOperations -= k
            queue[i] = (-ceil(a / (k + 1)), a)

        heapify(queue)
        while maxOperations > 0 and queue[0][0] < -1:
            a, raw = heappop(queue)
            if raw != -a:
                maxOperations += ceil(raw / -a) - 1

            b = -queue[0][0] - 1
            if b == 0:
                b = 1

            k = ceil(raw / b) - 1
            if k > maxOperations:
                k = maxOperations

            r = ceil(raw / (k + 1))
            maxOperations -= k
            heappush(queue, (-r, raw))

        return -queue[0][0]
