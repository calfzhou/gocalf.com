class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        s = sum(nums)
        target2 = s + target
        if s < abs(target) or target2 & 1: return 0
        target2 >>= 1

        dp = [0] * (target2 + 1)
        dp[0] = 1
        for num in nums:
            for t in range(target2, num - 1, -1):
                dp[t] += dp[t - num]

        return dp[target2]
