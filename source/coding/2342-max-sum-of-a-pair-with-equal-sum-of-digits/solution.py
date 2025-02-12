from collections import defaultdict
from heapq import heappush, heappushpop


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        max2 = lambda a, b: a if a >= b else b
        groups: dict[int, list[int]] = defaultdict(list)
        for num in nums:
            sd = 0
            val = num
            while val > 0:
                sd += val % 10
                val //= 10

            group = groups[sd]
            if not group:
                group.append(num)
            elif len(group) == 1:
                heappush(group, num)
            else:
                heappushpop(group, num)

        max_sum = -1
        for group in groups.values():
            if len(group) > 1:
                max_sum = max2(max_sum, group[0] + group[1])

        return max_sum
