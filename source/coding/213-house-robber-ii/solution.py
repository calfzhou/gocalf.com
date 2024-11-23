class Solution:
    def rob(self, nums: list[int]) -> int:
        if (n := len(nums)) == 1:
            return nums[0]

        # pp means i - 2, p means i - 1.
        t_pp, t_p = 0, nums[0] # t for nums[0:n-1].
        t1_pp, t1_p = 0, 0 # t1 for nums[1:n].
        for i in range(1, n):
            t_pp, t_p = t_p, max(t_p, t_pp + nums[i])
            t1_pp, t1_p = t1_p, max(t1_p, t1_pp + nums[i])

        return max(t_pp, t1_p)
