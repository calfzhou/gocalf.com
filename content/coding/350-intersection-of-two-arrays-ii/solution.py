from collections import defaultdict


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        min2 = lambda a, b: a if a <= b else b

        d1 = defaultdict(int)
        for num in nums1:
            d1[num] += 1

        d2 = defaultdict(int)
        for num in nums2:
            d2[num] += 1

        result = []
        for num, f1 in d1.items():
            if num in d2:
                f2 = d2[num]
                result.extend([num] * min2(f1, f2))

        return result
