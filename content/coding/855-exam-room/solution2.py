from heapq import heapify, heappush, heapreplace


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.heap = [(-self.dis(-1, n), -1, n)]

    def dis(self, l: int, r: int) -> int:
        if l == -1:
            return r
        elif r == self.n:
            return self.n - l - 1
        else:
            return (r - l) >> 1

    def seat(self) -> int:
        dis, left, right = self.heap[0]
        seat = 0 if left == -1 else left - dis
        res = (-self.dis(left, seat), left, seat)
        heapreplace(self.heap, res)
        res = (-self.dis(seat, right), seat, right)
        heappush(self.heap, res)
        return seat

    def leave(self, p: int) -> None:
        i, j = filter(lambda i: self.heap[i][1] == p or self.heap[i][2] == p, range(len(self.heap)))
        if self.heap[j][1] == p:
            left, right = self.heap[i][1], self.heap[j][2]
        else:
            left, right = self.heap[j][1], self.heap[i][2]

        del self.heap[j]
        del self.heap[i]
        heapify(self.heap)
        res = (-self.dis(left, right), left, right)
        heappush(self.heap, res)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
