class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pl = [1] * n
        pr = [1] * n
        for i in range(1, n):
            pl[i] = pl[i-1] * nums[i-1]
            j = n - 1 - i
            pr[j] = pr[j+1] * nums[j+1]

        return [pl[i] * pr[i] for i in range(n)]
