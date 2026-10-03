class MedianFinder:

    def __init__(self):
        self._store = [0] * 101
        self._size = 0
        self._mid_num = None
        self._mid_offset = 0

    def _next(self, num: int) -> int:
        return next(v for v in range(num + 1, 101) if self._store[v] > 0)

    def _prev(self, num: int) -> int:
        return next(v for v in range(num - 1, -1, -1) if self._store[v] > 0)

    def addNum(self, num: int) -> None:
        self._store[num] += 1

        if self._mid_num is None:
            self._mid_num = num
        elif num >= self._mid_num and self._size & 1 == 0:
            self._mid_offset += 1
            if self._mid_offset == self._store[self._mid_num]:
                self._mid_num = self._next(self._mid_num)
                self._mid_offset = 0
        elif num < self._mid_num and self._size & 1 == 1:
            self._mid_offset -= 1
            if self._mid_offset < 0:
                self._mid_num = self._prev(self._mid_num)
                self._mid_offset = self._store[self._mid_num] - 1

        self._size += 1

    def findMedian(self) -> float:
        if self._size & 1 == 1 or self._mid_offset < self._store[self._mid_num] - 1:
            return self._mid_num
        else:
            return (self._mid_num + self._next(self._mid_num)) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
