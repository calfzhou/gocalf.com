max2 = lambda a, b: a if a >= b else b


class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        s = set(arr)
        longest = 0
        dp: dict[tuple[int, int], int] = {}
        for k, z in enumerate(arr):
            for j in range(k - 1, -1, -1):
                y = arr[j]
                x = z - y
                if x >= y:
                    break
                if x in s:
                    dp[y, z] = dp.get((x, y), 2) + 1
                    longest = max2(longest, dp[y, z])

        return longest
