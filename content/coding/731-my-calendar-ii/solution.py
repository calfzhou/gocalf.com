from bisect import bisect_left
from math import inf


Range = tuple[int, int]
min2 = lambda a, b: a if a <= b else b
max2 = lambda a, b: a if a >= b else b


class MyCalendarTwo:

    def __init__(self):
        self._single_occupies: list[Range] = [(-inf, -inf), (inf, inf)]
        self._double_occupies: list[Range] = [(-inf, -inf), (inf, inf)]

    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self._double_occupies, (startTime, endTime))
        if self._double_occupies[i-1][1] > startTime or self._double_occupies[i][0] < endTime:
            return False

        new_doubles = []
        j = bisect_left(self._single_occupies, (startTime, endTime))
        jl = j
        if self._single_occupies[jl-1][1] > startTime:
            jl -= 1
            new_doubles.append((
                startTime,
                min2(self._single_occupies[jl][1], endTime),
            ))
        while self._single_occupies[j][0] < endTime:
            new_doubles.append((
                self._single_occupies[j][0],
                min2(self._single_occupies[j][1], endTime),
            ))
            j += 1
        self._single_occupies[jl:j] = [(
            min2(self._single_occupies[jl][0], startTime),
            max2(self._single_occupies[j-1][1], endTime),
        )]

        self._double_occupies[i:i] = new_doubles
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
