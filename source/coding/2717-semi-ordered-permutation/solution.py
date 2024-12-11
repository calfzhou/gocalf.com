class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        n = len(nums)
        a = b = -1
        for i, v in enumerate(nums):
            if v == 1:
                a = i
                if b >= 0:
                    a -= 1
                    break
            elif v == n:
                b = n - 1 - i
                if a >= 0:
                    break

        return a + b
