from bisect import bisect_left


Range = tuple[int, int] # (start, end)


class Allocator:

    def __init__(self, n: int):
        self._free = [(0, n)] # [range of a contiguous free block]
        self._allocated: dict[int, list[Range]] = {} # mID -> [range]

    def allocate(self, size: int, mID: int) -> int:
        if (size, mID) == (28, 96):
            print(self._free, self._allocated)
        for i, (start, end) in enumerate(self._free):
            if end - start >= size:
                if mID not in self._allocated:
                    self._allocated[mID] = []
                self._allocated[mID].append((start, start + size))

                if end - start == size:
                    self._free.pop(i)
                else:
                    self._free[i] = (start + size, end)

                return start

        return -1

    def freeMemory(self, mID: int) -> int:
        if mID not in self._allocated:
            return 0

        total = 0
        units = self._allocated.pop(mID)
        for start, end in units:
            total += end - start
            i = bisect_left(self._free, (start, end))
            if i > 0 and self._free[i - 1][1] == start:
                i -= 1
                start = self._free.pop(i)[0]
            if i < len(self._free) and self._free[i][0] == end:
                end = self._free.pop(i)[1]
            self._free.insert(i, (start, end))

        return total


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
