from bisect import bisect_left, bisect_right


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r and nums[l] <= nums[l+1]: l += 1
        if l == r: return 0
        while nums[r] >= nums[r-1]: r -= 1
        if r - l == n - 1: return n

        sub_min = min(nums[i] for i in range(l, r + 1))
        sub_max = max(nums[i] for i in range(l, r + 1))
        # while l > 0 and nums[l-1] > sub_min: l -= 1
        # while r < n - 1 and nums[r+1] < sub_max: r += 1
        l = bisect_right(nums, sub_min, hi=l)
        r = bisect_left(nums, sub_max, lo=r) - 1

        return r - l + 1
