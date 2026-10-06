from itertools import product
from typing import Iterable


min2 = lambda a, b: a if a <= b else b
max2 = lambda a, b: a if a >= b else b


class Rect:
    def __init__(self, row: int, col: int) -> None:
        self.top = self.bottom = row
        self.left = self.right = col

    def extend(self, row: int, col: int) -> None:
        # self.top = min2(self.top, row)
        self.bottom = max2(self.bottom, row)
        self.left = min2(self.left, col)
        self.right = max2(self.right, col)

    def __iter__(self) -> Iterable[tuple[int, int]]:
        yield from product(range(self.top, self.bottom+1), range(self.left, self.right+1))


class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        m = len(targetGrid)
        n = len(targetGrid[0])
        boxes: dict[int, Rect] = {} # {color: surrounding rectangle}
        for i, j in product(range(m), range(n)):
            color = targetGrid[i][j]
            if color not in boxes:
                boxes[color] = Rect(i, j)
            else:
                boxes[color].extend(i, j)

        def printable(color: int) -> bool:
            box = boxes[color]

            for i, j in box:
                if targetGrid[i][j] != color and targetGrid[i][j] > 0:
                    return False

            for i, j in box:
                targetGrid[i][j] = 0

            return True

        colors = set(boxes)
        while colors:
            printed = set(filter(printable, colors))
            if not printed: return False
            colors -= printed

        return True
