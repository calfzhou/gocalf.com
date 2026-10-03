from collections import defaultdict


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

    def contains(self, row: int, col: int) -> bool:
        return self.top <= row <= self.bottom and self.left <= col <= self.right


def has_circle(graph: dict[int, set[int]]) -> bool:
    nodes = {u: False for u in graph} # False: not processed; True: processing; <Removed>: finished.
    while nodes:
        stack = [next(iter(nodes))]
        while stack:
            u = stack.pop()
            if u not in nodes: # `u` is already finished.
                continue
            elif nodes[u]: # `u` is under processing, then finish it.
                nodes.pop(u)
                continue

            nodes[u] = True # `u` is not processed, mark it processing.
            stack.append(u)
            for v in graph[u]:
                if v in nodes:
                    if nodes[v]: # If `v` is under processing, there is a circle.
                        return True
                    stack.append(v) # `v` is not processed (and not finished).

    return False


def has_circle2(graph: dict[int, set[int]]) -> bool:
    in_degrees = defaultdict(int, {u: 0 for u in graph}) # u: u's in-degree.
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1

    while in_degrees:
        zero = next((u for u, d in in_degrees.items() if d == 0), None)
        if zero is None:
            return True

        in_degrees.pop(zero)
        for v in graph[zero]:
            if v in in_degrees:
                in_degrees[v] -= 1

    return False


class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        m = len(targetGrid)
        n = len(targetGrid[0])

        # Get surrounding boxes for each color.
        boxes: dict[int, Rect] = {} # {color: surrounding rectangle}
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                if c not in boxes:
                    boxes[c] = Rect(i, j)
                else:
                    boxes[c].extend(i, j)

        # Build a dependency graph.
        graph: dict[int, set[int]] = defaultdict(set) # {color: other colors should print later}
        # graph = {c: set() for c in boxes}
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                for c2, box in boxes.items():
                    if c2 != c and box.contains(i, j):
                        graph[c2].add(c)

        return not has_circle(graph)
