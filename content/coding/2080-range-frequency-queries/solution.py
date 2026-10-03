from bisect import bisect_left, bisect_right
from collections import defaultdict


class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self._container: dict[int, list[int]] = defaultdict(list) # {value: [index, ...]}
        for i, value in enumerate(arr):
            self._container[value].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self._container:
            return 0

        indices = self._container[value]
        return bisect_right(indices, right) - bisect_left(indices, left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
