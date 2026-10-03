from heapq import nlargest, nsmallest


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        largest3 = nlargest(3, nums)
        smallest2 = nsmallest(2, nums)
        a = largest3[0] * largest3[1] * largest3[2]
        b = smallest2[0] * smallest2[1] * largest3[0]
        return a if a >= b else b
