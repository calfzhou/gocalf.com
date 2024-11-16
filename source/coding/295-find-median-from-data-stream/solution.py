class MaxHeap:
    def __init__(self) -> None:
        self._store = []

    @property
    def size(self):
        return len(self._store)

    @property
    def top(self):
        return self._store[0]

    def add(self, value: int) -> None:
        n = len(self._store)
        self._store.append(value)
        self._shift_up(n)

    def pop(self) -> int:
        if len(self._store) == 1:
            return self._store.pop()

        top = self._store[0]
        self._store[0] = self._store.pop()
        self._shift_down(0)
        return top

    def _shift_up(self, pos: int) -> None:
        """Shifts store[pos] up to proper new position."""
        while pos > 0:
            parent = (pos - 1) >> 1
            if self._store[parent] < self._store[pos]:
                self._store[parent], self._store[pos] = self._store[pos], self._store[parent]
                pos = parent
            else:
                return

    def _shift_down(self, pos: int) -> None:
        """Shifts store[pos] down to proper new position."""
        n = len(self._store)
        leaf = n >> 1
        while pos < leaf:
            left = (pos << 1) + 1
            right = left + 1
            child = right if right < n and self._store[right] > self._store[left] else left
            if self._store[pos] < self._store[child]:
                self._store[pos], self._store[child] = self._store[child], self._store[pos]
                pos = child
            else:
                return


class MedianFinder:

    def __init__(self):
        self._left = MaxHeap()
        self._right = MaxHeap()

    def addNum(self, num: int) -> None:
        if self._left.size == 0 or num < self._left.top:
            self._left.add(num)
        else:
            self._right.add(-num)

        if self._left.size > self._right.size + 1:
            self._right.add(-self._left.pop())
        elif self._right.size > self._left.size + 1:
            self._left.add(-self._right.pop())

    def findMedian(self) -> float:
        if self._left.size > self._right.size:
            return self._left.top
        elif self._right.size > self._left.size:
            return -self._right.top

        return (self._left.top - self._right.top) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
