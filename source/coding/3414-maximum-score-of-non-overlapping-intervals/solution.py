from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        indices = sorted(range(n), key=lambda i: intervals[i][1])
        dp = [[(0, []) for _ in range(n+1)] for _ in range(4)]

        for i in range(n):
            interval = intervals[indices[i]]
            j = bisect_left(indices, interval[0], hi=i, key=lambda i: intervals[i][1])
            prev = (0, []) # dp[k-1][j]
            for k in range(4):
                dp[k][i+1] = dp[k][i]
                score_j = prev[0] + interval[2]
                if score_j > dp[k][i][0]:
                    dp[k][i+1] = score_j, prev[1] + [indices[i]]
                elif score_j == dp[k][i][0]:
                    selection_j = sorted(prev[1] + [indices[i]])
                    dp[k][i][1].sort()
                    if selection_j < dp[k][i][1]:
                        dp[k][i+1] = score_j, selection_j

                prev = dp[k][j]

        return sorted(dp[3][n][1])
