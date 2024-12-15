from heapq import heapify, heapreplace


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        n = len(classes)
        queue = [((t-p)/(t+1) - (t-p)/t, t - p, t) for p, t in classes]
        heapify(queue)
        for _ in range(extraStudents):
            _, f, t = queue[0]
            t += 1
            heapreplace(queue, (f/(t+1) - f/t, f, t))

        return 1 - sum(f/t for _, f, t in queue) / n
