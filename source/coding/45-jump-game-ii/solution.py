class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            dp[i] = 1 + min(dp[i + 1:i + nums[i] + 1], default=n)

        return dp[0]
