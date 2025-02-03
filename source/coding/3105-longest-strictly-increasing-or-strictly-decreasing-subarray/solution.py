class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        longest = 0
        current = 0
        dir = 0
        prev = nums[0]
        for num in nums:
            if num == prev:
                current = 1
                dir = 0
            elif num > prev:
                current = current + 1 if dir >= 0 else 2
                dir = 1
            else:
                current = current + 1 if dir <= 0 else 2
                dir = -1

            longest = max2(longest, current)
            prev = num

        return longest
