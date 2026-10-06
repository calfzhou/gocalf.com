from bisect import bisect_left
from collections import defaultdict


class NumberContainers:

    def __init__(self):
        self._numbers: dict[int, int] = {} # index -> number
        self._indices: dict[int, list[int]] = defaultdict(list) # number -> sorted list of indices

    def change(self, index: int, number: int) -> None:
        if index in self._numbers and self._numbers[index] == number:
            return

        if index in self._numbers:
            old_number = self._numbers[index]
            indices = self._indices[old_number]
            del indices[bisect_left(indices, index)]

        self._numbers[index] = number
        indices = self._indices[number]
        indices.insert(bisect_left(indices, index), index)

    def find(self, number: int) -> int:
        if number not in self._indices:
            return -1

        indices = self._indices[number]
        if not indices:
            return -1

        return indices[0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
