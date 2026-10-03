class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums) - k
        k_sums = [0] * (n + 1) # k_sums[i] = sum(nums[i:i+k])
        r_bests = [0] * (n + 1) # r_bests[i] = index of max(k_sums[i:])

        k_sums[n] = sum(nums[i] for i in range(n, n+k))
        r_bests[n] = n
        for i in range(n-1, -1, -1):
            k_sums[i] = k_sums[i+1] - nums[i+k] + nums[i]
            r_bests[i] = i if k_sums[i] >= k_sums[r_bests[i+1]] else r_bests[i+1]

        l_best = 0
        max_triple = 0
        choice = []
        for m in range(k, n-k+1):
            l, r = m - k, m + k
            if k_sums[l] > k_sums[l_best]:
                l_best = l

            if (s := k_sums[l_best] + k_sums[m] + k_sums[r_bests[r]]) > max_triple:
                max_triple = s
                choice = [l_best, m, r_bests[r]]

        return choice
