from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda interval: interval[1])

        res = 1
        right = intervals[0][1]
        for i in range(1, n):
            start, end = intervals[i]
            if start >= right:
                right = end
                res += 1

        return n - res
