class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        l = r = 2
        while r < n:
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1
            r += 1

        return l
