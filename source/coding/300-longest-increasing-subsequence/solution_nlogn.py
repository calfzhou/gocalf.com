from typing import List


def bin_find_min_ge(nums: list[int], val: int) -> int:
    """Finds the minimal position i in `nums`, where `nums[i] >= val`, using binary search.
    `nums` contains ordered **distinct** integers.
    Returns `len(nums)` if val is larger than all values in `nums`.
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) >> 1
        if (t := nums[m]) == val:
            return m
        elif t < val:
            l = m + 1
        elif val <= nums[l]:
            return l
        else:
            r = m - 1

    return r + 1


class Solution:
    # `O(n log n)` time, `O(n)` extra space.
    def lengthOfLIS(self, nums: List[int]) -> int:
        buffer = []
        for val in nums:
            i = bin_find_min_ge(buffer, val)
            if i < len(buffer):
                buffer[i] = val
            else:
                buffer.append(val)

        return len(buffer)
