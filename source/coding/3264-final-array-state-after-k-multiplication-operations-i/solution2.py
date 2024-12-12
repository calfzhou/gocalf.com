from heapq import heapify, heapreplace


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        if multiplier == 1: return nums

        for _ in range(k):
            i = nums.index(min(nums))
            nums[i] *= multiplier
        return nums
