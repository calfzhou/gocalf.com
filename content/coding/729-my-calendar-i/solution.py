from bisect import bisect_left


class MyCalendar:

    def __init__(self):
        self._events: list[tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self._events, (startTime, endTime)) # events[i] >= (startTime, endTime)
        if i > 0: # events[i-1].start < startTime, need check events[i-1].end vs startTime.
            if self._events[i-1][1] > startTime: return False
        if i < len(self._events): # events[i].start >= startTime, need check events[i].start vs endTime.
            if endTime > self._events[i][0]: return False

        self._events.insert(i, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
