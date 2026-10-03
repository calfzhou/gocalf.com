from functools import reduce


class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        def _gcd(a: int, b: int) -> int:
            while a % b > 0: a, b = b, a % b
            return b

        return reduce(_gcd, nums) == 1
