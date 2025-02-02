class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min2 = lambda a, b: a if a <= b else b
        height = m
        width = n
        for op in ops:
            height = min2(height, op[0])
            width = min2(width, op[1])

        return height * width
