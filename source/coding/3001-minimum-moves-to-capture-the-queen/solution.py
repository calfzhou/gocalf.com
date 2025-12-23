class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # Rook and queen in the same row or col, and bishop not between them.
        if e == a and not (e == c and (b < d < f or b > d > f)):
            return 1
        if f == b and not (f == d and (a < c < e or a > c > e)):
            return 1

        # bishop and queen in the same diagonal line, and rook not between them.
        if e + f == c + d and not (e + f == a + b and (c < a < e or c > a > e)):
            return 1
        if e - f == c - d and not (e - f == a - b and (c < a < e or c > a > e)):
            return 1

        return 2
