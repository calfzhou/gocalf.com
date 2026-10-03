from functools import reduce
import operator


class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        res = 0
        if len(nums1) & 1: res = reduce(operator.xor, nums2, res)
        if len(nums2) & 1: res = reduce(operator.xor, nums1, res)
        return res
