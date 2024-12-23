from bisect import bisect_left


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = [-1, n]

    def dis(self, l: int, r: int) -> int:
        if l == -1:
            return r
        elif r == self.n:
            return self.n - l - 1
        else:
            return (r - l) >> 1

    def seat(self) -> int:
        max_dis = 0
        idx = -1
        seat = -1
        left = self.seats[0]
        for i in range(1, len(self.seats)):
            right = self.seats[i]
            dis = self.dis(left, right)
            if dis > max_dis:
                max_dis = dis
                idx = i
                seat = 0 if left == -1 else left + dis
            left = right

        self.seats.insert(idx, seat)
        return seat

    def leave(self, p: int) -> None:
        idx = bisect_left(self.seats, p)
        del self.seats[idx]


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
