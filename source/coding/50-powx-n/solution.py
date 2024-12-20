class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: x, n = 1 / x, -n

        res = 1
        while n > 0:
            if n & 1:
                res *= x
            n >>= 1
            x *= x

        return res
