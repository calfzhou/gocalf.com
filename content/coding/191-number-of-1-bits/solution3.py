class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            cnt += 1
            n &= n - 1

        return cnt
