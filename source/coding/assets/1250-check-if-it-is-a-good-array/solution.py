from math import gcd


class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        return gcd(*nums) == 1
