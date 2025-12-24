class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) >> 1
            if nums[m] == target:
                return True
            elif nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            elif (nums[l] <= target < nums[m]) or (nums[l] > nums[m] and (nums[l] <= target or target < nums[m])):
                r = m - 1
            else:
                l = m + 1

        return False
