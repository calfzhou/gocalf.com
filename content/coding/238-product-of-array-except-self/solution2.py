class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        has_zero = False
        prod = 1
        for val in nums:
            if val == 0:
                if has_zero:
                    return [0] * n
                has_zero = True
            else:
                prod *= val

        if has_zero:
            return [not val and prod or 0 for val in nums]

        return [prod // val for val in nums]
