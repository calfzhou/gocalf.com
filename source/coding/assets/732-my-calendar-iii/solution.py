from bisect import bisect_left
from math import inf


max2 = lambda a, b: a if a >= b else b


class MyCalendarThree:

    def __init__(self):
        self._occupies: list[list[int]] = [[-inf, 0], [inf, 0]] # [time, occupied events count]
        self._max_occupy = 0

    def book(self, startTime: int, endTime: int) -> int:
        i = bisect_left(self._occupies, [startTime])
        j = bisect_left(self._occupies, [endTime])
        if endTime < self._occupies[j][0]:
            self._occupies.insert(j, [endTime, self._occupies[j-1][1]])
        for k in range(i, j):
            self._occupies[k][1] += 1
        if startTime < self._occupies[i][0]:
            self._occupies.insert(i, [startTime, self._occupies[i-1][1] + 1])

        self._max_occupy = max2(self._max_occupy, max(self._occupies[k][1] for k in range(i, j + 1)))
        return self._max_occupy


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
