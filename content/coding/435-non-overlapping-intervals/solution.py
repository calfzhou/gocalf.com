from typing import List


def bin_find_max_le(intervals: list[list[int]], end: int, val: int) -> int:
    """Finds the maximal position i in `intervals[0:end]`, where `intervals[i][1] <= val`, using binary search.
    `intervals[:][1]` are ordered, but may contain duplicate values.
    Returns `-1` if val is smaller than all `intervals[:][1]`.
    """
    l = 0
    r = end - 1
    while l <= r:
        m = (l + r) >> 1
        if (t := intervals[m][1]) == val:
            while m < r and intervals[m+1][1] == val:
                m += 1
            return m
        elif t > val:
            r = m - 1
        elif val >= intervals[r][1]:
            return r
        else:
            l = m + 1

    return l - 1


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda interval: interval[1])

        counts = [1] * n
        results = [1] * n
        for i in range(1, n):
            start = intervals[i][0]
            j = bin_find_max_le(intervals, i, start)
            if j >= 0:
                counts[i] = max(counts[i], results[j] + 1)
            results[i] = max(counts[i], results[i - 1])

        return n - results[n - 1]
