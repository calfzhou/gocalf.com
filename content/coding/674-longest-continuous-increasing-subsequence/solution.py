class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        max_len = 1
        prev = nums[0]
        curr_len = 1
        for num in nums:
            if num > prev:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            else:
                curr_len = 1

            prev = num

        return max_len
