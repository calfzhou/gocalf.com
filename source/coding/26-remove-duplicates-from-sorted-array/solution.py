class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        l = r = 1
        while r < n:
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1

        return l
