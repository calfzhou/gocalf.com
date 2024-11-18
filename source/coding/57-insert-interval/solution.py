class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        after = self._bin_find_max_lt(intervals, newInterval[0])
        i = after + 1
        if i < len(intervals):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            while i < len(intervals) and intervals[i][0] <= newInterval[1]:
                i += 1
            if i > after + 1:
                newInterval[1] = max(newInterval[1], intervals[i-1][1])

        intervals[after+1:i] = [newInterval]
        return intervals

    def _bin_find_max_lt(self, intervals: list[list[int]], val: int) -> int:
        """Finds the maximal index i, where `intervals[i][1] < val`, using binary search.
        `intervals[:][1]` are ordered **distinct** integers.
        Returns `-1` if val is smaller than all `intervals[:][1]`.
        """
        l = 0
        r = len(intervals) - 1
        while l <= r:
            m = (l + r) >> 1
            if intervals[m][1] >= val:
                r = m - 1
            elif val > intervals[r][1]:
                return r
            else:
                l = m + 1

        return l - 1
