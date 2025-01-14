from heapq import heapify, heappop, heapreplace


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapify(nums)
        cnt = 0
        while nums[0] < k:
            x = heappop(nums)
            heapreplace(nums, (x << 1) + nums[0])
            cnt += 1

        return cnt
