class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        max_sum = 0
        s = 0
        prev = nums[0]
        for num in nums:
            if num > prev:
                s += num
            else:
                s = num

            max_sum = max2(max_sum, s)
            prev = num

        return max_sum
