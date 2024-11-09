from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        indices = list(range(n))
        indices.sort(key=lambda i: nums[i])

        for i, p1 in enumerate(indices):
            v2 = target - nums[p1]
            p2 = self._bin_find(nums, indices, v2, i + 1)
            if p2 is not None:
                return [p1, p2]

        return []

    def _bin_find(self, nums: List[int], indices: List[int], value: int, left: int) -> int | None:
        l = left
        if l >= len(indices) or (t := nums[indices[l]]) > value:
            return None
        elif t == value:
            return indices[l]

        r = len(indices) - 1
        if (t := nums[indices[r]]) < value:
            return None
        elif t == value:
            return indices[r]

        while l <= r:
            m = (l + r) >> 1
            if (t := nums[indices[m]]) == value:
                return indices[m]
            elif t < value:
                l = m + 1
            else:
                r = m - 1

        return None
