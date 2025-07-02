from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l < r - 1:
            m = (l + r) >> 1
            v_l, v, v_r = nums[m-1:m+2]
            if v_l != v != v_r:
                return v

            if (m - l) & 1 == 0:
                # Even elements in each half array.
                if v == v_l:
                    # v_l is not single, remove it, then left half remains odd elements, check left half.
                    r = m - 1
                else:
                    # Otherwise, check right half.
                    l = m + 2
            else:
                # Odd elements in each half array.
                if v == v_l:
                    # v_l is not single, remove it, then right half still has odd elements, check right half.
                    l = m + 1
                else:
                    # Otherwise, check left half.
                    r = m

        return nums[l]
