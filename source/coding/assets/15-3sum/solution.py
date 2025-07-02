from typing import Generator, List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negatives = []
        positives = []
        zero = 0
        for v in nums:
            if v < 0:
                negatives.append(-v)
            elif v > 0:
                positives.append(v)
            else:
                zero += 1

        negatives.sort()
        positives.sort()
        triplets = []

        if zero >= 3:
            triplets.append([0, 0, 0])

        # Find all [-, 0, +] triplets.
        if zero > 0:
            for v in self._find_all(negatives, positives):
                triplets.append([-v, 0, v])

        # Find all [-, -, +] triplets.
        for i, v_i in enumerate(negatives):
            if i > 0 and v_i == negatives[i - 1]:
                continue # Prevent duplication.

            for v_j in self._find_all(negatives, positives, i + 1, v_i):
                triplets.append([-v_i, -v_j, v_i + v_j])

        # Find all [-, +, +] triplets.
        for j, v_j in enumerate(positives):
            if j > 0 and v_j == positives[j - 1]:
                continue # Prevent duplication.

            for v_k in self._find_all(positives, negatives, j + 1, v_j):
                triplets.append([-v_j - v_k, v_j, v_k])

        return triplets

    def _find_all(self, nums1: list[int], nums2: list[int], start1: int = 0, gap: int = 0) -> Generator[int, None, None]:
        """Finds all unique v1 from nums1[start1:], where v1 + gap exists in nums2.
        Both nums1 and nums2 are sorted.
        """
        i2 = 0
        count2 = len(nums2)
        prev_v1 = None
        for i1 in range(start1, len(nums1)):
            v1 = nums1[i1]
            if v1 == prev_v1:
                continue # Prevent duplication.

            prev_v1 = v1
            while i2 < count2 and nums2[i2] < v1 + gap:
                i2 += 1

            if i2 == count2:
                return

            if nums2[i2] == v1 + gap:
                yield v1
