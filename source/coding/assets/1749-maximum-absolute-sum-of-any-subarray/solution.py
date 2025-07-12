min2 = lambda a, b: a if a <= b else b
max2 = lambda a, b: a if a >= b else b


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        sl = largest = nums[0]
        ss = smallest = nums[0]
        for i in range(1, len(nums)):
            sl = max2(sl, 0) + nums[i]
            largest = max2(largest, sl)

            ss = min2(ss, 0) + nums[i]
            smallest = min2(smallest, ss)

        return max2(largest, -smallest)
