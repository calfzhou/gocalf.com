from typing import List


def bin_find_min_ge(nums: list[int], end: int, val: int) -> int:
    """Finds the minimal position i in `nums[0:end]`, where `nums[i] >= val`, using binary search.
    `nums` contains ordered **distinct** integers.
    Returns `end` if val is larger than all values in `nums[0:end]`.
    """
    l = 0
    r = end - 1
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
    # `O(n log n)` time, `O(1)` extra space.
    def lengthOfLIS(self, nums: List[int]) -> int:
        end = 0
        for val in nums:
            i = bin_find_min_ge(nums, end, val)
            nums[i] = val
            if i == end:
                end += 1

        return end
