from collections import defaultdict


min2 = lambda a, b: a if a <= b else b
max2 = lambda a, b: a if a >= b else b


class Rect:
    def __init__(self, row: int, col: int) -> None:
        self.top = self.bottom = row
        self.left = self.right = col
        self.area = 1

    def extend(self, row: int, col: int) -> None:
        if self.contains(row, col): return
        # self.top = min2(self.top, row)
        self.bottom = max2(self.bottom, row)
        self.left = min2(self.left, col)
        self.right = max2(self.right, col)
        self.area = (self.bottom - self.top + 1) * (self.right - self.left + 1)

    def contains(self, row: int, col: int) -> bool:
        return self.top <= row <= self.bottom and self.left <= col <= self.right


class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        m = len(targetGrid)
        n = len(targetGrid[0])
        boxes: dict[int, Rect] = {} # {color: surrounding rectangle}
        counts: dict[int, int] = defaultdict(int) # {color: number of cells can be printed to this color}
        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                counts[color] += 1
                if color not in boxes:
                    boxes[color] = Rect(i, j)
                else:
                    boxes[color].extend(i, j)

        while counts:
            color = next((c for c, cnt in counts.items() if cnt == boxes[c].area), None)
            if color is None:
                return False

            box = boxes[color]
            for i in range(box.top, box.bottom + 1):
                for j in range(box.left, box.right + 1):
                    if targetGrid[i][j] != color: continue
                    for c2 in counts:
                        box2 = boxes[c2]
                        if c2 != color and box2.contains(i, j):
                            counts[c2] += 1

            counts.pop(color)

        return True
