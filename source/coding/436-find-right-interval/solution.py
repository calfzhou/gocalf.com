from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        indices = sorted(range(n), key=lambda i: intervals[i][0])
        ans = [-1] * n
        for idx, i in enumerate(indices):
            j = bisect_left(indices, intervals[i][1], lo=idx, key=lambda j: intervals[j][0])
            if j < n:
                ans[i] = indices[j]

        return ans
