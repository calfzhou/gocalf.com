class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        powers = [-1] * (n - k + 1)
        length = 0
        for i in range(0, n):
            if i == 0 or nums[i] != nums[i-1] + 1:
                length = 1
            elif length < k:
                length += 1

            if length == k:
                powers[i - k + 1] = nums[i]
        return powers
