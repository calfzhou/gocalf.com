from collections import defaultdict


class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        occurs: dict[int, int] = defaultdict(int) # {num, freq}
        for num in nums:
            occurs[num] += 1
            if occurs[num] > 2:
                return False

        return True
