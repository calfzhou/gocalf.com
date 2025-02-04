class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        i, j = 0, 1
        while i < n and j < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 != 0:
                j += 2
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]

        return nums
