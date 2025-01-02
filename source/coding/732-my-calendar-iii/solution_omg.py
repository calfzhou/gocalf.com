from bisect import bisect_left
from math import inf


min2 = lambda a, b: a if a <= b else b
max2 = lambda a, b: a if a >= b else b


class MyCalendarThree:

    def __init__(self):
        self._occupies: list[tuple[int, int, int]] = [(-inf, -inf, 0), (inf, inf, 0)] # (start, end, events count)
        self._max_occupy = 0

    def book(self, startTime: int, endTime: int) -> int:
        i = bisect_left(self._occupies, (startTime,))
        if self._occupies[i-1][1] <= startTime and endTime <= self._occupies[i][0]:
            # Not overlap with another events.
            self._occupies.insert(i, (startTime, endTime, 1))
            self._max_occupy = max2(self._max_occupy, 1)
            return self._max_occupy

        new_occupies = []
        start = startTime
        if self._occupies[i-1][1] > startTime:
            i -= 1
            new_occupies.append((
                self._occupies[i][0],
                start,
                self._occupies[i][2],
            ))
        elif startTime < self._occupies[i][0]:
            new_occupies.append((
                start,
                self._occupies[i][0],
                1,
            ))
            start = new_occupies[-1][1]

        il = i
        while self._occupies[i][0] < endTime:
            if self._occupies[i][1] < endTime:
                new_occupies.append((
                    start,
                    self._occupies[i][1],
                    self._occupies[i][2] + 1,
                ))
                new_occupies.append((
                    self._occupies[i][1],
                    min2(endTime, self._occupies[i+1][0]),
                    1,
                ))
            else:
                new_occupies.append((
                    start,
                    endTime,
                    self._occupies[i][2] + 1,
                ))
                if endTime < self._occupies[i][1]:
                    new_occupies.append((
                        endTime,
                        self._occupies[i][1],
                        self._occupies[i][2],
                    ))
            i += 1
            start = self._occupies[i][0]

        if start < endTime:
            new_occupies.append((
                start,
                endTime,
                1,
            ))

        self._occupies[il:i] = new_occupies
        self._max_occupy = max2(self._max_occupy, max(cnt for _, _, cnt in new_occupies))
        return self._max_occupy


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
