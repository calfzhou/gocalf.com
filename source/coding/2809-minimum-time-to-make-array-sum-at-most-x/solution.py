class Solution:
    def minimumTime(self, nums1: list[int], nums2: list[int], x: int) -> int:
        if (total := sum(nums1)) <= x: return 0
        s2 = sum(nums2)

        n = len(nums1)
        indices = sorted(range(n), key=lambda i: nums2[i])
        nums1 = [nums1[i] for i in indices]
        nums2 = [nums2[i] for i in indices]

        dp = [0] * n
        for t in range(1, n + 1):
            for j in range(t-1, n):
                v = nums1[j] + t * nums2[j]
                j -= t - 1
                if t > 1:
                    v += dp[j]
                if j > 0 and dp[j-1] > v:
                    v = dp[j-1]
                dp[j] = v

            total += s2
            if total - dp[n-t] <= x:
                return t

        return -1
