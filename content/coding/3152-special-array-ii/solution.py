class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        dp = [1] * n
        prev = nums[0] & 1
        for i in range(1, n):
            if prev != (prev := nums[i] & 1):
                dp[i] += dp[i - 1]

        return [f > t - dp[t] for f, t in queries]
