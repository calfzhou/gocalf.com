class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        a2 = 0
        b = int(c ** 0.5)
        b2 = b * b
        while a <= b:
            if (s := a2 + b2) == c:
                return True
            elif s > c:
                b -= 1
                b2 = b * b
            else:
                a += 1
                a2 = a * a

        return False
