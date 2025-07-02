from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        lcs = 0
        for v in num_set:
            # Check if v is the min number of a sequence.
            # If not, ignore it.
            if v - 1 in num_set:
                continue

            # Found the min number of a sequence, iterate this sequence to get its length.
            length = 1
            v += 1
            while v in num_set:
                v += 1
                length += 1

            lcs = max(lcs, length)

        return lcs
