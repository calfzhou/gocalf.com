class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if (n ^ k) & k:
            return -1

        r = (n ^ k) & n
        cnt = 0
        while r > 0:
            cnt += 1
            r &= r - 1

        return cnt
