from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        counts: dict[int, int] = defaultdict(int) # nums[i] - i -> count
        for i, num in enumerate(nums):
            counts[num - i] += 1

        n = len(nums)
        total = n * (n - 1) // 2
        for count in counts.values():
            total -= count * (count - 1) // 2

        return total
