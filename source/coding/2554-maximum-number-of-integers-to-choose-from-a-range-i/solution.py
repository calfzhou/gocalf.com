class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        skips = set(banned) # or: set(v for v in banned if 1 <= v <= n), but slower
        cnt = 0
        for v in range(1, n + 1):
            if v in skips: continue
            maxSum -= v
            if maxSum < 0: break
            cnt += 1

        return cnt
