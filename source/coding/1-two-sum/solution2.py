from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        half = target >> 1 if target & 1 == 0 else None
        for i, v in enumerate(nums):
            # Special treatment of `target / 2` when target is even.
            if half is not None and v == half and v in indices:
                return [indices[v], i]

            indices[v] = i

        for i, v1 in enumerate(nums):
            if half is not None and v1 == half:
                continue

            v2 = target - v1
            if v2 in indices:
                return i, indices[v2]

        return []
